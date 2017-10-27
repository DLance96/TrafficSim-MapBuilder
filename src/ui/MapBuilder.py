import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.Constants import LANE_WIDTH
import math

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtGui, QtCore


class MapBuilder(QMainWindow):
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

    def initUI(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        selected_menu = menu_bar.addMenu("MapObject")

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

        self.add_to_end_action.triggered.connect(self.add_road_to_end_coord)
        self.add_to_start_action.triggered.connect(self.add_road_to_start_coord)

        screen = app.primaryScreen()
        self.resize(screen.size().width(), screen.size().height())
        self.setWindowTitle("Traffic Simulator - Map Builder")
        self.setFixedSize(self.size())

        self.show()

    def draw_road(self, road, qp):

        polygon = QtGui.QPolygonF()

        for point in road.get_points():
            polygon.append(QtCore.QPoint(point.x, point.y))

        qp.drawPolygon(polygon)

        qp.setPen(Qt.lightGray)
        point_one = QtCore.QPoint(road.start_coord.x, road.start_coord.y)
        point_two = QtCore.QPoint(road.end_coord.x, road.end_coord.y)
        qp.drawLine(point_one, point_two)
        qp.setPen(Qt.black)

    def draw_intersection(self, center, radius, qp):
        qp.drawEllipse(center.x - radius, center.y - radius, radius * 2, radius * 2)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(Qt.darkGray)
        for obj in self.roads:
            self.draw_road(obj, qp)
        qp.setBrush(Qt.darkGray)
        for obj in self.intersections:
            self.draw_intersection(obj.center, obj.radius, qp)
        if self.selected_object is not None:
            qp.setBrush(Qt.yellow)
            if type(self.selected_object) is Road:
                self.draw_road(self.selected_object, qp)
            if type(self.selected_object) is Intersection:
                self.draw_intersection(self.selected_object.center, self.selected_object.radius, qp)
        qp.end()

    # change to first intersection!!!
    def first_road(self):
        start_coord = Coordinates(250, 250)

        center = Coordinates(start_coord.x, start_coord.y)
        i = Intersection(center, 40)
        self.intersections.append(i)
        self.update()

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        converted_position = Coordinates(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        for obj in self.roads:
            if obj.is_on_road(converted_position):
                self.selected_object = obj

        for obj in self.intersections:
            if obj.is_on_intersection(converted_position):
                self.selected_object = obj

        if self.selected_object is not None:
            if type(self.selected_object) is Road:
                # check if start/end connection is present
                if self.selected_object.start_connection is None:
                    self.add_to_start_action.setEnabled(True)
                else:
                    self.add_to_start_action.setEnabled(False)

                if self.selected_object.end_connection is None:
                    self.add_to_end_action.setEnabled(True)
                else:
                    self.add_to_end_action.setEnabled(False)
            else:
                self.add_to_start_action.setEnabled(True)
                self.add_to_end_action.setEnabled(True)

        self.update()

    def add_road_to_end_coord(self):
        prev_road = self.selected_object
        if prev_road is None:
            return

        if type(prev_road) is Intersection:
            length = 75
            angle = 90 * (math.pi/180)
            in_lanes = 1
            out_lanes = 1

            new_road = prev_road.add_connection(angle, length, out_lanes, in_lanes)
            self.roads.append(new_road)

        if type(prev_road) is Road:
            length = 40

            if prev_road.get_end_connection() is not None:
                return

            new_intersection = prev_road.generate_end_connection(length)

            self.add_to_end_action.setEnabled(False)

            self.intersections.append(new_intersection)

        self.update()

    def add_road_to_start_coord(self):
        prev_road = self.selected_object
        if prev_road is None:
            return

        if type(prev_road) is Intersection:
            length = 75
            angle = -90 * (math.pi/180)
            in_lanes = 1
            out_lanes = 1

            new_road = prev_road.add_connection(angle, length, out_lanes, in_lanes)
            self.roads.append(new_road)

        if type(prev_road) is Road:
            length = 40

            if prev_road.get_start_connection() is not None:
                return

            new_intersection = prev_road.generate_start_connection(length)

            self.add_to_start_action.setEnabled(False)

            self.intersections.append(new_intersection)

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    mb.first_road()
    sys.exit(app.exec_())
