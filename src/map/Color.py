class Color:

    """
    This class represents a color composed of RGB components. This will be used by the user of the Map Builder to determine
    the color of vehicles in a vehicle template.
    """

    def __init__(self, r, g, b):

        """
        Establishes a RGB color
        :param r: Red component
        :param g: Green component
        :param b: Blue component

        :type r: int
        :type g: int
        :type b: int

        """

        self.r = r
        self.g = g
        self.b = b

    def get_r(self):
        """
        :return: red component of the inputted RGB color.
        """
        return self.r

    def get_g(self):
        """
        :return: green component of the inputted RGB color.
        """
        return self.g

    def get_b(self):
        """
        :return: blue component of the inputted RGB color.
        """
        return self.b

    def update_r(self, new_r):
        """
        Updates the red component of the current RGB color
        :param new_r: new value of red RGB component
        :type new_r: int
        :return: None
        """
        self.r = new_r

    def update_g(self, new_g):
        """
        Updates the green component of the current RGB color
        :param new_g: new value of green RGB component
        :type new_g: int
        :return: None
        """
        self.g = new_g

    def update_b(self, new_b):
        """
        Updates the blue component of the current RGB color
        :param new_b: new value of blue RGB component
        :type new_b: int
        :return: None
        """
        self.b = new_b
