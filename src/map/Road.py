import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Coordinates import Coordinates
from src.map.Constants import LANE_WIDTH
import src.map as traffic_map


class Road(object):
    """
    This class represents a road object in the MapBuilder section of our application

    """

    def __init__(self, start_coord, end_coord, length, out_lanes, in_lanes, angle, speed_limit, name):
        """
        Establishes a road object

        :param start_coord: starting coordinates of the median of the road
        :param end_coord: end coordinates of the median of the road
        :param length: length of the road
        :param out_lanes: number of outgoing lanes of the road
        :param in_lanes: number of incoming lanes of the road
        :param angle: angle at which the road projects from the center of its connected intersection (in radians)
        :param name: name of the road

        :type start_coord: Coordinates
        :type end_coord: Coordinates
        :type length: float
        :type out_lanes: int
        :type in_lanes: int
        :type angle: float
        :type name: str
        """
        self.start_coord = start_coord
        self.end_coord = end_coord
        self.length = length
        self.out_lanes = out_lanes
        self.in_lanes = in_lanes
        self.angle = angle
        self.speed_limit = speed_limit
        self.start_connection = None
        self.end_connection = None
        self.name = name


    @classmethod
    def create_import_road(cls, length, out_lanes, in_lanes, angle):
        obj = cls(Coordinates(0, 0), Coordinates(0, 0), length, out_lanes, in_lanes, angle)
        return obj

    def get_speed_limit(self):
        """
        :return: speed limit of the road
        """
        return self.speed_limit

    def update_speed_limit(self, new_speed):
        """
        Updates the speed limit of the road
        :param new_speed: new speed limit
        :type new_speed: int
        :return: None
        """
        self.speed_limit = new_speed

    def get_name(self):
        """
        :return: name of the road
        """
        return self.name

    def update_name(self, new_name):
        """
        Updates the name of the road
        :param new_name: new name
        :type new_name: str
        :return: None
        """
        self.name = new_name

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
        :return: angle from which this road projects from the center of its connected intersection (in radians)
        """
        return self.angle

    def get_compatible_angle(self):
        """
        :return: angle from which this road projects from the center of its connected intersection (in radians)
        """
        return ((5*math.pi/2) - self.angle) % (2 * math.pi)

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

    def is_on_road(self, coordinate):
        """
        Determines if a given coordinate point is within the boundaries of the current road
        :param coordinate: coordinate point that will be tested for being within road boundaries
        :type coordinate: Coordinates
        :return: returns true if given coordinate is within the boundaries of the road. Otherwise, returns false
        """
        point_list = self.get_points()

        # left of the starting point
        p_1 = point_list[0]

        # right of the starting point
        p_2 = point_list[1]

        # right of the ending point
        p_3 = point_list[3]

        # left of the ending point
        p_4 = point_list[2]

        cx = coordinate.get_x()
        cy = coordinate.get_y()

        p1x = p_1.get_x()
        p1y = p_1.get_y()
        p2x = p_2.get_x()
        p2y = p_2.get_y()
        p3x = p_3.get_x()
        p3y = p_3.get_y()
        p4x = p_4.get_x()
        p4y = p_4.get_y()

        # this chunk of code determines the area of the rectangle
        width_delta_x = p_2.get_x() - p_1.get_x()
        width_delta_y = p_2.get_y() - p_1.get_y()
        length_delta_x = p_4.get_x() - p_1.get_x()
        length_delta_y = p_4.get_y() - p_1.get_y()

        rect_width = math.sqrt((width_delta_x * width_delta_x) + (width_delta_y * width_delta_y))
        rect_length = math.sqrt((length_delta_x * length_delta_x) + (length_delta_y * length_delta_y))

        # area of the rectangle (road)
        rect_area = rect_width * rect_length

        # this next chunk of code determines the lengths of triangles created between rect sides and the coord point
        # for reference, point 1 = A, point 2 = B, point 3 = C, and point 4 = D
        ab_delta_x = p2x - p1x
        ab_delta_y = p2y - p1y

        cd_delta_x = p4x - p3x
        cd_delta_y = p4y - p3y

        ac_delta_x = p3x - p1x
        ac_delta_y = p3y - p1y

        bd_delta_x = p4x - p2x
        bd_delta_y = p4y - p2y

        lab = math.sqrt((ab_delta_x * ab_delta_x) + (ab_delta_y * ab_delta_y))
        lcd = math.sqrt((cd_delta_x * cd_delta_x) + (cd_delta_y * cd_delta_y))
        lac = math.sqrt((ac_delta_x * ac_delta_x) + (ac_delta_y * ac_delta_y))
        lbd = math.sqrt((bd_delta_x * bd_delta_x) + (bd_delta_y * bd_delta_y))

        pa_delta_x = cx - p1x
        pa_delta_y = cy - p1y

        pb_delta_x = cx - p2x
        pb_delta_y = cy - p2y

        pc_delta_x = cx - p3x
        pc_delta_y = cy - p3y

        pd_delta_x = cx - p4x
        pd_delta_y = cy - p4y

        lpa = math.sqrt((pa_delta_x * pa_delta_x) + (pa_delta_y * pa_delta_y))
        lpb = math.sqrt((pb_delta_x * pb_delta_x) + (pb_delta_y * pb_delta_y))
        lpc = math.sqrt((pc_delta_x * pc_delta_x) + (pc_delta_y * pc_delta_y))
        lpd = math.sqrt((pd_delta_x * pd_delta_x) + (pd_delta_y * pd_delta_y))

        # this chunk of code determines the sum of the area of the triangles generated above
        pab_half_perim = (lpa + lab + lpb) / 2.0
        pbd_half_perim = (lbd + lpb + lpd) / 2.0
        pcd_half_perim = (lcd + lpc + lpd) / 2.0
        pac_half_perim = (lac + lpa + lpc) / 2.0

        sqrt_inner_pab = pab_half_perim * (pab_half_perim - lpa) * (pab_half_perim - lab) * (pab_half_perim - lpb)
        sqrt_inner_pbd = pbd_half_perim * (pbd_half_perim - lbd) * (pbd_half_perim - lpb) * (pbd_half_perim - lpd)
        sqrt_inner_pcd = pcd_half_perim * (pcd_half_perim - lcd) * (pcd_half_perim - lpc) * (pcd_half_perim - lpd)
        sqrt_inner_pac = pac_half_perim * (pac_half_perim - lac) * (pac_half_perim - lpa) * (pac_half_perim - lpc)

        area_pab = math.sqrt(sqrt_inner_pab)
        area_pbd = math.sqrt(sqrt_inner_pbd)
        area_pcd = math.sqrt(sqrt_inner_pcd)
        area_pac = math.sqrt(sqrt_inner_pac)

        # the sum of all calculated triangles
        tot_triangle_sum = area_pab + area_pbd + area_pcd + area_pac

        if tot_triangle_sum <= rect_area:
            return True
        else:
            return False

    def add_start_connection(self, start_connection):
        """
        Adds a connecting object to the start of the road
        :param start_connection: object to be connected to the start of the road
        :type start_connection: Intersection
        :return: None
        """
        self.start_connection = start_connection

    def generate_start_connection(self, length, speed_limit):
        """
        Adds a connecting object to the start of the road
        :param length: length of intersection connection to be created
        :return: new Intersection map object
        """
        corrected_angle = self.angle + math.pi

        start_x = self.start_coord.x + (length * math.sin(corrected_angle))
        start_y = self.start_coord.y + (length * math.cos(corrected_angle))

        central_point = Coordinates(start_x, start_y)

        intersection = traffic_map.Intersection.Intersection(central_point, length, speed_limit)

        intersection.add_incoming_connection(self)
        self.start_connection = intersection

        return intersection

    def generate_end_connection(self, length, speed_limit):
        """
        Adds a connecting object to the start of the road
        :param length: length of intersection connection to be created
        :return: new Intersection map object
        """
        start_x = self.end_coord.x + (length * math.sin(self.angle))
        start_y = self.end_coord.y + (length * math.cos(self.angle))

        central_point = Coordinates(start_x, start_y)

        intersection = traffic_map.Intersection.Intersection(central_point, length, speed_limit)

        intersection.add_incoming_connection(self)
        self.end_connection = intersection

        return intersection

    def add_end_connection(self, end_connection):
        """
        Adds a connecting object to the end of the road
        :param end_connection: object to be connected to the end of the road
        :type end_connection: Intersection
        :return: None
        """
        self.end_connection = end_connection
        # self.end_connection.add_incoming_connection(self)

    def get_start_connection(self):
        """
        :return: connecting object at the start of the road
        """
        return self.start_connection

    def get_end_connection(self):
        """
        :return: connecting object at the end of the road
        """
        return self.end_connection

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

        left_radius = self.in_lanes * LANE_WIDTH
        right_radius = self.out_lanes * LANE_WIDTH

        right_angle = self.angle + (math.pi/2.0)
        left_angle = self.angle - (math.pi/2.0)

        x_left_of_start = start_x + (left_radius * math.sin(left_angle))
        y_left_of_start = start_y + (left_radius * math.cos(left_angle))

        x_right_of_start = start_x + (right_radius * math.sin(right_angle))
        y_right_of_start = start_y + (right_radius * math.cos(right_angle))

        x_left_of_end = end_x + (left_radius * math.sin(left_angle))
        y_left_of_end = end_y + (left_radius * math.cos(left_angle))

        x_right_of_end = end_x + (right_radius * math.sin(right_angle))
        y_right_of_end = end_y + (right_radius * math.cos(right_angle))

        points.append(Coordinates(x_left_of_start, y_left_of_start))
        points.append(Coordinates(x_right_of_start, y_right_of_start))
        points.append(Coordinates(x_right_of_end, y_right_of_end))
        points.append(Coordinates(x_left_of_end, y_left_of_end))

        return points