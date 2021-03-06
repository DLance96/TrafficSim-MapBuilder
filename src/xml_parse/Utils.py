import math
from src.map.Constants import LANE_WIDTH
from src.xml_parse.Exceptions import XMLFormatError
from src.xml_parse.Constants import SIG_FIGS


def is_connected_traffic_map(roads, intersections):
    # return True
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

    to_visit_roads.append(roads[0])

    while len(to_visit_roads) > 0:
        road = to_visit_roads.pop()
        visited_roads.append(road)
        new_roads = []
        if road.get_start_connection() is not None and road.get_start_connection() not in visited_intersections:
            new_roads.extend(road.get_start_connection().get_connections())
            visited_intersections.append(road.get_start_connection())
        if road.get_end_connection() is not None and road.get_end_connection() not in visited_intersections:
            new_roads.extend(road.get_end_connection().get_connections())
            visited_intersections.append(road.get_end_connection())
        new_roads = list(set(new_roads))
        new_roads = remove_visited_roads(new_roads, visited_roads)
        new_roads = remove_visited_roads(new_roads, to_visit_roads)
        for new_road in new_roads:
            to_visit_roads.append(new_road)

    if len(roads) == len(visited_roads) and len(intersections) == len(visited_intersections):
        return True
    else:
        return False


def check_overload_intersection(intersection):
    # road_angle_pairs = list()  # List of of angles where the roads edges intersect the intersection
    #
    # for road in intersection.get_connections():
    #     width = (road.get_out_lanes() + road.get_in_lanes()) * LANE_WIDTH
    #     if road.get_start_connection() is intersection:
    #         angle = road.get_angle()
    #         angle_to_edge = math.
    #     elif road.get_end_connection() is intersection:
    #         angle = add_angles(road.get_angle(), math.pi)
    #     else:
    #         raise XMLFormatError("Intersection has a road connected but not vice versa")
    return


def remove_visited_roads(roads, visited_roads):
    """
    Removes all the previous visted roads from the new roads list
    :param roads: list of new roads to be filtered
    :param visited_roads: list of roads that have already been visited
    :return: removes duplicates between visted roads and roads
    """
    return [road for road in roads if road not in visited_roads]


def add_angles(angle1, angle2):
    """
    Adds to angles and keeps them in the range 0 < x < 2*PI
    :param angle1: double angle in radians
    :param angle2: double angle in radians
    :return: angle result of the addition
    """
    return_angle = angle1 + angle2
    return return_angle % (2 * math.pi)


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
    return round(dist, SIG_FIGS)
