# Class that stores coordinates of a point.
class coordinates:
    # Constructor for coordinates. Stores x and y coord values of a point.
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    # returns x coord value of a point.
    def get_x(self):
        return self.x

    # returns y coord value of a point.
    def get_y(self):
        return self.y


# main method for coordinates
def main():
    coord = coordinates(2.1, 3.3)
    print('x: ' + str(coord.get_x()))
    print('y: ' + str(coord.get_y()))


if __name__ == '__main__':
    main()
