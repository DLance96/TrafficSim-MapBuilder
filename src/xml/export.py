import xml.etree.ElementTree as ET
from src.map.constants import ROAD_IN_ENTRANCE_PT_INDEX, ROAD_OUT_ENTRANCE_PT_INDEX


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
        ET.SubElement(temp_road, "length").text = road.get_length()
        ET.SubElement(temp_road, "incoming_lanes").text = road.get_in_lanes()
        ET.SubElement(temp_road, "outgoing_lanes").text = road.get_out_lanes()

        ET.SubElement(temp_road, "angle_radians").text = road.get_angle()
        temp_coord = road.get_points()[ROAD_IN_ENTRANCE_PT_INDEX]
        ET.SubElement(temp_road, "incoming_entrance_corner").text = temp_coord.get_x() + " " + temp_coord.get_y()
        temp_coord = road.get_points()[ROAD_OUT_ENTRANCE_PT_INDEX]
        ET.SubElement(temp_road, "outgoing_entrance_corner").text = temp_coord.get_x() + " " + temp_coord.get_y()

        ET.SubElement(temp_road, "speed_limit").text = ""  # TODO change when speed limit is added

        if road.get_out_intersection() is not None:
            ET.SubElement(temp_road, "outgoing_intersection").text = intersections.index(road.get_out_intersection())
        if road.get_in_intersection() is not None:
            ET.SubElement(temp_road, "incoming_intersection").text = intersections.index(road.get_in_intersection())

    for index, intersection in enumerate(intersections):
        temp_intersection = ET.SubElement(intersection_elements, "intersection", name=index)
        ET.SubElement(temp_intersection, "center_point").text = intersection.get_center()
        ET.SubElement(temp_intersection, "radius").text = intersection.get_radius()
        temp_connections = ET.SubElement(temp_intersection, "connections")
        for connected_road in intersection.get_connections:
            ET.SubElement(temp_connections, "connection_road").text = roads.index(connected_road)

    tree = ET.ElementTree(traffic_map)
    tree.write(save_location)


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
        if road.get_out_intersection() is not None and road.get_out_intersection() not in visited_intersections:
            new_roads.extend(road.get_out_intersection().get_connections())
            visited_intersections.extend(road.get_out_intersection())
        if road.get_in_intersection() is not None and road.get_in_intersection() not in visited_intersections:
            new_roads.extend(road.get_in_intersection().get_connections())
            visited_intersections.extend(road.get_in_intersection())
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
    export([], [], "temp.xml")
