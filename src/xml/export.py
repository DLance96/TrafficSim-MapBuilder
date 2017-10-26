import xml.etree.ElementTree as ET
import math
from src.map.coordinates import Coordinates
from src.map.constants import ROAD_IN_ENTRANCE_PT_INDEX, ROAD_OUT_ENTRANCE_PT_INDEX, LANE_WIDTH


def export_xml(roads, intersections, save_location):
    """
    Main function of export that makes that the map is valid and then creates an xml file
    :param roads: list of the roads in the map
    :param intersections: list of the roads in the map
    :param save_location: where to save the xml file
    :return:
    """
    if is_connected(roads, intersections) and valid_intersections(intersections):
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
        temp_road = ET.SubElement(road_elements, "road", name=index)
        length, anchor_coordinate = convert_road_to_simulation_size(road)

        ET.SubElement(temp_road, "length").text = length
        ET.SubElement(temp_road, "incoming_lanes").text = road.get_in_lanes()
        ET.SubElement(temp_road, "outgoing_lanes").text = road.get_out_lanes()

        ET.SubElement(temp_road, "angle_radians").text = road.get_angle()
        ET.SubElement(temp_road, "anchor_point").text = anchor_coordinate.get_x() + " " + anchor_coordinate.get_y()

        ET.SubElement(temp_road, "speed_limit").text = ""  # TODO change when speed limit is added

        if road.get_start_connection() is not None:
            ET.SubElement(temp_road, "outgoing_intersection").text = intersections.index(road.get_start_connection())
        if road.get_end_connection() is not None:
            ET.SubElement(temp_road, "incoming_intersection").text = intersections.index(road.get_end_connection())

    for index, intersection in enumerate(intersections):
        temp_intersection = ET.SubElement(intersection_elements, "intersection", name=index)
        ET.SubElement(temp_intersection, "center_point").text = intersection.get_center()
        ET.SubElement(temp_intersection, "radius").text = intersection.get_radius()
        temp_connections = ET.SubElement(temp_intersection, "connections")
        for connected_road in intersection.get_connections:
            ET.SubElement(temp_connections, "connection_road").text = roads.index(connected_road)

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

    return length, anchor_coordinate


def is_connected(roads, intersections):
    """
    Verifies that a collection of intersections and roads is fully connected
    :param roads: list of roads in the map
    :param intersections: list of intersections in the map
    :return: boolean on whether the map is fully connected
    """
    to_visit_roads = []
    visited_roads = []
    visited_intersections = []

    if len(roads) == 0:
        if len(intersections) == 0 or len(intersections) == 1:
            return True
        else:
            return False

    to_visit_roads.extend(roads.pop())

    while len(to_visit_roads) > 0:
        road = to_visit_roads.pop()
        new_roads = []
        if road.get_start_connection() is not None and road.get_start_connection() not in visited_intersections:
            new_roads.extend(road.get_start_connection().get_connections())
            visited_intersections.extend(road.get_start_connection())
        if road.get_end_connection() is not None and road.get_end_connection() not in visited_intersections:
            new_roads.extend(road.get_end_connection().get_connections())
            visited_intersections.extend(road.get_end_connection())
        remove_visited_roads(new_roads, visited_roads)

    if len(roads) == len(visited_roads) and len(intersections) == len(visited_intersections):
        return True
    else:
        return False


def remove_visited_roads(roads, visited_roads):
    """
    Removes all the previous visted roads from the new roads list
    :param roads: list of new roads to be filtered
    :param visited_roads: list of roads that have already been visited
    :return: removes duplicates between visted roads and roads
    """
    for road in roads:
        if road in visited_roads:
            roads.remove(roads)


def valid_intersections(intersections):
    """
    Check to make sure that no intersection has roads that overlap
    :param intersections: list of intersections to check
    :return: boolean whether all intersections are valid
    """
    # TODO check to make sure no overlapping roads on any intersection
    return True


if __name__ == '__main__':
    export_xml([], [], "temp.xml")
