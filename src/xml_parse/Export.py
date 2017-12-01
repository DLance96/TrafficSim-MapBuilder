import math
import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml_parse.Utils import is_connected_traffic_map
from src.map.Coordinates import Coordinates
from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Constants import LANE_WIDTH


def export_xml(roads, intersections, save_location):
    """
    Main function of export that makes that the map is valid and then creates an xml file
    :param roads: list of the roads in the map
    :param intersections: list of the roads in the map
    :param save_location: where to save the xml file
    :return:
    """
    if is_connected_traffic_map(roads, intersections) and valid_intersections(intersections):
        make_xml(roads, intersections, save_location)
    else:
        print("Fail export")
        return  # TODO decide what to do with incomplete map


def make_xml(roads, intersections, save_location):
    """
    Creates an xml document from a map and saves it to a given location
    :param roads: list of roads in the map
    :param intersections: list of intersections in the mpa
    :param save_location: location of the xml file
    :return:
    """
    traffic_map = ET.Element("map")

    for index, road in enumerate(roads):
        temp_road = ET.SubElement(traffic_map, "road", name=str(index))
        length, anchor_coordinate = convert_road_to_simulation_size(road)

        ET.SubElement(temp_road, "length").text = str(length)
        ET.SubElement(temp_road, "incoming_lanes").text = str(road.get_in_lanes())
        ET.SubElement(temp_road, "outgoing_lanes").text = str(road.get_out_lanes())

        ET.SubElement(temp_road, "angle_radians").text = str(road.get_angle())
        ET.SubElement(temp_road, "anchor_point").text = \
            "{} {}".format(anchor_coordinate.get_x(), anchor_coordinate.get_y())

        ET.SubElement(temp_road, "speed_limit").text = "30"  # TODO change when speed limit is added

        if road.get_start_connection() is not None:
            ET.SubElement(temp_road, "start_intersection").text = \
                str(intersections.index(road.get_start_connection()))
        if road.get_end_connection() is not None:
            ET.SubElement(temp_road, "end_intersection").text = \
                str(intersections.index(road.get_end_connection()))

    for index, intersection in enumerate(intersections):
        temp_intersection = ET.SubElement(traffic_map, "intersection", name=str(index))
        ET.SubElement(temp_intersection, "center_point").text = "{} {}".format(intersection.get_center().get_x(),
                                                                               intersection.get_center().get_y())
        ET.SubElement(temp_intersection, "radius").text = str(intersection.get_radius())

    tree = ET.ElementTree(traffic_map)
    tree.write(save_location)


def convert_road_to_simulation_size(road):
    """
    Takes a road and moves it slightly into the intersections on its ends so that the end of the road create a chord
    with the intersection so that there is no place a car could be where it is not on road or intersection on the
    simulation side of things
    :param road: the Road to be adjusted
    :return: tuple of length and anchor_coordinate to be added the the xml file
    """
    length = road.get_length()
    road_width = (road.get_in_lanes() + road.get_out_lanes()) * LANE_WIDTH

    if road.get_start_connection() is not None:
        intersection = road.get_start_connection()
        intersection_radius = road.get_start_connection().get_radius()
        # gets angle that the anchor point is from the midpoint
        chord_angle = math.asin((road_width/2.0)/intersection_radius)
        # rotates to where the road is on the intersection
        angle_to_anchor = road.get_angle() - chord_angle
        # adds length between chord and original center point
        length += intersection_radius - math.cos(chord_angle) * intersection_radius
        # gets new anchor point with polar coordinates
        anchor_coordinate = Coordinates(intersection.get_center().get_x() + intersection_radius *
                                        math.cos(angle_to_anchor),
                                        intersection.get_center().get_y() + intersection_radius *
                                        math.sin(angle_to_anchor))
    else:
        anchor_coordinate = Coordinates(road.get_start_coords().get_x() +
                                        math.cos(road.get_angle() - math.pi / 2) * (road_width / 2),
                                        road.get_start_coords().get_y() +
                                        math.sin(road.get_angle() - math.pi / 2) * (road_width / 2))
    if road.get_end_connection() is not None:
        intersection_radius = road.get_end_connection().get_radius()
        chord_angle = math.asin((road_width / 2) / intersection_radius)
        # adds length between chord and original center point
        length += intersection_radius - \
            math.cos(chord_angle) * intersection_radius

    return length, anchor_coordinate


def valid_intersections(intersections):
    """
    Check to make sure that no intersection has roads that overlap
    :param intersections: list of intersections to check
    :return: boolean whether all intersections are valid
    """
    # TODO check to make sure no overlapping roads on any intersection
    return True


if __name__ == '__main__':
    roads = []
    intersections = []
    intersection1 = Intersection(Coordinates(100, 640), 30)
    intersection2 = Intersection(Coordinates(640, 640), 30)
    intersection3 = Intersection(Coordinates(640, 100), 30)
    intersection4 = Intersection(Coordinates(100, 100), 30)
    road1 = Road(Coordinates(130, 640), Coordinates(610, 640), 480, 2, 2, 0)
    road2 = Road(Coordinates(640, 610), Coordinates(640, 130), 480, 2, 2, 3 * math.pi / 2)
    road3 = Road(Coordinates(610, 100), Coordinates(130, 100), 480, 2, 2, math.pi)
    road4 = Road(Coordinates(100, 130), Coordinates(100, 610), 480, 2, 2, math.pi / 2)
    intersection1.add_outgoing_connection(road1)
    intersection1.add_incoming_connection(road4)
    intersection2.add_outgoing_connection(road2)
    intersection2.add_incoming_connection(road1)
    intersection3.add_outgoing_connection(road3)
    intersection3.add_incoming_connection(road2)
    intersection4.add_outgoing_connection(road4)
    intersection4.add_incoming_connection(road3)
    road1.add_start_connection(intersection1)
    road1.add_end_connection(intersection2)
    road2.add_start_connection(intersection2)
    road2.add_end_connection(intersection3)
    road3.add_start_connection(intersection3)
    road3.add_end_connection(intersection4)
    road4.add_start_connection(intersection4)
    road4.add_end_connection(intersection1)

    roads.append(road1)
    roads.append(road2)
    roads.append(road3)
    roads.append(road4)
    intersections.append(intersection1)
    intersections.append(intersection2)
    intersections.append(intersection3)
    intersections.append(intersection4)
    export_xml(roads, intersections, "temp.xml")
    pass

