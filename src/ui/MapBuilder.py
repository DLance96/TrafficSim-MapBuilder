import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.DriverProfile import DriverProfile
from src.map.VehicleProfile import VehicleProfile
from src.map.Constants import LANE_WIDTH
import math

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, \
    QPushButton, QGridLayout, QComboBox, QDialog, QDialogButtonBox, \
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, \
    QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtGui, QtCore

selected_object = None
profile_action_type = None
driver_profiles = []
vehicle_profiles = []

class MapBuilder(QMainWindow):
    roads = []
    intersections = []
    driver_profiles = []
    vehicle_profiles = []
    selected_object = None
    profile_action_num = None
    add_to_start_action = None
    add_to_end_action = None
    add_driver_action = None
    add_vehicle_action = None
    delete_driver_action = None
    delete_vehicle_action = None
    edit_action = None
    selected_menu = None
    profile_menu = None

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
        self.profile_menu = menu_bar.addMenu("Profile")

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)

        self.add_driver_action = QAction("Add Driver Profile", self)
        self.delete_driver_action = QAction("Delete Driver Profile", self)
        self.add_vehicle_action = QAction("Add Vehicle Profile", self)
        self.delete_vehicle_action = QAction("Delete Vehicle Profile", self)

        self.profile_menu.addAction(self.add_driver_action)
        self.profile_menu.addAction(self.add_vehicle_action)
        self.profile_menu.addAction(self.delete_driver_action)
        self.profile_menu.addAction(self.delete_vehicle_action)

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

        self.add_driver_action.triggered.connect(self.open_add_driver_profile_dialog)
        self.add_vehicle_action.triggered.connect(self.open_add_vehicle_profile_dialog)
        self.delete_driver_action.triggered.connect(self.open_delete_driver_profile_dialog)
        self.delete_vehicle_action.triggered.connect(self.open_delete_vehicle_profile_dialog)

        self.add_to_start_action.setEnabled(False)
        self.add_to_end_action.setEnabled(False)
        self.edit_action.setEnabled(False)

        # self.delete_vehicle_action.setEnabled(False)
        # self.delete_driver_action.setEnabled(False)

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


    def open_add_driver_profile_dialog(self):
        global profile_action_type
        profile_action_type = 0
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_add_vehicle_profile_dialog(self):
        global profile_action_type
        profile_action_type = 1
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_delete_driver_profile_dialog(self):
        global profile_action_type
        profile_action_type = 2
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_delete_vehicle_profile_dialog(self):
        global profile_action_type
        profile_action_type = 3
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

class ProfileDialog(QDialog):
    vehicle_name = None
    width = None
    length = None
    v_max_accel = None
    v_max_braking_decel = None
    v_mass = None
    v_max_speed = None

    driver_name = None
    over_braking_factor = None
    following_time = None
    d_max_accel = None
    d_min_accel = None
    d_max_speed = None
    d_accel_time = None
    update_time_ms = None

    def __init__(self):
        global profile_action_type
        super(ProfileDialog, self).__init__()

        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        if profile_action_type == 0:
            self.setWindowTitle("Add Driver Profile")
        elif profile_action_type == 1:
            self.setWindowTitle("Add Vehicle Profile")
        elif profile_action_type == 2:
            self.setWindowTitle("Delete Driver Profile")
        else:
            self.setWindowTitle("Delete Vehicle Profile")

    def createFormGroupBox(self):
        global profile_action_type
        layout = QFormLayout()


        if profile_action_type == 0:
            self.formGroupBox = QGroupBox("Attribute Input - Please fill in appropriate values below")

            self.driver_name = QLineEdit(self)

            self.over_braking_factor = QSpinBox(self)
            self.over_braking_factor.setMinimum(1)
            self.over_braking_factor.setMaximum(10)


            self.following_time = QSpinBox(self)
            self.following_time.setMinimum(1)
            self.following_time.setMaximum(25)

            self.d_max_accel = QSpinBox(self)
            self.d_max_accel.setMinimum(2)
            self.d_max_accel.setMaximum(14)

            self.d_min_accel = QSpinBox(self)
            self.d_min_accel.setMinimum(1)
            self.d_min_accel.setMaximum(4)

            self.d_max_speed = QSpinBox(self)
            self.d_max_speed.setMinimum(30)
            self.d_max_speed.setMaximum(200)

            self.d_accel_time = QSpinBox(self)
            self.d_accel_time.setMinimum(1)
            self.d_accel_time.setMaximum(30)

            self.update_time_ms = QSpinBox(self)
            self.update_time_ms.setMinimum(1)
            self.update_time_ms.setMaximum(20)

            layout.addRow(QLabel("Driver Profile Name: "), self.driver_name)
            layout.addRow(QLabel("Over-Braking Factor: "), self.over_braking_factor)
            layout.addRow(QLabel("Following Time (seconds): "), self.following_time)
            layout.addRow(QLabel("Maximum Acceleration (m/s^2): "), self.d_max_accel)
            layout.addRow(QLabel("Minimum Acceleration (m/s^2): "), self.d_min_accel)
            layout.addRow(QLabel("Maximum Speed (MPH): "), self.d_max_speed)
            layout.addRow(QLabel("Acceleration time (seconds): "), self.d_accel_time)
            layout.addRow(QLabel("How often Driver checks surroundings (ms): "), self.update_time_ms)

        elif profile_action_type == 1:
            self.formGroupBox = QGroupBox("Attribute Input - Please fill in appropriate values below")

            self.vehicle_name = QLineEdit(self)

            self.width = QSpinBox(self)
            self.width.setMinimum(5)
            self.width.setMaximum(8)

            self.length = QSpinBox(self)
            self.length.setMinimum(15)
            self.length.setMaximum(60)

            self.v_max_accel = QSpinBox(self)
            self.v_max_accel.setMinimum(2)
            self.v_max_accel.setMaximum(20)

            self.v_max_braking_decel = QSpinBox(self)
            self.v_max_braking_decel.setMinimum(2)
            self.v_max_braking_decel.setMaximum(8)

            self.v_mass = QSpinBox(self)
            self.v_mass.setMinimum(1000)
            self.v_mass.setMaximum(10000)

            self.v_max_speed = QSpinBox(self)
            self.v_max_speed.setMinimum(65)
            self.v_max_speed.setMaximum(200)

            layout.addRow(QLabel("Vehicle Profile Name: "), self.vehicle_name)
            layout.addRow(QLabel("Width (feet): "), self.width)
            layout.addRow(QLabel("Length (feet): "), self.length)
            layout.addRow(QLabel("Maximum Acceleration (m/s^2): "), self.v_max_accel)
            layout.addRow(QLabel("Maximum Braking Deceleration (m/s^2): "), self.v_max_braking_decel)
            layout.addRow(QLabel("Mass (kg): "), self.v_mass)
            layout.addRow(QLabel("Maximum Speed (MPH): "), self.v_max_speed)

        elif profile_action_type == 2:
            self.formGroupBox = QGroupBox("Select Driver Profile to delete")

            driver_profile_names = []

            for prof_name in driver_profiles:
                name = prof_name.get_driver_profile_name()
                driver_profile_names.append(name)

            name_list = QComboBox(self)

            for name in driver_profile_names:
                name_list.addItem(name)

            layout.addRow(QLabel("Profile to be deleted: "), name_list)

        else:
            self.formGroupBox = QGroupBox("Select Vehicle Profile to delete")

            vehicle_profile_names = []

            for prof_name in vehicle_profiles:
                name = prof_name.get_vehicle_profile_name()
                vehicle_profile_names.append(name)

            name_list = QComboBox(self)

            for name in vehicle_profile_names:
                name_list.addItem(name)

            layout.addRow(QLabel("Profile to be deleted: "), name_list)


        self.formGroupBox.setLayout(layout)

    def accept(self):
        global profile_action_type
        global driver_profiles
        global vehicle_profiles

        if profile_action_type == 0:
            driver = DriverProfile(self.driver_name.text(), self.over_braking_factor.value(),
                                   self.following_time.value(), self.d_max_accel.value(),
                                   self.d_min_accel.value(), self.d_max_speed.value(),
                                   self.d_accel_time.value(), self.update_time_ms.value())
            if self.driver_name.text() != '':
                driver_profiles.append(driver)

        elif profile_action_type == 1:
            vehicle = VehicleProfile(self.vehicle_name.text(), self.width.value(), self.length.value(),
                                     self.v_max_accel.value(), self.v_max_braking_decel.value(),
                                     self.v_mass.value(), self.v_max_speed.value())

            if self.vehicle_name.text() != '':
                vehicle_profiles.append(vehicle)

        print('num driver profiles = ' + str(len(driver_profiles)))

        # print('driver profile name = ' + driver_profiles[0].get_driver_profile_name())
        print('num vehicle profiles = ' + str(len(vehicle_profiles)))

        self.close()


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
