class DriverProfile:

    """
    This class represents a Driver Profile in the Map Builder portion of our system. A user will be able to create a
    Driver Profile with custom values which can then be used to spawn cars in the simulation with said Driver Profile.
    Essentially, it represents the characteristics of the driver behind the wheel.
    """

    def __init__(self, over_braking_factor, following_time, max_accel, min_accel, max_speed, accel_time, update_time_ms):

        """
        Establishes a Driver Profile object

        :param over_braking_factor: factor by which the driver will over-brake
        :param following_time: the distance that the driver is comfortable driving behind the next closest car
        :param max_accel: the max acceleration that a driver is comfortable with
        :param min_accel: the minimum acceleration that a driver will use while driving
        :param max_speed: the max speed that the driver is comfortable with
        :param accel_time: time driver wishes to take to approach desired speed
        :param update_time_ms: interval at which driver checks their surroundings
        """
        self.over_braking_factor = over_braking_factor
        self.following_time = following_time
        self.max_accel = max_accel
        self.min_accel = min_accel
        self.max_speed = max_speed
        self.accel_time = accel_time
        self.update_time_ms = update_time_ms

    def get_over_braking_factor(self):
        """
        :return: the over-braking factor of the driver
        """
        return self.over_braking_factor

    def get_following_time(self):
        """
        :return: the following time of the driver
        """
        return self.following_time

    def get_max_accel(self):
        """
        :return: the max acceleration of the driver
        """
        return self.max_accel

    def get_min_accel(self):
        """
        :return: the minimum acceleration of the driver
        """
        return self.min_accel

    def get_max_speed(self):
        """
        :return: the maximum speed of the driver
        """
        return self.max_speed

    def get_accel_time(self):
        """
        :return: the acceleration time of the driver
        """
        return self.accel_time

    def get_update_time_ms(self):
        """
        :return: the interval at which a driver checks its surroundings
        """
        return self.update_time_ms

    def update_over_breaking_factor(self, new_brake_factor):
        """
        Update the over braking factor of the driver
        :param new_brake_factor: new braking factor of the driver
        :return: None
        """
        self.over_braking_factor = new_brake_factor

    def update_following_time(self, new_following_time):
        """
        Update the following time of the driver
        :param new_following_time: new following time of the driver
        :return: None
        """
        self.following_time = new_following_time

    def update_max_accel(self, new_max_accel):
        """
        Update the max acceleration of the driver
        :param new_max_accel: new max acceleration of the driver
        :return: None
        """
        self.max_accel = new_max_accel

    def update_min_accel(self, new_min_accel):
        """
        Update the minimum acceleration of the driver
        :param new_min_accel: new minimum acceleration of the driver
        :return: None
        """
        self.min_accel = new_min_accel

    def update_max_speed(self, new_max_speed):
        """
        Update the max speed of the driver
        :param new_max_speed: new max speed of the driver
        :return: None
        """
        self.max_speed = new_max_speed

    def update_accel_time(self, new_accel_time):
        """
        Update the acceleration time of the driver
        :param new_accel_time: new acceleration time of the driver
        :return: None
        """
        self.accel_time = new_accel_time

    def update_update_time_ms(self, new_update_time_ms):
        """
        Update the interval at which a driver checks its surroundings
        :param new_update_time_ms: new interval at which a driver checks its surroundings
        :return: None
        """
        self.update_time_ms = new_update_time_ms


def main():
    """
    Main method for the coordinates class
    :return: for now, prints information regarding points instantiated within the method
    """
    print('Hello World! Driver Profile')


if __name__ == '__main__':
    main()
