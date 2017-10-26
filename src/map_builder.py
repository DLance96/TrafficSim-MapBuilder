import sys
import road, intersection, coordinates, math

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtGui, QtCore


class MapBuilder(QMainWindow):
    start_coord_to_obj = {}
    roads = []
    intersections = []
    selected_object = None
    add_to_start_action = None
    add_to_end_action = None

    def __init__(self):
        super().__init__()
        self.title = 'Map Builder'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.initUI()
        self.roads = []
        self.intersections = []
        self.x = 100

    def initUI(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        selected_menu = menu_bar.addMenu("MapObject")

        # buttons
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 440)
        button.clicked.connect(self.add_road)

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)

        self.add_to_start_action = QAction("Add to Start", self)
        self.add_to_end_action = QAction("Add to End", self)
        edit_action = QAction("Edit", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        selected_menu.addAction(self.add_to_start_action)
        selected_menu.addAction(self.add_to_end_action)
        selected_menu.addAction(edit_action)

        self.add_to_start_action.triggered.connect(self.adds_road)

        screen = app.primaryScreen()
        self.resize(screen.size().width(), screen.size().height())
        self.setWindowTitle("Traffic Simulator - Map Builder")
        self.setFixedSize(self.size())

        self.show()

    def draw_road(self, points, qp):
        polygon = QtGui.QPolygonF()
        for point in points:
            polygon.append(QtCore.QPoint(point.x, point.y))
        qp.drawPolygon(polygon)

    def draw_intersection(self, center, radius, qp):
        qp.drawEllipse(center.x, center.y, radius, radius)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        for obj in self.roads:
            self.draw_road(obj.get_points(), qp)
        for obj in self.intersections:
            self.draw_intersection(obj.center, obj.radius, qp)
        if self.selected_object is not None:
            qp.setBrush(Qt.yellow)
            if type(self.selected_object) is road.road:
                self.draw_road(self.selected_object.get_points(), qp)
            if type(self.selected_object) is intersection.intersection:
                self.draw_intersection(self.selected_object.center, self.selected_object.radius, qp)
        qp.end()

    # change to first intersection!!!
    def first_road(self):
        leng = 100
        start_coord = coordinates.coordinates(100 - (leng / 2), 140)
        end_coord = coordinates.coordinates(start_coord.x + leng, start_coord.y)
        r = road.road(start_coord, end_coord, leng, 2, 2, 90)
        self.roads.append(r)
        self.start_coord_to_obj.update({str(50) + ' ' + str(140): r})

        center = coordinates.coordinates(start_coord.x, start_coord.y + 100)
        i = intersection.intersection(center, 20)
        self.intersections.append(i)
        self.update()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        converted_position = coordinates.coordinates(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        for obj in self.roads:
            if obj.is_on_road(converted_position):
                self.selected_object = obj
        for obj in self.intersections:
            if obj.is_on_intersection(converted_position):
                self.selected_object = obj
        if self.selected_object is not None:
            if type(self.selected_object) is road.road:
                # check if start/end connection is present
                self.add_to_end_action.setEnabled(False)
        self.update()

    @pyqtSlot()
    def add_road(self):
        prevr = self.roads[self.roads.__len__()-1]
        leng = 100

        start_coord = prevr.get_end_coords()
        end_coord = coordinates.coordinates(start_coord.x + leng, start_coord.y)

        r = road.road(start_coord, end_coord, leng, 1, 1, 90)

        self.roads.append(r)
        self.start_coord_to_obj.update({str(start_coord.x) + ' ' + str(start_coord.y): r})

        self.x = self.x + 20
        self.update()

    def adds_road(self):
        prevr = self.selected_object
        if prevr is None:
            return
        if type(prevr) is intersection.intersection:

            le = 100
            angle = 90
            in_lanes = 2
            out_lanes = 2

            r = prevr.add_connection(angle, le, in_lanes, out_lanes)
            print(str(r.start_coord.x) + ", " + str(r.start_coord.y) + '\n')
            self.roads.append(r)

        if type(prevr) is road.road:

            leng = 100

            start_coord = prevr.get_end_coords()
            end_coord = coordinates.coordinates(start_coord.x + leng, start_coord.y)

            r = road.road(start_coord, end_coord, leng, 1, 1, 90)

            self.roads.append(r)
            self.start_coord_to_obj.update({str(start_coord.x) + ' ' + str(start_coord.y): r})

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    mb.first_road()
    sys.exit(app.exec_())
