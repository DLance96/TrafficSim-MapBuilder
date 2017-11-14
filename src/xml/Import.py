import math
import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml.Exceptions import XMLFormatError
from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates


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

    validate_connected(roads, intersections)
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
    anchor_point = map(float,road.find('anchor_point').text.split(' '))
    if not road.find('speed_limit'):
        raise XMLFormatError('Missing speed limit in road')
    speed_limit = int(road.find('speed_limit').text)

    start, end, length = convert_to_mapbuilder_size(anchor_point, angle, length, intersections)

    return Road(start, end, length, out_lanes, inc_lanes, angle)


def generate_intersection(intersection):
    if not intersection.find('center_point'):
        raise XMLFormatError('Missing center point in a intersection')
    center_point = map(float, intersection.find('center_point').text.split(' '))
    if not intersection.find('radius'):
        raise XMLFormatError('Missing radius in a intersection')
    radius = float(intersection.find('radius').text)

    return Intersection(Coordinates(center_point[0], center_point[1]), radius)


def validate_connected(roads, intersections):
    pass


def validate_geometry(roads, intersections):
    pass


def convert_to_mapbuilder_size(anchor_point, angle, length, intersections):
    return 0, 0, 0


def distance(coord1, coord2):
    """
    Gets the distance between the two coords
    :param coord1: xy coordinate
    :param coord2: xy coordinate
    :return: float distance
    """
    x_diff = coord1.get_x() - coord2.get_x()
    y_diff = coord1.get_y() - coord2.get_y()
    dist = (x_diff ** 2 + y_diff ** 2) ** .5
    return dist

if __name__ == '__main__':
    import_xml('temp.xml')
