import math
import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml_parse.Exceptions import XMLFormatError
from src.xml_parse.Constants import IMPORT_ROAD_TOLERANCE
from src.xml_parse.Utils import is_connected_traffic_map, distance, add_angles
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

    if not is_connected_traffic_map(roads, intersections):
        raise XMLFormatError('Traffic Map is not connected')
    validate_geometry(roads, intersections)

    return roads, intersections


def generate_road(road, intersections):
    if road.find('length') is None:
        raise XMLFormatError('Missing length in a road')
    length = float(road.find('length').text)
    if road.find('incoming_lanes') is None:
        raise XMLFormatError('Missing incoming lanes count in road')
    in_lanes = int(road.find('incoming_lanes').text)
    if road.find('outgoing_lanes') is None:
        raise XMLFormatError('Missing outgoing lanes count in road')
    out_lanes = int(road.find('outgoing_lanes').text)
    if road.find('angle_radians') is None:
        raise XMLFormatError('Missing angle in road')
    angle = float(road.find('angle_radians').text)
    if road.find('anchor_point') is None:
        raise XMLFormatError('Missing anchor point in road')
    coords = road.find('anchor_point').text.split(' ')
    try:
        anchor_point = Coordinates(float(coords[0]), float(coords[1]))
    except ValueError:
        raise XMLFormatError('Anchor coordinates not floats in format \"{float} {float}\"')
    if road.find('speed_limit') is None:
        raise XMLFormatError('Missing speed limit in road')
    speed_limit = int(road.find('speed_limit').text)  # TODO: update when speed limit added

    return_road = Road.create_import_road(length, out_lanes, in_lanes, angle)
    add_connections(return_road, road.find('start_intersection'), road.find('end_intersection'), intersections)
    convert_to_mapbuilder_size(return_road, anchor_point)

    return return_road


def generate_intersection(intersection):
    if intersection.find('center_point') is None:
        raise XMLFormatError('Missing center point in a intersection')
    coords = intersection.find('center_point').text.split(' ')
    try:
        center_point = Coordinates(float(coords[0]), float(coords[1]))
    except ValueError:
        raise XMLFormatError('Center coordinates not floats in format \"{float} {float}\"')
    if intersection.find('radius') is None:
        raise XMLFormatError('Missing radius in a intersection')
    radius = int(intersection.find('radius').text)

    return Intersection(center_point, radius)


def validate_geometry(roads, intersections):
    for road in roads:
        start_intersection = road.get_start_connection()
        end_intersection = road.get_end_connection()

        if start_intersection is not None:
            if not math.isclose(distance(road.get_start_coords(), start_intersection.get_center()),
                                start_intersection.get_radius(), rel_tol=IMPORT_ROAD_TOLERANCE):
                raise XMLFormatError('Road start point not on intersection edge')
        if end_intersection is not None:
            if not math.isclose(distance(road.get_end_coords(), end_intersection.get_center()),
                                end_intersection.get_radius(), rel_tol=IMPORT_ROAD_TOLERANCE):
                raise XMLFormatError('Road end point not on intersection edge')
    for intersection in intersections:
        check_overload_intersection(intersection)
    return True


def add_connections(road, start, end, intersections):
    if start is not None:
        if not 0 <= int(start.text) < len(intersections):
            raise XMLFormatError('Start intersection does not exist')
        road.add_start_connection(intersections[int(start.text)])
        intersections[int(start.text)].add_outgoing_connection(road)
    if end is not None:
        if not 0 <= int(end.text) < len(intersections):
            raise XMLFormatError('End intersection does not exist')
        road.add_end_connection(intersections[int(end.text)])
        intersections[int(end.text)].add_incoming_connection(road)


def convert_to_mapbuilder_size(road, anchor_point):
    length = road.get_length()
    road_width = (road.get_in_lanes() + road.get_out_lanes()) * LANE_WIDTH
    start_intersection = road.get_start_connection()
    end_intersection = road.get_end_connection()

    temp_point = Coordinates(anchor_point.get_x() + math.cos(road.angle) * road.get_length(),
                             anchor_point.get_y() + math.sin(road.angle) * road.get_length())
    end_anchor_point = Coordinates(temp_point.get_x() + math.cos(road.angle + math.pi / 2) * road_width,
                                   temp_point.get_y() + math.sin(road.angle + math.pi / 2) * road_width)

    if start_intersection is not None:
        chord_center = get_chord_center(road.get_angle(), road_width, anchor_point)
        if not in_intersection(start_intersection, chord_center):
            raise XMLFormatError('Center chord point of road not in intersection')
        start = Coordinates(start_intersection.get_center().get_x() + math.cos(road.get_angle() *
                                                                               start_intersection.get_radius()),
                            start_intersection.get_center().get_y() + math.sin(road.get_angle() *
                                                                               start_intersection.get_radius()))
        length -= distance(chord_center, start)
    else:
        start = get_chord_center(road.get_angle(), road_width, anchor_point)

    if end_intersection is not None:
        chord_center = get_chord_center(add_angles(road.get_angle(), math.pi), road_width, end_anchor_point)
        if not in_intersection(end_intersection, chord_center):
            raise XMLFormatError('End chord point of road not in intersection')
        end = Coordinates(end_intersection.get_center().get_x() +
                          math.cos(add_angles(road.get_angle(), math.pi)) * end_intersection.get_radius(),
                          end_intersection.get_center().get_y() +
                          math.sin(add_angles(road.get_angle(), math.pi)) * end_intersection.get_radius())
        length -= distance(chord_center, end)
    else:
        end = get_chord_center(add_angles(road.get_angle() + math.pi), road_width, end_anchor_point)

    road.update_start_coords(start)
    road.update_end_coords(end)
    road.update_length(length)
    pass


def check_overload_intersection(intersection):
    road_angle_pairs = list()  # List of of angles where the roads edges intersect the intersection


def get_chord_center(angle_of_perpendicular, chord_length, anchor_point):
    angle = add_angles(angle_of_perpendicular, math.pi / 2)
    return Coordinates(anchor_point.get_x() + math.cos(angle) * chord_length / 2,
                       anchor_point.get_y() + math.sin(angle) * chord_length / 2)


def in_intersection(intersection, point):
    return True if distance(intersection.get_center(), point) < intersection.get_radius() else False


if __name__ == '__main__':
    chord_center = get_chord_center(0, 10, Coordinates(0, -5))
    x = chord_center.get_x()
    y = chord_center.get_y()
    checkx = math.isclose(x, 0, rel_tol=.00001)
    checky = -.1 < y < .1
    import_xml('temp.xml')
