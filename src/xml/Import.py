import math
import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


def import_xml(filename):

    roads = []
    intersections = []

    if not os.path.isfile(filename):
        raise FileNotFoundError()
    traffic_map = ET.parse(filename)
    root = traffic_map.getroot()
    for road in root.find('roads'):
        roads.append(parse_road(road))
    for intersection in root.find('intersections'):
        intersections.append(generate_intersection(intersection, roads))

    validate_connected(roads, intersections)
    validate_geometry(roads, intersections)

    return roads, intersections


def parse_road(road):
    pass


def generate_intersection(intersection):
    pass


def validate_connected(roads, intersections):
    pass


def validate_geometry(roads, intersections):
    pass


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
