import coordinates
import math
import road


class intersection(object):
    """
    This class represents an intersection object in the MapBuilder section of our application.
    An intersection is represented in our implementation by a circle, where roads
    can connect to it at any point along its circumference.

    """

    def __init__(self, central_point, radius):
        """
        Establishes an intersection object

        :param central_point: center point of the intersection circle
        :param radius: radius of the intersection circle

        :type central_point: coordinates.coordinates
        :type radius: float
        """
        self.center = central_point
        self.radius = radius
        self.connections = []

    # need to create another constructor to handle a central point and its connecting object (CHECK IF THAT IS TRUE)

    def add_connection(self, angle, distance, in_lanes, out_lanes):
        """
        Currently adds a road to the intersection
        :param angle: angle that the road protrudes from the intersection relative to the intersection's origin
        :param distance: length of the road
        :param in_lanes: number of incoming lanes that the road contains
        :param out_lanes: number of outgoing lanes that the road contains

        :type angle: float
        :type distance: float
        :type in_lanes: int
        :type out_lanes: int

        :return: returns road object for added connection
        """

        angle_rads = angle * (math.pi/180.0)
        start_x = self.center.get_x() + (self.radius * math.cos(angle_rads))
        start_y = self.center.get_y() + (self.radius * math.sin(angle_rads))

        start_coord = coordinates.coordinates(start_x, start_y)

        end_x = self.center.get_x() + ((self.radius + distance) * math.cos(angle_rads))
        end_y = self.center.get_y() + ((self.radius + distance) * math.sin(angle_rads))

        end_coord = coordinates.coordinates(end_x, end_y)

        r = road.road(start_coord, end_coord, distance, out_lanes, in_lanes, angle)

        self.connections.append(r)

        return r

    def get_center(self):
        """
        :return: center point of the intersection circle
        """
        return self.center

    def get_radius(self):
        """
        :return: radius of the intersection circle
        """
        return self.radius

    def get_connections(self):
        """
        :return: list of map objects that are connected to this intersection
        """
        return self.connections

    def update_center(self, new_center):
        """
        Updates the center point of the intersection circle

        :param new_center: new center point of the intersection circle
        :type new_center: coordinates.coordinates

        :return: None
        """
        self.center = new_center

    def update_radius(self, new_radius):
        """
        Updates the radius of the intersection circle

        :param new_radius: new radius of the intersection circle
        :type new_radius: float

        :return: None
        """
        self.radius = new_radius

    def update_connections(self, new_connections):
        """
        Updates the list of connections for the intersection

        :param new_connections: new list of connections for the intersection
        :type new_connections: list consisting of map objects

        :return: None
        """
        self.connections = new_connections

    def is_on_intersection(self, coordinate):
        """
        Determines if a given coordinate point is within the boundaries of the current intersection
        :param coordinate: coordinate point that will be tested for being within intersection boundaries
        :type coordinate: coordinates.coordinates
        :return: returns true if given coordinate is within the boundaries of the intersection. Otherwise, returns false
        """
        delta_x = self.center.get_x() - coordinate.x
        delta_y = self.center.get_y() - coordinate.y

        x_squared = delta_x * delta_x
        y_squared = delta_y * delta_y

        distance = math.sqrt(x_squared + y_squared)

        if self.radius >= distance:
            return True
        return False


def main():
    center = coordinates.coordinates(1,1)
    radius = 4
    i = intersection(center, radius)

    i.add_connection(25.0, 6, 3, 2)
    print('main method goes here')


if __name__ == '__main__':
    main()
