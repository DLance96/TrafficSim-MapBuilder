from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def get_opposite(self):
        return {
            '0': Direction.SOUTH,
            '1': Direction.WEST,
            '2': Direction.NORTH,
            '3': Direction.EAST,
        }[self.value]
