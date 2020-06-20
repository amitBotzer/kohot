class Playground:

    def __init__(self, name, address, location, opening_hours):
        """

        :param name: of the playground. Usually the street or neighborhood in which the playground is located.
        :param location: the coordinates of the playground, given as a tuple of latitude and longitude.
        :param opening_hours: the hours when people can play in this playground, given as a list of tuples where each
        tuple stats a time range such as: (1400, 2200).
        """
        self._name = name
        self._address = address
        self._location = location
        self._opening_hours = opening_hours

    def is_open_at(self, desired_time):
        """
        :param desired_time: a desired time given as a string such as '1830'.
        :return: whether this playground is open in the desired time.
        """
        for time_range in self._opening_hours:
            if time_range[0] < desired_time < time_range[1]:
                return True
        return False