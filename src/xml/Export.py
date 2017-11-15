import math
import sys
import os
import xml.etree.ElementTree as ET

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml.Utils import is_connected_traffic_map
from src.map.Coordinates import Coordinates
from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Constants import ROAD_IN_ENTRANCE_PT_INDEX, ROAD_OUT_ENTRANCE_PT_INDEX, LANE_WIDTH


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
    road_elements = ET.SubElement(traffic_map, "roads")
    intersection_elements = ET.SubElement(traffic_map, "intersections")

    for index, road in enumerate(roads):
        temp_road = ET.SubElement(road_elements, "road", name=str(index))
        length, anchor_coordinate = convert_road_to_simulation_size(road)

        ET.SubElement(temp_road, "length").text = str(length)
        ET.SubElement(temp_road, "incoming_lanes").text = str(road.get_in_lanes())
        ET.SubElement(temp_road, "outgoing_lanes").text = str(road.get_out_lanes())

        ET.SubElement(temp_road, "angle_radians").text = str(road.get_angle())
        ET.SubElement(temp_road, "anchor_point").text = \
            "{} {}".format(anchor_coordinate.get_x(), anchor_coordinate.get_y())

        ET.SubElement(temp_road, "speed_limit").text = "200"  # TODO change when speed limit is added

        if road.get_start_connection() is not None:
            ET.SubElement(temp_road, "start_intersection").text = \
                str(intersections.index(road.get_start_connection()))
        if road.get_end_connection() is not None:
            ET.SubElement(temp_road, "end_intersection").text = \
                str(intersections.index(road.get_end_connection()))

    for index, intersection in enumerate(intersections):
        temp_intersection = ET.SubElement(intersection_elements, "intersection", name=str(index))
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
    anchor_coordinate = road.get_points()[ROAD_OUT_ENTRANCE_PT_INDEX]
    road_width = (road.get_in_lanes() + road.get_out_lanes()) * LANE_WIDTH

    if road.get_start_connection() is not None:
        intersection_radius = road.get_start_connection().get_radius()
        # gets angle that the anchor point is from the midpoint
        angle_to_anchor = math.asin((road_width/2)/intersection_radius)
        # rotates to where the road is on the intersection
        angle_to_anchor = angle_to_anchor + road.get_angle()
        # removes over rotation
        while angle_to_anchor > 2 * math.pi:
            angle_to_anchor -= 2 * math.pi
        # adds length between chord and original center point
        length += road.get_start_connection().get_radius() - \
                  math.cos(angle_to_anchor) * intersection_radius
        # gets new anchor point with polar coordinates
        anchor_coordinate = Coordinates(intersection_radius * math.cos(angle_to_anchor),
                                                                       intersection_radius * math.sin(angle_to_anchor))
    if road.get_end_connection() is not None:
        intersection_radius = road.get_end_connection().get_radius()
        angle_to_anchor = math.asin((road_width / 2) / intersection_radius)
        # rotates to where the road is on the intersection (adds pi to get opposite angle because it is end connection)
        angle_to_anchor = angle_to_anchor + road.get_angle() + math.pi
        # removes over rotation
        while angle_to_anchor > 2 * math.pi:
            angle_to_anchor -= 2 * math.pi
        # adds length between chord and original center point
        length += road.get_end_connection().get_radius() - \
            math.cos(angle_to_anchor) * intersection_radius

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
    intersection = Intersection(Coordinates(50, 70), 20)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi / 2)
    intersection.add_incoming_connection(road)
    road.add_end_connection(intersection)
    roads.append(road)
    intersections.append(intersection)
    export_xml(roads, intersections, "temp.xml")

