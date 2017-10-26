import math
from src.xml.Constants import IMPORT_ROAD_TOLERANCE
from src.map.Constants import ROAD_OUT_ENTRANCE_PT_INDEX, ROAD_OUT_EXIT_PT_INDEX


def import_xml(filename):
    # TODO check if file exists
    return


def valid_roads(roads):
    """
    Checks that roads values are consistent
    :param roads: list of roads to check
    :return: boolean whether or not all the roads are consistent
    """
    for road in roads:
        matching_length = math.isclose(
            distance(road.get_points()[ROAD_OUT_ENTRANCE_PT_INDEX], road.get_points()[ROAD_OUT_EXIT_PT_INDEX]),
            road.get_length(), abs_tol=IMPORT_ROAD_TOLERANCE
        )
        x_diff = road.get_points()[ROAD_OUT_EXIT_PT_INDEX].get_x() - \
                 road.get_points()[ROAD_OUT_ENTRANCE_PT_INDEX].get_x()
        y_diff = road.get_points()[ROAD_OUT_EXIT_PT_INDEX].get_y() - \
                 road.get_points()[ROAD_OUT_ENTRANCE_PT_INDEX].get_y()
        matching_angle = math.isclose(math.atan(y_diff / x_diff), road.get_angle(), abs_tol=IMPORT_ROAD_TOLERANCE)
        if not matching_length or not matching_angle:
            return False
    return True


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
