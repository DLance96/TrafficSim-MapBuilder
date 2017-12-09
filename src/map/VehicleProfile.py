class VehicleProfile:

    """
    This class represents a Vehicle Profile in the Map Builder portion of our system. A user will be able to create a
    Vehicle Profile with custom values which can then be used to spawn cars in the simulation with said Vehicle Profile.
    Essentially, it represents the characteristics of the vehicle spawned.
    """

    def __init__(self, profile_name, width, length, max_accel, max_braking_decel, mass, max_speed):

        """
        Establishes a Vehicle Profile object

        :param profile_name: Name of Vehicle Profile
        :param width: width of the car
        :param length: length of the car
        :param max_accel: maximum acceleration of the car
        :param max_braking_decel: maximum braking deceleration of the car
        :param mass: mass of the car
        :param max_speed: maximum speed of the car
        """
        self.profile_name = profile_name
        self.width = width
        self.length = length
        self.max_accel = max_accel
        self.max_braking_decel = max_braking_decel
        self.mass = mass
        self.max_speed = max_speed

    def get_vehicle_profile_name(self):
        """
        :return: Name of the vehicle profile
        """
        return self.profile_name

    def get_width(self):
        """
        :return: width of the vehicle
        """
        return self.width

    def get_length(self):
        """
        :return: length of the vehicle
        """
        return self.length

    def get_max_accel(self):
        """
        :return: maximum acceleration of the vehicle
        """
        return self.max_accel

    def get_max_braking_decel(self):
        """
        :return: maximum braking deceleration of the vehicle
        """
        return self.max_braking_decel

    def get_mass(self):
        """
        :return: mass of the vehicle
        """
        return self.mass

    def get_max_speed(self):
        """
        :return: maximum speed of the vehicle
        """
        return self.max_speed

    def update_width(self, new_width):
        """
        Updates the width of the vehicle. Should only be called prior to the simulation running.
        :param new_width: the new width of the vehicle
        :return: None
        """
        self.width = new_width

    def update_length(self, new_length):
        """
        Updates the length of the vehicle. Should only be called prior to the simulation running.
        :param new_length: the new length of the vehicle
        :return: None
        """
        self.length = new_length

    def update_max_accel(self, new_max_accel):
        """
        Updates the maximum acceleration of the vehicle. Should only be called prior to the simulation running.
        :param new_max_accel: the new maximum acceleration of the vehicle
        :return: None
        """
        self.max_accel = new_max_accel

    def update_max_braking_decel(self, new_max_braking_decel):
        """
        Updates the maximum braking deceleration of the vehicle. Should only be called prior to the simulation running.
        :param new_max_braking_decel: the new maximum braking deceleration of the vehicle.
        :return: None
        """
        self.max_braking_decel = new_max_braking_decel

    def update_mass(self, new_mass):
        """
        Updates the mass of the vehicle. Should only be called prior to the simulation running.
        :param new_mass: the new mass of the vehicle
        :return: None
        """
        self.mass = new_mass

    def update_max_speed(self, new_max_speed):
        """
        Updates the maximum speed of the vehicle. Should only be called prior to the simulation running.
        :param new_max_speed: the new maximum speed of the vehicle
        :return: None
        """
        self.max_speed = new_max_speed

    def update_profile_name(self, new_name):
        """
        Updates the name of the vehicle profile. Should only be called prior to the simulation running.
        :param new_name: The new name of the profile
        :return: None
        """
        self.profile_name = new_name
