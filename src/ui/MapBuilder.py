import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.Constants import LANE_WIDTH
import math

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, \
    QPushButton, QGridLayout, QComboBox, QDialog, QDialogButtonBox, \
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, \
    QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtGui, QtCore

selected_object = None

class MapBuilder(QMainWindow):
    roads = []
    intersections = []
    # selected_object = None
    add_to_start_action = None
    add_to_end_action = None
    edit_action = None
    selected_menu = None

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
        self.selected_menu = menu_bar.addMenu("MapObject")

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)

        self.add_to_start_action = QAction("Add to Start", self)
        self.add_to_end_action = QAction("Add to End", self)
        self.edit_action = QAction("Edit", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        self.selected_menu.addAction(self.add_to_start_action)
        self.selected_menu.addAction(self.add_to_end_action)
        self.selected_menu.addAction(self.edit_action)

        self.add_to_end_action.triggered.connect(self.add_road_to_end_coord)
        self.add_to_start_action.triggered.connect(self.add_road_to_start_coord)
        self.edit_action.triggered.connect(self.open_dialog)

        self.add_to_start_action.setEnabled(False)
        self.add_to_end_action.setEnabled(False)
        self.edit_action.setEnabled(False)

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
        global selected_object
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(Qt.darkGray)
        for obj in self.roads:
            self.draw_road(obj, qp)
        qp.setBrush(Qt.darkGray)
        for obj in self.intersections:
            self.draw_intersection(obj.center, obj.radius, qp)
        if selected_object is not None:
            qp.setBrush(Qt.yellow)
            if type(selected_object) is Road:
                self.draw_road(selected_object, qp)
            if type(selected_object) is Intersection:
                self.draw_intersection(selected_object.center, selected_object.radius, qp)
        qp.end()

    # change to first intersection!!!
    def first_road(self):
        start_coord = Coordinates(250, 250)

        center = Coordinates(start_coord.x, start_coord.y)
        i = Intersection(center, 40)
        self.intersections.append(i)
        self.update()

    def mousePressEvent(self, QMouseEvent):
        global selected_object
        print(QMouseEvent.pos())
        converted_position = Coordinates(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        for obj in self.roads:
            if obj.is_on_road(converted_position):
                selected_object = obj

        for obj in self.intersections:
            if obj.is_on_intersection(converted_position):
                selected_object = obj

        if selected_object is not None:
            self.edit_action.setEnabled(True)
            if type(selected_object) is Road:
                # check if start/end connection is present
                if selected_object.start_connection is None:
                    self.add_to_start_action.setEnabled(True)
                else:
                    self.add_to_start_action.setEnabled(False)

                if selected_object.end_connection is None:
                    self.add_to_end_action.setEnabled(True)
                else:
                    self.add_to_end_action.setEnabled(False)
            else:
                self.add_to_start_action.setEnabled(True)
                self.add_to_end_action.setEnabled(True)
        else:
            self.add_to_start_action.setEnabled(False)
            self.add_to_end_action.setEnabled(False)
            self.edit_action.setEnabled(False)

        self.update()

    def add_road_to_end_coord(self):
        global selected_object
        prev_road = selected_object
        if prev_road is None:
            return

        if type(prev_road) is Intersection:
            length = 75
            angle = 45 * (math.pi/180)
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
        global selected_object
        prev_road = selected_object
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

    def open_dialog(self):
        dialog = Dialog()
        dialog.exec_()
        dialog.show()


class Dialog(QDialog):
    radius = None
    in_lanes = None
    out_lanes = None

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Edit")

    def createFormGroupBox(self):
        global selected_object
        layout = QFormLayout()

        if type(selected_object) is Intersection:
            self.formGroupBox = QGroupBox("Intersection")
            self.radius = QSpinBox(self)
            self.radius.setMinimum(1)
            self.radius.setMaximum(100)
            self.radius.setValue(selected_object.radius)
            layout.addRow(QLabel("Radius:"), self.radius)
        else:
            self.formGroupBox = QGroupBox("Road")
            self.in_lanes = QSpinBox(self)
            self.in_lanes.setMinimum(0)
            self.in_lanes.setMaximum(10)
            self.in_lanes.setValue(selected_object.in_lanes)
            self.out_lanes = QSpinBox(self)
            self.out_lanes.setMinimum(0)
            self.out_lanes.setMaximum(10)
            self.out_lanes.setValue(selected_object.out_lanes)
            layout.addRow(QLabel("In Lanes:"), self.in_lanes)
            layout.addRow(QLabel("Out Lanes:"), self.out_lanes)

        self.formGroupBox.setLayout(layout)

    def accept(self):
        global selected_object
        if type(selected_object) is Intersection:
            selected_object.radius = self.radius.value()
        else:
            selected_object.in_lanes = self.in_lanes.value()
            selected_object.out_lanes = self.out_lanes.value()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    mb.first_road()
    sys.exit(app.exec_())
