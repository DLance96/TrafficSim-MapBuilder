from src.map.nodes import Node
from src.map.paths import Path


class DirectionUnavailableException(Exception):

    def __init__(self, obj, direction):
        """
        A error for whenever a node or path tries to access a direction that isn't setup for the given map piece
        :param obj: a map piece
        :param direction: the direction that was attempted to view
        """
        if type(obj) in (Node, Path):
            Exception.__init__(self, "{0} is not a valid direction for this {1}".format(direction, type(obj)))
        else:
            raise NotImplementedError()


class NotInitializedSetException(Exception):

    def __init__(self, obj, direction):
        """
        An error for accessing map pieces that have not been initialized
        :param obj: a map piece
        :param direction: the direction that was attempted to view
        """
        if type(obj) is Node:
            Exception.__init__(self, "No path {0} of this node".format(direction))
        elif type(obj) is Path:
            Exception.__init__(self, "No node {0} of this path".format(direction))
        else:
            raise NotImplementedError()