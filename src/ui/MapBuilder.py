import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.Constants import LANE_WIDTH
import math

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, \
    QPushButton, QGridLayout, QComboBox, QDialog, QButtonGroup, QDialogButtonBox, \
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QCheckBox, QLabel, QLineEdit, \
    QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtGui, QtCore

selected_object = None
road = []
intersection = []
driver_profiles = []
vehicle_profiles = []

class MapBuilder(QMainWindow):
    global road
    global intersection
    global driver_profiles
    global vehicle_profiles

    selected_object = None
    add_action = None
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

    def initUI(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        self.selected_menu = menu_bar.addMenu("MapObject")
        profile_menu = menu_bar.addMenu("Profile")

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        add_driver_action = QAction("Add Driver Profile", self)
        delete_driver_action = QAction("Delete Driver Profile", self)
        add_vehicle_action = QAction("Add Vehicle Profile", self)
        delete_vehicle_action = QAction("Delete Vehicle Profile", self)

        profile_menu.addAction(add_driver_action)
        profile_menu.addAction(add_vehicle_action)
        profile_menu.addAction(delete_driver_action)
        profile_menu.addAction(delete_vehicle_action)

        self.add_action = QAction("Add Connection", self)
        self.edit_action = QAction("Edit", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        self.selected_menu.addAction(self.add_action)
        self.selected_menu.addAction(self.edit_action)

        self.add_action.triggered.connect(self.open_add_dialog)
        self.edit_action.triggered.connect(self.open_edit_dialog)

        self.add_action.setEnabled(False)
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
        for obj in road:
            self.draw_road(obj, qp)
        qp.setBrush(Qt.darkGray)
        for obj in intersection:
            self.draw_intersection(obj.center, obj.radius, qp)
        if selected_object is not None:
            qp.setBrush(Qt.yellow)
            if type(selected_object) is Road:
                self.draw_road(selected_object, qp)
            if type(selected_object) is Intersection:
                self.draw_intersection(selected_object.center, selected_object.radius, qp)
            self.update_menu_bar()
        qp.end()

    def first_road(self):
        start_coord = Coordinates(250, 250)

        center = Coordinates(start_coord.x, start_coord.y)
        i = Intersection(center, 40)
        intersection.append(i)
        self.update()

    def mousePressEvent(self, QMouseEvent):
        global selected_object
        print(QMouseEvent.pos())
        converted_position = Coordinates(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        for obj in road:
            if obj.is_on_road(converted_position):
                selected_object = obj

        for obj in intersection:
            if obj.is_on_intersection(converted_position):
                selected_object = obj

        self.update()

    # called in paint function to make sure menu bar updates immediately with added objects
    def update_menu_bar(self):
        if selected_object is not None:
            self.edit_action.setEnabled(True)
            if type(selected_object) is Road:
                # check if start/end connection is present
                if selected_object.start_connection is None:
                    self.add_action.setEnabled(True)
                elif selected_object.end_connection is None:
                    self.add_action.setEnabled(True)
                else:
                    self.add_action.setEnabled(False)
            else:
                self.add_action.setEnabled(True)
        else:
            self.add_action.setEnabled(False)
            self.edit_action.setEnabled(False)

    def open_edit_dialog(self):
        dialog = EditDialog()
        dialog.exec_()
        dialog.show()

    def open_add_dialog(self):
        dialog = AddDialog()
        dialog.exec_()
        dialog.show()


class EditDialog(QDialog):
    global road
    global intersection
    global driver_profiles
    global vehicle_profiles

    radius = None
    in_lanes = None
    out_lanes = None

    def __init__(self):
        super(EditDialog, self).__init__()
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


class AddDialog(QDialog):
    global road
    global intersection
    global driver_profiles
    global vehicle_profiles

    add_position = None
    radius = None
    in_lanes = None
    out_lanes = None
    angle = None

    def __init__(self):
        super(AddDialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Add")

    def createFormGroupBox(self):
        global selected_object
        layout = QFormLayout()

        if type(selected_object) is Road:
            self.formGroupBox = QGroupBox("Add Intersection")
            self.add_position = QComboBox()
            if selected_object.start_connection is None:
                self.add_position.addItem("Start")
            if selected_object.end_connection is None:
                self.add_position.addItem("End")
            layout.addRow(QLabel("Position:"), self.add_position)
            self.radius = QSpinBox(self)
            self.radius.setMinimum(1)
            self.radius.setMaximum(100)
            self.radius.setValue(40)
            layout.addRow(QLabel("Radius:"), self.radius)
        else:
            self.formGroupBox = QGroupBox("Add Road")
            self.angle = QSpinBox(self)
            self.angle.setMinimum(0)
            self.angle.setMaximum(360)
            self.angle.setValue(0)
            layout.addRow(QLabel("Angle:"), self.angle)
            self.radius = QSpinBox(self)
            self.radius.setMinimum(1)
            self.radius.setMaximum(100)
            self.radius.setValue(40)
            layout.addRow(QLabel("Length:"), self.radius)
            self.in_lanes = QSpinBox(self)
            self.in_lanes.setMinimum(0)
            self.in_lanes.setMaximum(10)
            self.in_lanes.setValue(1)
            self.out_lanes = QSpinBox(self)
            self.out_lanes.setMinimum(0)
            self.out_lanes.setMaximum(10)
            self.out_lanes.setValue(1)
            layout.addRow(QLabel("In Lanes:"), self.in_lanes)
            layout.addRow(QLabel("Out Lanes:"), self.out_lanes)

        self.formGroupBox.setLayout(layout)

    def accept(self):
        global selected_object
        if type(selected_object) is Road:
            if self.add_position.currentText() == "End":
                intersection.append(selected_object.generate_end_connection(self.radius.value()))
            else:
                intersection.append(selected_object.generate_start_connection(self.radius.value()))
        else:
            road.append(selected_object.add_connection(self.angle.value() * math.pi / 180, self.radius.value(),
                                           self.in_lanes.value(), self.out_lanes.value()))
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    mb.first_road()
    sys.exit(app.exec_())
