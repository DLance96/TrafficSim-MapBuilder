class coordinates:
    """
    This class represents a two-dimensional coordinate point in the MapBuilder section of our application.
    The user interface / graphics side of the MapBuilder will have a two-dimensional "grid" that shows where roads
    and intersections are placed, as well as where obstructions are placed, cars are placed, etc. This class stores
    information regarding the placement of objects in said scene.

    """

    def __init__(self, x_val, y_val):
        """
        Establishes a coordinate point
        :param x_val: x value for the coordinate point
        :param y_val: y value for the coordinate point

        :type x_val: float
        :type y_val: float
        """
        self.x = x_val
        self.y = y_val

    def get_x(self):
        """
        :return: x value of the current coordinate point
        """
        return self.x

    def get_y(self):
        """
        :return: y value of the current coordinate point
        """
        return self.y


def main():
    """
    Main method for the coordinates class
    :return: for now, prints information regarding points instantiated within the method
    """
    coord = coordinates(2.1, 3.3)
    print('x: ' + str(coord.get_x()))
    print('y: ' + str(coord.get_y()))


if __name__ == '__main__':
    main()
