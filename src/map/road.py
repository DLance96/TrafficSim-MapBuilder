<<<<<<< Updated upstream
import sys
import os
=======
from src.map.coordinates import Coordinates
from src.map.constants import LANE_WIDTH
>>>>>>> Stashed changes
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.coordinates import Coordinates


class Road(object):
    """
    This class represents a road object in the MapBuilder section of our application

    """

    def __init__(self, start_coord, end_coord, length, out_lanes, in_lanes, angle):
        """
        Establishes a road object

        :param start_coord: starting coordinates of the median of the road
        :param end_coord: end coordinates of the median of the road
        :param length: length of the road
        :param out_lanes: number of outgoing lanes of the road
        :param in_lanes: number of incoming lanes of the road
        :param angle: angle at which the road projects from the center of its connected intersection (in radians)

        :type start_coord: Coordinates
        :type end_coord: Coordinates
        :type length: float
        :type out_lanes: int
        :type in_lanes: int
        :type angle: float
        """
        self.start_coord = start_coord
        self.end_coord = end_coord
        self.length = length
        self.out_lanes = out_lanes
        self.in_lanes = in_lanes
        self.angle = angle * (math.pi / 180.0)

    def get_start_coords(self):
        """
        :return: starting coordinates of the road
        """
        return self.start_coord

    def get_length(self):
        """
        :return: length of the road
        """
        return self.length

    def get_end_coords(self):
        """
        :return: end coordinates of the road
        """
        return self.end_coord

    def get_out_lanes(self):
        """
        :return: number of outgoing lanes of the road
        """
        return self.out_lanes

    def get_in_lanes(self):
        """
        :return: number of incoming lanes of the road
        """
        return self.in_lanes

    def get_angle(self):
        """
        :return: angle from which this road projects from the center of its connected intersection (in degrees)
        """
        return self.angle * (180.0 / math.pi)

    def update_start_coords(self, new_start_coord):
        """
        Updates the start coordinates of the road
        :param new_start_coord: new start coordinates of the road
        :type new_start_coord: Coordinates
        :return: None
        """
        self.start_coord = new_start_coord

    def update_end_coords(self, new_end_coord):
        """
        Updates the end coordinates of the road
        :param new_end_coord: new end coordinates of the road
        :type new_end_coord: Coordinates
        :return: None
        """
        self.end_coord = new_end_coord

    def update_length(self, new_length):
        """
        Updates the length of the road
        :param new_length: new length of the road
        :type new_length: float
        :return: None
        """
        self.length = new_length

    def update_out_lanes(self, new_out_lanes):
        """
        Updates the number of outgoing lanes of the road
        :param new_out_lanes: new number of outgoing lanes
        :type new_out_lanes: int
        :return: None
        """
        self.out_lanes = new_out_lanes

    def update_in_lanes(self, new_in_lanes):
        """
        Updates the number of incoming lanes of the road
        :param new_in_lanes:  new number of incoming lanes
        :type new_in_lanes: int
        :return: None
        """
        self.in_lanes = new_in_lanes

    def update_angle(self, new_angle):
        """
        Updates the angle from which the road projects from the center of the intersection.
        :param new_angle: new angle of the road
        :type new_angle: float
        :return: None
        """
        self.angle = new_angle * (math.pi / 180.0)

    def is_on_road(self, coordinate):
        """
        Determines if a given coordinate point is within the boundaries of the current road
        :param coordinate: coordinate point that will be tested for being within road boundaries
        :type coordinate: Coordinates
        :return: returns true if given coordinate is within the boundaries of the road. Otherwise, returns false
        """
        if (coordinate.x > self.start_coord.x) & (coordinate.x < self.end_coord.x):
            if coordinate.y > (self.start_coord.get_y() - (self.in_lanes * LANE_WIDTH)):
                if coordinate.y < (self.start_coord.get_y() + (self.out_lanes * LANE_WIDTH)):
                    return True
        return False

    # ------------------------------------------------------------------------------------------

    # This should be implemented to include previous and next neighbors
    def add_neighboring_road(self, neighbor_road):
        self.neighboring_road = neighbor_road

    # This should be implemented to include previous and next neighbors
    def add_neighboring_intersection(self, intersection):
        self.neighboring_intersection = intersection

    # Returns the neighboring road.
    def get_neighboring_road(self):
        return self.neighboring_road

    # Returns the neighboring intersection.
    def get_neighboring_intersection(self):
        return self.neighboring_intersection

    # --------------SHOULD THE PREVIOUS FOUR METHODS EVEN BE IN THIS CODE???---------------------

    def get_points(self):
        """
        Retrieves the four corner points of the road
        :return: a list of all corner points of the road
        """
        points = []
        start_x = self.start_coord.get_x()
        start_y = self.start_coord.get_y()
        end_x = self.end_coord.get_x()
        end_y = self.end_coord.get_y()

        left_rad = self.in_lanes
        right_rad = self.out_lanes

        right_angle = (math.pi/2) - self.angle
        left_angle = (math.pi/2) + self.angle

        x_left_of_start = start_x + (left_rad * math.cos(left_angle))
        y_left_of_start = start_y + (left_rad * math.sin(left_angle))

        x_right_of_start = start_x + (right_rad * math.cos(right_angle))
        y_right_of_start = start_y + (right_rad * math.sin(right_angle))

        x_left_of_end = end_x + (left_rad * math.cos(left_angle))
        y_left_of_end = end_y + (left_rad * math.sin(left_angle))

        x_right_of_end = end_x + (right_rad * math.cos(right_angle))
        y_right_of_end = end_y + (right_rad * math.sin(right_angle))

        points.append(Coordinates(x_left_of_start, y_left_of_start))
        points.append(Coordinates(x_right_of_start, y_right_of_start))
        points.append(Coordinates(x_left_of_end, y_left_of_end))
        points.append(Coordinates(x_right_of_end, y_right_of_end))

        return points


def main():
    """
    Main method for the road class
    :return: Prints attribute values for the current road
    """
    start_coord = Coordinates(3, 1)
    end_coord = Coordinates(4, 8)
    out_lanes = 4
    in_lanes = 3
    length = 2
    angle = 45.0

    r = Road(start_coord, end_coord, length, out_lanes, in_lanes, angle)
    r2 = Road(start_coord, end_coord, 12, 23, 54, 90.0)

    r.add_neighboring_road(r2)

    road_coord = r.get_start_coords()
    end_road_coord = r.get_end_coords()

    start_x = road_coord.get_x()
    start_y = road_coord.get_y()
    end_x = end_road_coord.get_x()
    end_y = end_road_coord.get_y()

    print('start coords: (' + str(start_x) + ', ' + str(start_y) + ')')
    print('out lanes: ' + str(r.get_out_lanes()))
    print('in lanes: ' + str(r.get_in_lanes()))
    print('length: ' + str(r.get_length()))
    print('end coords: (' + str(end_x) + ', ' + str(end_y) + ')')
    print(' ')

    new_coord = Coordinates(7, 4)
    new_end_coord = Coordinates(17, 9)

    r.update_start_coords(new_coord)
    r.update_end_coords(new_end_coord)
    r.update_length(10)
    r.update_out_lanes(96)
    r.update_in_lanes(12)

    new_road_coord = r.get_start_coords()
    new_road_end_coord = r.get_end_coords()
    new_x = new_road_coord.get_x()
    new_y = new_road_coord.get_y()
    new_end_x = new_road_end_coord.get_x()
    new_end_y = new_road_end_coord.get_y()

    print('new coords: (' + str(new_x) + ', ' + str(new_y) + ')')
    print('out lanes: ' + str(r.get_out_lanes()))
    print('in lanes: ' + str(r.get_in_lanes()))
    print('length: ' + str(r.get_length()))
    print('end coords: (' + str(new_end_x) + ', ' + str(new_end_y) + ')')
    print(' ')

    print('angle of road in radians: ' + str(r.angle))
    print('angle of road in degrees: ' + str(r.get_angle()))
    print(' ')

    r.update_angle(87.5)

    print('updated angle of road in radians: ' + str(r.angle))
    print('updated angle of road in degrees: ' + str(r.get_angle()))
    print(' ')

    p_start_coord = Coordinates(1, 1)
    p_end_coord = Coordinates(1, 5)
    p_length = 4
    p_out_lanes = 2
    p_in_lanes = 3
    p_angle = 90.0

    p = Road(p_start_coord, p_end_coord, p_length, p_out_lanes, p_in_lanes, p_angle)

    p_points = p.get_points()

    for point in p_points:
        print('( ' + str(point.get_x()) + ', ' + str(point.get_y()) + ' )')


if __name__ == '__main__':
    main()
