import math
import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml.Exceptions import XMLFormatError
from src.xml.Utils import is_connected_traffic_map, distance, add_angles
from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.Constants import LANE_WIDTH


def import_xml(filename):

    roads = []
    intersections = []

    if not os.path.isfile(filename):
        raise FileNotFoundError()
    traffic_map = ET.parse(filename)
    root = traffic_map.getroot()
    for intersection in root.find('intersections'):
        intersections.append(generate_intersection(intersection))
    for road in root.find('roads'):
        roads.append(generate_road(road, intersections))

    is_connected_traffic_map(roads, intersections)
    validate_geometry(roads, intersections)

    return roads, intersections


def generate_road(road, intersections):
    if not road.find('length'):
        raise XMLFormatError('Missing length in a road')
    length = float(road.find('length').text)
    if not road.find('incoming_lanes'):
        raise XMLFormatError('Missing incoming lanes count in road')
    inc_lanes = int(road.find('incoming_lanes').text)
    if not road.find('outgoing_lanes'):
        raise XMLFormatError('Missing outgoing lanes count in road')
    out_lanes = int(road.find('outgoing_lanes').text)
    if not road.find('angle_radians'):
        raise XMLFormatError('Missing angle in road')
    angle = float(road.find('angle_radians').text)
    if not road.find('anchor_point'):
        raise XMLFormatError('Missing anchor point in road')
    coords = road.find('anchor_point').text.split(' ')
    try:
        anchor_point = Coordinates(float(coords[0]), float(coords[1]))
    except ValueError:
        raise XMLFormatError('Anchor coordinates not floats in format \"{float} {float}\"')
    if not road.find('speed_limit'):
        raise XMLFormatError('Missing speed limit in road')
    speed_limit = int(road.find('speed_limit').text)  # TODO: update when speed limit added

    return_road = Road.create_import_road(length, out_lanes, inc_lanes, angle)
    add_connections(return_road, road, intersections)
    convert_to_mapbuilder_size(return_road, anchor_point)

    return return_road


def generate_intersection(intersection):
    if not intersection.find('center_point'):
        raise XMLFormatError('Missing center point in a intersection')
    center_point = map(float, intersection.find('center_point').text.split(' '))
    if not intersection.find('radius'):
        raise XMLFormatError('Missing radius in a intersection')
    radius = float(intersection.find('radius').text)

    return Intersection(Coordinates(center_point[0], center_point[1]), radius)


def validate_geometry(roads, intersections):
    pass


def add_connections(road, road_xml, intersections):
    if road_xml.find('start_intersection'):
        if not intersections[int(road_xml.find('start_intersection').text)] < len(intersections):
            raise XMLFormatError('Start intersection does not exist')
        road.add_start_connection(intersections[int(road_xml.find('start_intersection').text)])
        intersections[int(road_xml.find('start_intersection').text)].add_outgoing_connection(road)
    if road_xml.find('end_intersection'):
        if intersections[int(road_xml.find('end_intersection').text)] < len(intersections):
            raise XMLFormatError('End intersection does not exist')
        road.add_end_connection(intersections[int(road_xml.find('end_intersection').text)])
        intersections[int(road_xml.find('end_intersection').text)].add_incoming_connection(road)


def convert_to_mapbuilder_size(road, anchor_point):
    length = road.get_length()
    start_intersection = road.get_start_connection()
    end_intersection = road.get_end_connection()
    end_anchor_point = Coordinates(anchor_point.get_x() + math.sin(road.angle) * road.get_length(),
                                   anchor_point.get_y() + math.cos(road.angle) * road.get_length())

    if start_intersection is not None:
        if not in_intersection(start_intersection, get_chord_center(road, anchor_point)):
            raise XMLFormatError('Center chord point of road not in intersection')
        start = Coordinates(start_intersection.get_center().get_x() + math.sin(road.get_angle() *
                                                                               start_intersection.get_radius()),
                            start_intersection.get_center().get_y() + math.cos(road.get_angle() *
                                                                               start_intersection.get_radius()))
        length -= distance(anchor_point, start)
    else:
        start = get_chord_center(road, anchor_point)

    if end_intersection is not None:
        if not in_intersection(end_intersection, get_chord_center(road, end_anchor_point)):
            raise XMLFormatError('End chord point of road not in intersection')
        start = Coordinates(end_intersection.get_center().get_x() + math.sin(add_angles(road.get_angle(), math.pi) *
                                                                             end_intersection.get_radius()),
                            end_intersection.get_center().get_y() + math.cos(add_angles(road.get_angle(), math.pi) *
                                                                             end_intersection.get_radius()))
        length -= distance(anchor_point, start)
    else:
        end = get_chord_center(road, end_anchor_point)

    road.update_start_coords(start)
    road.update_end_coords(end)
    road.update_length(length)
    pass


def get_chord_center(road, anchor_point):
    angle = add_angles(road.get_angle(), -math.pi / 2)
    chord_length = (road.get_in_lanes() + road.get_out_lanes()) * LANE_WIDTH
    return Coordinates(anchor_point.get_x() + math.sin(angle) * chord_length / 2,
                       anchor_point.get_y() + math.cos(angle) * chord_length / 2)


def in_intersection(intersection, point):
    return True if distance(intersection.get_center(), point) < intersection.get_radius() else False

if __name__ == '__main__':
    import_xml('temp.xml')
