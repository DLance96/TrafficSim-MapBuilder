import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.DriverProfile import DriverProfile
from src.map.VehicleProfile import VehicleProfile
from src.map.SpawningProfile import SpawningProfile
from src.map.Constants import LANE_WIDTH
from src.xml_parse.Import import import_xml
from src.xml_parse.Export import export_xml
import math

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, \
    QPushButton, QGridLayout, QComboBox, QDialog, QButtonGroup, QDialogButtonBox, \
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QCheckBox, QLabel, QLineEdit, \
    QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtGui, QtCore

selected_object = None
profile_action_type = None
road = []
intersection = []
driver_profiles = []
vehicle_profiles = []
spawning_profiles = []
app = None

testing = False

class MapBuilder(QMainWindow):
    """
    The main class for the MapBuilder. Instantiates the UI that is used to construct traffic maps.
    """

    global road
    global intersection
    global driver_profiles
    global vehicle_profiles
    global spawning_profiles
    global app

    y_offset = 0
    x_offset = 0

    selected_object = None
    profile_action_num = None
    add_driver_action = None
    add_vehicle_action = None
    add_spawn_action = None
    delete_driver_action = None
    delete_vehicle_action = None
    delete_spawn_action = None
    add_action = None
    edit_action = None
    add_spawn = None
    delete_spawn = None
    selected_menu = None
    spawning_profile_menu = None
    vehicle_profile_menu = None
    driver_profile_menu = None
    auto_connect = None
    save_action = None
    open_action = None
    new_action = None

    # Traffic Light Menu Actions
    traffic_light_menu = None
    edit_yellow_light = None
    add_cycle = None
    remove_cycle = None
    reset_light = None

    def __init__(self):
        super().__init__()
        self.title = 'Map Builder'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.initUI()

        default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
        default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)
        default_spawn = SpawningProfile("Default", default_driver, default_vehicle)

        driver_profiles.append(default_driver)
        vehicle_profiles.append(default_vehicle)
        spawning_profiles.append(default_spawn)

    def initUI(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        self.selected_menu = menu_bar.addMenu("MapObject")
        self.profile_menu = menu_bar.addMenu("Profile")
        self.traffic_light_menu = menu_bar.addMenu("StopLight")

        #StopLight Actions
        self.edit_yellow_light = QAction("Edit Yellow Light Length", self)
        self.add_cycle = QAction("Add Cycle", self)
        self.remove_cycle = QAction("Remove Cycle", self)
        self.reset_light = QAction("Reset Light", self)
        self.traffic_light_menu.addAction(self.edit_yellow_light)
        self.traffic_light_menu.addAction(self.add_cycle)
        self.traffic_light_menu.addAction(self.remove_cycle)
        self.traffic_light_menu.addAction(self.reset_light)
        self.edit_yellow_light.triggered.connect(self.open_update_yellow_dialog)
        self.add_cycle.triggered.connect(self.open_add_cycle_dialog)
        self.reset_light.triggered.connect(self.reset_stoplight)
        self.traffic_light_menu.setEnabled(False)

        self.driver_profile_menu = menu_bar.addMenu("Driver Profile")
        self.vehicle_profile_menu = menu_bar.addMenu("Vehicle Profile")
        self.spawning_profile_menu = menu_bar.addMenu("Spawning Profile")

        #File Actions
        self.new_action = QAction("New", self)
        self.new_action.triggered.connect(self.reset_file)
        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.import_to_file)
        self.open_action.setEnabled(False)
        self.save_action = QAction("Save", self)
        self.save_action.triggered.connect(self.export_to_file)

        self.add_driver_action = QAction("Add Driver Profile", self)
        self.delete_driver_action = QAction("Delete Driver Profile", self)
        self.add_vehicle_action = QAction("Add Vehicle Profile", self)
        self.delete_vehicle_action = QAction("Delete Vehicle Profile", self)
        self.add_spawn_action = QAction("Add Spawning Profile", self)
        self.delete_spawn_action = QAction("Delete Spawning Profile", self)

        self.driver_profile_menu.addAction(self.add_driver_action)
        self.driver_profile_menu.addAction(self.delete_driver_action)

        self.vehicle_profile_menu.addAction(self.add_vehicle_action)
        self.vehicle_profile_menu.addAction(self.delete_vehicle_action)

        self.spawning_profile_menu.addAction(self.add_spawn_action)
        self.spawning_profile_menu.addAction(self.delete_spawn_action)

        self.add_action = QAction("Add Connection", self)
        self.edit_action = QAction("Edit MapObject", self)
        self.add_spawn = QAction("Add Spawning Profile", self)
        self.delete_spawn = QAction("Delete Spawning Profile", self)
        self.auto_connect = QAction("Connect Intersections", self)

        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

        self.selected_menu.addAction(self.add_action)
        self.selected_menu.addAction(self.edit_action)
        self.selected_menu.addAction(self.add_spawn)
        self.selected_menu.addAction(self.delete_spawn)
        self.selected_menu.addAction(self.auto_connect)

        self.add_action.triggered.connect(self.open_add_dialog)
        self.edit_action.triggered.connect(self.open_edit_dialog)
        self.add_spawn.triggered.connect(self.add_profile_to_intersection_dialog)
        self.delete_spawn.triggered.connect(self.delete_profile_from_intersection_dialog)
        self.auto_connect.triggered.connect(self.open_connect_dialog)

        self.add_driver_action.triggered.connect(self.open_add_driver_profile_dialog)
        self.add_vehicle_action.triggered.connect(self.open_add_vehicle_profile_dialog)
        self.add_spawn_action.triggered.connect(self.open_add_spawn_profile_dialog)
        self.delete_driver_action.triggered.connect(self.open_delete_driver_profile_dialog)
        self.delete_vehicle_action.triggered.connect(self.open_delete_vehicle_profile_dialog)
        self.delete_spawn_action.triggered.connect(self.open_delete_spawn_profile_dialog)

        self.add_action.setEnabled(False)
        self.edit_action.setEnabled(False)
        self.add_spawn.setEnabled(False)
        self.delete_spawn.setEnabled(False)
        self.auto_connect.setEnabled(False)

        self.delete_driver_action.setEnabled(False)
        self.delete_spawn_action.setEnabled(False)
        self.delete_vehicle_action.setEnabled(False)

        # need some means of setting these active once a vehicle/driver/spawn profile is added.
        # self.delete_vehicle_action.setEnabled(False)
        # self.delete_driver_action.setEnabled(False)
        # self.delete_spawn_action.setEnabled(False)

        screen = app.primaryScreen()
        self.resize(screen.size().width(), screen.size().height())
        self.setWindowTitle("Traffic Simulator - Map Builder")
        self.setFixedSize(self.size())

        self.show()

    def reset_file(self):
        global road, intersection, selected_object
        road = []
        intersection = []
        selected_object = None
        self.first_road()

    def export_to_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "XML Files (*.xml)", options=options)
        if filename:
            print(filename)
            export_xml(road, intersection, filename)

    def import_to_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "XML Files (*.xml)", options=options)
        if filename:
            print(filename)
            import_xml(filename)

    def draw_road(self, road, qp):

        polygon = QtGui.QPolygonF()

        for point in road.get_points():
            polygon.append(QtCore.QPoint(point.x + self.x_offset, point.y + self.y_offset))

        qp.drawPolygon(polygon)

        qp.setPen(Qt.lightGray)
        point_one = QtCore.QPoint(road.start_coord.x + self.x_offset, road.start_coord.y + self.y_offset)
        point_two = QtCore.QPoint(road.end_coord.x + self.x_offset, road.end_coord.y + self.y_offset)
        qp.drawLine(point_one, point_two)
        qp.setPen(Qt.black)

    def draw_intersection(self, center, radius, qp):
        qp.drawEllipse(center.x - radius + self.x_offset, center.y - radius + self.y_offset, radius * 2, radius * 2)

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
        global selected_object
        start_coord = Coordinates(400,250)

        center = Coordinates(start_coord.x, start_coord.y)
        i = Intersection(center, 40, 25)
        intersection.append(i)

        selected_object = intersection[0]
        self.update()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_W:
            self.y_offset = self.y_offset + 5
        elif key == QtCore.Qt.Key_A:
            self.x_offset = self.x_offset + 5
        elif key == QtCore.Qt.Key_S:
            self.y_offset = self.y_offset - 5
        elif key == QtCore.Qt.Key_D:
            self.x_offset = self.x_offset - 5
        elif key == QtCore.Qt.Key_R:
            self.x_offset = 0
            self.y_offset = 0
        self.update()

    def mousePressEvent(self, QMouseEvent):
        global selected_object
        print(QMouseEvent.pos())
        converted_position = Coordinates(QMouseEvent.pos().x() - self.x_offset, QMouseEvent.pos().y() - self.y_offset)
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
                self.traffic_light_menu.setEnabled(False)
                self.add_spawn.setEnabled(False)
                # check if start/end connection is present
                self.auto_connect.setEnabled(False)
                if selected_object.start_connection is None:
                    self.add_action.setEnabled(True)
                    self.delete_spawn.setEnabled(False)
                    self.add_spawn.setEnabled(False)
                elif selected_object.end_connection is None:
                    self.add_action.setEnabled(True)
                    self.delete_spawn.setEnabled(False)
                    self.add_spawn.setEnabled(False)
                else:
                    self.add_action.setEnabled(False)
            else:

                if len(intersection) > 1:
                    self.auto_connect.setEnabled(True)
                else:
                    self.auto_connect.setEnabled(False)
                self.traffic_light_menu.setEnabled(True)
                self.remove_cycle.setEnabled(False)
                # self.auto_connect.setEnabled(True)
                self.add_action.setEnabled(True)
                self.add_spawn.setEnabled(True)

                if selected_object.spawn_profiles:
                    self.delete_spawn.setEnabled(True)
                else:
                    self.delete_spawn.setEnabled(False)

        else:
            self.add_action.setEnabled(False)
            self.edit_action.setEnabled(False)

        if len(driver_profiles) > 1:
            self.delete_driver_action.setEnabled(True)
        else:
            self.delete_driver_action.setEnabled(False)

        if len(vehicle_profiles) > 1:
            self.delete_vehicle_action.setEnabled(True)
        else:
            self.delete_vehicle_action.setEnabled(False)

        if len(spawning_profiles) > 1:
            self.delete_spawn_action.setEnabled(True)
        else:
            self.delete_spawn_action.setEnabled(False)

    def reset_stoplight(self):
        global selected_object

        selected_object.reset_light()

    def open_edit_dialog(self):
        dialog = EditDialog()
        dialog.exec_()
        dialog.show()

    def open_add_dialog(self):
        dialog = AddDialog()
        dialog.exec_()
        dialog.show()

    def open_update_yellow_dialog(self):
        dialog = YellowDialog()
        dialog.exec_()
        dialog.show()

    def open_add_cycle_dialog(self):
        dialog = AddCycleDialog()
        dialog.exec_()
        dialog.show()


    def open_connect_dialog(self):
        """
        Helper method that links the "Connect Intersections" button to its prompt.
        :return: the prompt that allows users to connect two intersections
        """
        dialog = ConnectDialog()
        dialog.exec_()
        dialog.show()

    def open_add_driver_profile_dialog(self):
        """
        Helper method that links the "Add Driver Profile" button to its prompt
        :return: the prompt that allows users to create a driver profile
        """
        global profile_action_type
        profile_action_type = 0
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_add_vehicle_profile_dialog(self):
        """
        Helper method that links the "Add Vehicle Profile" button to its prompt
        :return: the prompt that allows users to create a vehicle profile
        """
        global profile_action_type
        profile_action_type = 1
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_delete_driver_profile_dialog(self):
        """
        Helper method that links the "Delete Driver Profile" button to its prompt
        :return: the prompt that allows users to delete a driver profile
        """
        global profile_action_type
        profile_action_type = 2
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_delete_vehicle_profile_dialog(self):
        """
        Helper method that links the "Delete Vehicle Profile" button to its prompt
        :return: the prompt that allows users to delete a vehicle profile
        """
        global profile_action_type
        profile_action_type = 3
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_add_spawn_profile_dialog(self):
        """
        Helper method that links the "Add Spawning Profile" button to its prompt
        :return: the prompt that allows users to create a spawning profile
        """
        global profile_action_type
        profile_action_type = 4
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def open_delete_spawn_profile_dialog(self):
        """
        Helper method that links the "Delete Spawning Profile" button to its prompt
        :return: the prompt that allows users to delete a spawning profile
        """
        global profile_action_type
        profile_action_type = 5
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def add_profile_to_intersection_dialog(self):
        """
        Helper method that links the "Add Spawning Profile" button (in MapObject dropdown) to its prompt
        :return: the prompt that allows users to add a spawning profile to an intersection
        """
        global profile_action_type
        profile_action_type = 6
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

    def delete_profile_from_intersection_dialog(self):
        """
        Helper method that links the "Remove Spawning Profile" button (in MapObject dropdown) to its prompt
        :return: the prompt that allows users to remove a spawning profile from an intersection
        """
        global profile_action_type
        profile_action_type = 7
        dialog = ProfileDialog()
        dialog.exec_()
        dialog.show()

class ConnectDialog(QDialog):
    """
    Dialog for a user to connect two intersections together
    """

    intersection_list = None

    def __init__(self):
        super(ConnectDialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Connect Intersections")

    def createFormGroupBox(self):
        """
        This section allows the user to select which intersection to connect to, relative to the
        intersection that is currently selected
        :return: Connected intersections
        """

        global selected_object
        global intersection
        layout = QFormLayout()

        self.formGroupBox = QGroupBox("Choose Intersection to Connect to")

        index_of_selected_object = intersection.index(selected_object)

        self.intersection_list = QComboBox(self)

        for x in range(len(intersection)):
            if x != index_of_selected_object:
                self.intersection_list.addItem(str(x))

        layout.addRow(QLabel("Intersection: "), self.intersection_list)

        self.formGroupBox.setLayout(layout)

    def accept(self):
        """
        After the user selects the intersection to connect to and hits "accept", this method then
        connects two intersections together via a road.
        :return: Connected intersections.
        """
        global selected_object

        start_roads = selected_object.get_connections()

        num = int(self.intersection_list.currentText())

        dest_intersect = intersection[num]

        end_roads = intersection[num].get_connections()

        connected = False

        for s_road in start_roads:
            if s_road in end_roads:
                connected = True
                break

        if not connected:
            start_center = selected_object.get_center()
            end_center =  dest_intersect.get_center()

            add_theta = None
            theta = None
            angle = None

            deltax = end_center.get_x() - start_center.get_x()
            deltay = end_center.get_y() - start_center.get_y()

            if (deltax == 0) & (deltay > 0):
                add_theta = 0
                theta = 0
                angle = add_theta
            elif (deltax == 0) & (deltay < 0):
                add_theta = math.pi
                theta = 0
                angle = add_theta
            elif (deltax > 0) & (deltay == 0):
                add_theta = math.pi / 2
                theta = 0
                angle = add_theta
            elif (deltax < 0) & (deltay == 0):
                add_theta = (3 * math.pi) / 2
                theta = 0
                angle = add_theta
            elif (deltax > 0) & (deltay > 0):
                add_theta = math.pi / 2
                theta = math.atan((deltay / deltax))
                angle = add_theta - theta
            elif (deltax > 0) & (deltay < 0):
                add_theta = math.pi / 2
                theta = math.atan((deltay / deltax))
                angle = add_theta - theta
            elif (deltax < 0) & (deltay < 0):
                add_theta = (3 * math.pi) / 2
                theta = math.atan((deltay / deltax))
                angle = add_theta - theta
            else:
                add_theta = (3 * math.pi) / 2
                theta = math.atan((deltay / deltax))
                angle = add_theta - theta

            start_rad = selected_object.get_radius()
            end_rad = dest_intersect.get_radius()

            deltax_square = deltax * deltax
            deltay_square = deltay * deltay
            total_dist = math.sqrt(deltax_square + deltay_square)

            road_length = total_dist - (start_rad + end_rad)

            new_road = selected_object.add_connection(angle, road_length, 2, 2, 50, 'ConnectingRoad')

            new_road.add_start_connection(selected_object)
            new_road.add_end_connection(dest_intersect)

            road.append(new_road)

            dest_intersect.add_incoming_connection(new_road)

        self.close()

class ProfileDialog(QDialog):
    """
    This class is used for ALL profile operations. Specifically, it is used to add and delete vehicle, driver
    and spawning profiles. This class is also used to attach/remove spawning profiles to/from intersections.
    """

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

    deleted_driver = None
    deleted_vehicle = None
    deleted_spawn = None

    driver_name_list = None
    vehicle_name_list = None
    spawn_name_list = None

    add_spawn_intersection = None
    intersection_add_spawn = None
    delete_spawn_intersection = None
    intersection_deleted_spawn = None

    driver_for_spawn = None
    driver_name_for_spawn = None
    vehicle_for_spawn = None
    vehicle_name_for_spawn = None
    spawn_name = None

    def __init__(self):
        global profile_action_type
        global selected_object
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
        elif profile_action_type == 3:
            self.setWindowTitle("Delete Vehicle Profile")
        elif profile_action_type == 4:
            self.setWindowTitle("Add Spawning Profile")
        elif profile_action_type == 5:
            self.setWindowTitle("Delete Spawning Profile")
        elif profile_action_type == 6:
            self.setWindowTitle("Add Spawning Profile to Intersection")
        else:
            self.setWindowTitle("Remove Spawning Profile from Intersection")

    def createFormGroupBox(self):
        """
        This function is where a majority of the user input is determined. Depending on the circumstance, users will
        use this function to create/delete spawning, vehicle and driver profiles, as well as attach/remove spawning
        profiles from intersections
        :return: A modified state of the MapBuilder scene depending on which variables are affected.
        """
        global profile_action_type
        global selected_object
        layout = QFormLayout()


        if profile_action_type == 0:
            """
            In this instance, a user is able to create a driver profile
            """
            self.formGroupBox = QGroupBox("Attribute Input - Please fill in appropriate values below")

            self.driver_name = QLineEdit(self)
            self.driver_name.insert('testDriverName')

            self.over_braking_factor = QSpinBox(self)
            self.over_braking_factor.setMinimum(1)
            self.over_braking_factor.setMaximum(10)


            self.following_time = QSpinBox(self)
            self.following_time.setMinimum(1)
            self.following_time.setMaximum(8)

            self.d_max_accel = QSpinBox(self)
            self.d_max_accel.setMinimum(4)
            self.d_max_accel.setMaximum(30)

            self.d_min_accel = QSpinBox(self)
            self.d_min_accel.setMinimum(0)
            self.d_min_accel.setMaximum(4)

            self.d_max_speed = QSpinBox(self)
            self.d_max_speed.setMinimum(100)
            self.d_max_speed.setMaximum(400)

            self.d_accel_time = QSpinBox(self)
            self.d_accel_time.setMinimum(1)
            self.d_accel_time.setMaximum(10)

            self.update_time_ms = QSpinBox(self)
            self.update_time_ms.setMinimum(500)
            self.update_time_ms.setMaximum(5000)

            layout.addRow(QLabel("Driver Profile Name: "), self.driver_name)
            layout.addRow(QLabel("Over-Braking Factor: "), self.over_braking_factor)
            layout.addRow(QLabel("Following Time (seconds): "), self.following_time)
            layout.addRow(QLabel("Maximum Acceleration (m/s^2): "), self.d_max_accel)
            layout.addRow(QLabel("Minimum Acceleration (m/s^2): "), self.d_min_accel)
            layout.addRow(QLabel("Maximum Speed (km/hr): "), self.d_max_speed)
            layout.addRow(QLabel("Acceleration time (seconds): "), self.d_accel_time)
            layout.addRow(QLabel("How often Driver checks surroundings (milliseconds): "), self.update_time_ms)
            layout.addRow(QLabel("WARNING: Only driver profiles with UNIQUE profile names will be stored!"))
            layout.addRow(QLabel("(i.e. names that are not currently in use)"))

        elif profile_action_type == 1:
            """
            In this instance, the user is able to create a vehicle profile
            """
            self.formGroupBox = QGroupBox("Attribute Input - Please fill in appropriate values below")

            self.vehicle_name = QLineEdit(self)
            self.vehicle_name.insert('testVehicleName')

            self.width = QSpinBox(self)
            self.width.setMinimum(3)
            self.width.setMaximum(5)

            self.length = QSpinBox(self)
            self.length.setMinimum(4)
            self.length.setMaximum(15)

            self.v_max_accel = QSpinBox(self)
            self.v_max_accel.setMinimum(1)
            self.v_max_accel.setMaximum(25)

            self.v_max_braking_decel = QSpinBox(self)
            self.v_max_braking_decel.setMinimum(3)
            self.v_max_braking_decel.setMaximum(20)

            self.v_mass = QSpinBox(self)
            self.v_mass.setMinimum(1000)
            self.v_mass.setMaximum(6000)

            self.v_max_speed = QSpinBox(self)
            self.v_max_speed.setMinimum(100)
            self.v_max_speed.setMaximum(400)

            layout.addRow(QLabel("Vehicle Profile Name: "), self.vehicle_name)
            layout.addRow(QLabel("Width (m): "), self.width)
            layout.addRow(QLabel("Length (m): "), self.length)
            layout.addRow(QLabel("Maximum Acceleration (m/s^2): "), self.v_max_accel)
            layout.addRow(QLabel("Maximum Braking Deceleration (m/s^2): "), self.v_max_braking_decel)
            layout.addRow(QLabel("Mass (kg): "), self.v_mass)
            layout.addRow(QLabel("Maximum Speed (km/hr): "), self.v_max_speed)
            layout.addRow(QLabel("WARNING: Only vehicle profiles with UNIQUE profile names will be stored!"))
            layout.addRow(QLabel("(i.e. names that are not currently in use)"))

        elif profile_action_type == 2:
            """
            In this case, a user is able to select which pre-existing driver profile to delete.
            """
            self.formGroupBox = QGroupBox("Select Driver Profile to delete")

            driver_profile_names = []

            for prof_name in driver_profiles:
                name = prof_name.get_driver_profile_name()
                if name != 'Default':
                    driver_profile_names.append(name)

            self.driver_name_list = QComboBox(self)

            for name in driver_profile_names:
                self.driver_name_list.addItem(name)

            layout.addRow(QLabel("Profile to be deleted: "), self.driver_name_list)
            layout.addRow(QLabel("WARNING: If a spawning profile contains this driver profile, then it will also be deleted."))
            layout.addRow(QLabel("The affected spawning profile will also be removed from any intersection that currently uses it."))

        elif profile_action_type == 3:
            """
            In this case, a user is able to select which pre-existing vehicle profile to delete.
            """
            self.formGroupBox = QGroupBox("Select Vehicle Profile to delete")

            vehicle_profile_names = []

            for prof_name in vehicle_profiles:
                name = prof_name.get_vehicle_profile_name()
                if name != 'Default':
                    vehicle_profile_names.append(name)

            self.vehicle_name_list = QComboBox(self)

            for name in vehicle_profile_names:
                self.vehicle_name_list.addItem(name)

            layout.addRow(QLabel("Profile to be deleted: "), self.vehicle_name_list)
            layout.addRow(QLabel("WARNING: If a spawning profile contains this vehicle profile, then it will also be deleted."))
            layout.addRow(QLabel("The affected spawning profile will also be removed from any intersection that currently uses it."))

        elif profile_action_type == 4:
            """
            In this case, a user is able to create a spawning profile
            """
            self.formGroupBox = QGroupBox("Attribute Input - Please select appropriate values below")

            vehicle_profile_name_list = []
            driver_profile_name_list = []

            for v in vehicle_profiles:
                name = v.get_vehicle_profile_name()
                vehicle_profile_name_list.append(name)


            for d in driver_profiles:
                name = d.get_driver_profile_name()
                driver_profile_name_list.append(name)

            self.spawn_name = QLineEdit(self)
            self.spawn_name.insert('testSpawnName')
            self.driver_for_spawn = QComboBox(self)
            self.vehicle_for_spawn = QComboBox(self)

            for name in vehicle_profile_name_list:
                self.vehicle_for_spawn.addItem(name)

            for name in driver_profile_name_list:
                self.driver_for_spawn.addItem(name)

            layout.addRow(QLabel("Name of Spawning Profile"), self.spawn_name)
            layout.addRow(QLabel("Vehicle Profile: "), self.vehicle_for_spawn)
            layout.addRow(QLabel("Driver Profile: "), self.driver_for_spawn)
            layout.addRow(QLabel("WARNING: Only spawning profiles with UNIQUE names will be stored!"))
            layout.addRow(QLabel("(i.e. names that are not currently in use)"))

        elif profile_action_type == 5:
            """
            In this case, a user is able to select which pre-existing spawning profile to delete.
            """
            self.formGroupBox = QGroupBox("Select Spawning Profile to delete")

            spawning_profile_names = []

            for prof_name in spawning_profiles:
                name = prof_name.get_spawning_profile_name()
                if name != 'Default':
                    spawning_profile_names.append(name)

            self.spawn_name_list = QComboBox(self)

            for name in spawning_profile_names:
                self.spawn_name_list.addItem(name)

            layout.addRow(QLabel("Profile to be deleted: "), self.spawn_name_list)
            layout.addRow(QLabel("WARNING: Intersections that currently store this spawning profile will also remove said"))
            layout.addRow(QLabel("profile from their lists."))

        elif profile_action_type == 6:
            """
            In this case, a user is able to select which pre-existing driver profile to add to an intersection.
            """
            self.formGroupBox = QGroupBox("Select Spawning Profile to add to Intersection")

            spawning_profile_names = []

            for prof_name in spawning_profiles:
                name = prof_name.get_spawning_profile_name()
                spawning_profile_names.append(name)

            self.add_spawn_intersection = QComboBox(self)

            for name in spawning_profile_names:
                self.add_spawn_intersection.addItem(name)

            layout.addRow(QLabel("Spawning Profile to be added:"), self.add_spawn_intersection)

        else:
            """
            In this case, a user is able to select which pre-existing driver profile to remove from an intersection.
            """
            self.formGroupBox = QGroupBox("Select Spawning Profile to delete from Intersection")

            spawning_profile_names = []

            for prof_name in selected_object.spawn_profiles:
                name = prof_name.get_spawning_profile_name()
                spawning_profile_names.append(name)

            self.delete_spawn_intersection = QComboBox(self)

            for name in spawning_profile_names:
                self.delete_spawn_intersection.addItem(name)

            layout.addRow(QLabel("Spawning Profile to be deleted:"), self.delete_spawn_intersection)

        self.formGroupBox.setLayout(layout)



    def accept(self):
        """
        Once a user selects "accept" at the end of the createGroupFormBox method, this method is then used
        to modify the current state of the system based of the actions of the user.
        :return: a modified state
        """
        global profile_action_type
        global driver_profiles
        global vehicle_profiles
        global spawning_profiles
        global selected_object
        global intersection

        if profile_action_type == 0:
            """
            A driver profile is instantiated and stored.
            """
            driver = DriverProfile(self.driver_name.text(), self.over_braking_factor.value(),
                                   self.following_time.value(), self.d_max_accel.value(),
                                   self.d_min_accel.value(), self.d_max_speed.value(),
                                   self.d_accel_time.value(), self.update_time_ms.value())

            name_in_use = False

            for profile in driver_profiles:
                if profile.get_driver_profile_name() == self.driver_name.text():
                    name_in_use = True
                    break


            if (self.driver_name.text() != '') & (not name_in_use):
                driver_profiles.append(driver)
                # need to enable the delete_driver_action
                # need to display error message of some sort when no name is given

        elif profile_action_type == 1:
            """
            A vehicle profile is instantiated and stored.
            """
            vehicle = VehicleProfile(self.vehicle_name.text(), self.width.value(), self.length.value(),
                                     self.v_max_accel.value(), self.v_max_braking_decel.value(),
                                     self.v_mass.value(), self.v_max_speed.value())

            name_in_use = False

            for profile in vehicle_profiles:
                if profile.get_vehicle_profile_name() == self.vehicle_name.text():
                    name_in_use = True
                    break

            if (self.vehicle_name.text() != '') & (not name_in_use):
                vehicle_profiles.append(vehicle)

        elif profile_action_type == 2:
            """
            A driver profile is deleted. Other objects using the driver profile are also deleted (i.e. spawning
            profile).
            """
            self.deleted_driver = self.driver_name_list.currentText()

            deleted_profile = None
            spawning_profiles_to_delete = []

            for profile in driver_profiles:
                name = profile.get_driver_profile_name()
                if name == str(self.deleted_driver):
                    deleted_profile = profile
                    break

            if deleted_profile is not None:

                for profile in spawning_profiles:
                    if profile.get_driver_profile() == deleted_profile:
                        spawning_profiles_to_delete.append(profile)

                for profile in spawning_profiles_to_delete:
                    for i in intersection:
                        for spawn in i.get_spawning_profile_list():
                            if spawn == profile:
                                i.get_spawning_profile_list().remove(spawn)

                for profile in spawning_profiles_to_delete:
                    spawning_profiles.remove(profile)

                driver_profiles.remove(deleted_profile)


            #Remaining code in this else if statement is used for testing.
            print(str(len(driver_profiles)))

            for profile in driver_profiles:
                print(str(profile.get_driver_profile_name()) + ' ')

        elif profile_action_type == 3:
            """
            A vehicle profile is deleted. Other objects using the vehicle profile are also deleted (i.e. spawning
            profile).
            """
            self.deleted_vehicle = self.vehicle_name_list.currentText()

            deleted_profile = None
            spawning_profiles_to_delete = []

            for profile in vehicle_profiles:
                name = profile.get_vehicle_profile_name()
                if name == str(self.deleted_vehicle):
                    deleted_profile = profile
                    break

            if deleted_profile is not None:

                for profile in spawning_profiles:
                    if profile.get_vehicle_profile() == deleted_profile:
                        spawning_profiles_to_delete.append(profile)

                for profile in spawning_profiles_to_delete:
                    for i in intersection:
                        for spawn in i.get_spawning_profile_list():
                            if spawn == profile:
                                i.get_spawning_profile_list().remove(spawn)

                for profile in spawning_profiles_to_delete:
                    spawning_profiles.remove(profile)

                vehicle_profiles.remove(deleted_profile)

            #Remaining code in this else if statement is used for testing.
            print(str(len(vehicle_profiles)))

            for profile in vehicle_profiles:
                print(str(profile.get_vehicle_profile_name()) + ' ')

        elif profile_action_type == 4:
            """
            A spawning profile is created and stored in the system. 
            """
            # spawn = SpawningProfile(self.spawn_name.text(), None, None)
            self.vehicle_name_for_spawn = self.vehicle_for_spawn.currentText()
            self.driver_name_for_spawn = self.driver_for_spawn.currentText()

            selected_driver = None
            selected_vehicle = None

            for profile in driver_profiles:
                name = profile.get_driver_profile_name()
                if name == str(self.driver_name_for_spawn):
                    selected_driver = profile
                    break

            for vprofile in vehicle_profiles:
                name = vprofile.get_vehicle_profile_name()
                if name == str(self.vehicle_name_for_spawn):
                    selected_vehicle = vprofile

            name_in_use = False

            for profile in spawning_profiles:
                if profile.get_spawning_profile_name() == self.spawn_name.text():
                    name_in_use = True
                    break


            if (self.spawn_name.text() != '') & (not name_in_use):
                spawning_profile = SpawningProfile(self.spawn_name.text(), selected_driver, selected_vehicle)
                spawning_profiles.append(spawning_profile)

            #Remaining code in this else if statement is used for testing.
            print(str(len(spawning_profiles)))

            for profile in spawning_profiles:
                print(str(profile.get_spawning_profile_name()) + ' ')

        elif profile_action_type == 5:
            """
            A spawning profile is deleted. Intersections will also remove the spawning profile from their list of
            connected spawning profiles. 
            """
            self.deleted_spawn = self.spawn_name_list.currentText()

            deleted_profile = None

            for profile in spawning_profiles:
                name = profile.get_spawning_profile_name()
                if name == str(self.deleted_spawn):
                    deleted_profile = profile
                    break

            if deleted_profile is not None:

                for i in intersection:
                    for profile in i.get_spawning_profile_list():
                        if profile == deleted_profile:
                         i.get_spawning_profile_list().remove(profile)

                spawning_profiles.remove(deleted_profile)

            # Remaining code in this else if statement is used for testing.
            print(str(len(spawning_profiles)))

            for profile in spawning_profiles:
                print(str(profile.get_spawning_profile_name()) + ' ')

        elif profile_action_type == 6:
            """
            This section connects a spawning profile to an intersection.
            """
            self.intersection_add_spawn = self.add_spawn_intersection.currentText()

            added_profile = None

            for profile in spawning_profiles:
                name = profile.get_spawning_profile_name()
                if name == str(self.intersection_add_spawn):
                    added_profile = profile


            name_in_use = False

            for profile in selected_object.get_spawning_profile_list():
                if profile.get_spawning_profile_name() == self.intersection_add_spawn:
                    name_in_use = True
                    break

            if (added_profile is not None) & (not name_in_use):
                selected_object.add_spawning_profile(added_profile)

        else:
            """
            This section removes a spawning profile form an intersection
            """
            self.intersection_deleted_spawn = self.delete_spawn_intersection.currentText()

            profile_to_delete = None

            for profile in spawning_profiles:
                name = profile.get_spawning_profile_name()
                if name == str(self.intersection_deleted_spawn):
                    profile_to_delete = profile

            if profile_to_delete is not None:
                selected_object.remove_spawning_profile(profile_to_delete)

        # print('num driver profiles = ' + str(len(driver_profiles)))

        # print('driver profile name = ' + driver_profiles[0].get_driver_profile_name())
        # print('num vehicle profiles = ' + str(len(vehicle_profiles)))

        self.close()


class EditDialog(QDialog):
    global road
    global intersection
    global driver_profiles
    global vehicle_profiles

    radius = None
    in_lanes = None
    out_lanes = None
    speed_limit = None
    intersection_speed = None
    # road_name = None

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
        global testing

        layout = QFormLayout()

        if type(selected_object) is Intersection:
            self.formGroupBox = QGroupBox("Intersection")
            self.radius = QSpinBox(self)
            self.radius.setMinimum(1)
            self.radius.setMaximum(100)
            self.radius.setValue(selected_object.radius)
            if testing:
                self.radius.setValue(90)
            layout.addRow(QLabel("Radius:"), self.radius)
            self.intersection_speed = QSpinBox(self)
            self.intersection_speed.setMinimum(10)
            self.intersection_speed.setMaximum(50)
            self.intersection_speed.setValue(selected_object.speed_limit)
            layout.addRow(QLabel("Speed Limit:"), self.intersection_speed)

        else:
            self.formGroupBox = QGroupBox("Road")
            # self.road_name = QLineEdit(self)
            # self.road_name.insert('example_name')
            self.in_lanes = QSpinBox(self)
            self.in_lanes.setMinimum(0)
            self.in_lanes.setMaximum(10)
            self.in_lanes.setValue(selected_object.in_lanes)
            self.out_lanes = QSpinBox(self)
            self.out_lanes.setMinimum(0)
            self.out_lanes.setMaximum(10)
            self.out_lanes.setValue(selected_object.out_lanes)
            if testing:
                self.in_lanes.setValue(3)
                self.out_lanes.setValue(2)

            # layout.addRow(QLabel("Road Name:"), self.road_name)
            layout.addRow(QLabel("In Lanes:"), self.in_lanes)
            layout.addRow(QLabel("Out Lanes:"), self.out_lanes)
            self.speed_limit = QSpinBox(self)
            self.speed_limit.setMinimum(20)
            self.speed_limit.setMaximum(75)
            self.speed_limit.setValue(selected_object.speed_limit)
            layout.addRow(QLabel("Speed Limit (km/hr):"), self.speed_limit)

        self.formGroupBox.setLayout(layout)

    def accept(self):
        global selected_object
        if type(selected_object) is Intersection:
            selected_object.radius = self.radius.value()
            selected_object.speed_limit = self.intersection_speed.value()
        else:
            selected_object.in_lanes = self.in_lanes.value()
            selected_object.out_lanes = self.out_lanes.value()
            selected_object.speed_limit = self.speed_limit.value()
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
    speed_limit = None
    intersection_speed_limit = None
    road_name = None

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
            self.intersection_speed_limit = QSpinBox(self)
            self.intersection_speed_limit.setMinimum(10)
            self.intersection_speed_limit.setMaximum(50)
            self.intersection_speed_limit.setValue(25)
            layout.addRow(QLabel("Speed Limit (km/hr):"), self.intersection_speed_limit)

        else:
            self.formGroupBox = QGroupBox("Add Road")
            self.road_name = QLineEdit(self)
            self.road_name.insert('example_name')
            layout.addRow(QLabel("Road Name:"), self.road_name)
            self.angle = QSpinBox(self)
            self.angle.setMinimum(0)
            self.angle.setMaximum(360)
            self.angle.setValue(0)
            layout.addRow(QLabel("Angle:"), self.angle)
            self.radius = QSpinBox(self)
            self.radius.setMinimum(10)
            self.radius.setMaximum(400)
            self.radius.setValue(100)
            layout.addRow(QLabel("Length:"), self.radius)
            self.in_lanes = QSpinBox(self)
            self.in_lanes.setMinimum(0)
            self.in_lanes.setMaximum(10)
            self.in_lanes.setValue(3)
            self.out_lanes = QSpinBox(self)
            self.out_lanes.setMinimum(0)
            self.out_lanes.setMaximum(10)
            self.out_lanes.setValue(3)
            layout.addRow(QLabel("In Lanes:"), self.in_lanes)
            layout.addRow(QLabel("Out Lanes:"), self.out_lanes)
            self.speed_limit = QSpinBox(self)
            self.speed_limit.setMinimum(20)
            self.speed_limit.setMaximum(75)
            self.speed_limit.setValue(35)
            layout.addRow(QLabel("Speed Limit (km/hr): "), self.speed_limit)

        self.formGroupBox.setLayout(layout)

    def accept(self):
        global selected_object
        if type(selected_object) is Road:
            if self.add_position.currentText() == "End":
                intersection.append(selected_object.generate_end_connection(self.radius.value(),
                                                                            self.intersection_speed_limit.value()))
            else:
                intersection.append(selected_object.generate_start_connection(self.radius.value(),
                                                                              self.intersection_speed_limit.value()))
        else:
            road.append(selected_object.add_connection(self.angle.value() * math.pi / 180, self.radius.value(),
                                           self.in_lanes.value(), self.out_lanes.value(), self.speed_limit.value(),
                                                       self.road_name.text()))

        self.close()


class YellowDialog(QDialog):
    global intersection

    yellow_length = None

    def __init__(self):
        super(YellowDialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Stop Light")

    def createFormGroupBox(self):
        global selected_object
        layout = QFormLayout()

        self.formGroupBox = QGroupBox("Yellow Light")
        self.yellow_length = QSpinBox(self)
        self.yellow_length.setMinimum(1000)
        self.yellow_length.setMaximum(8000)
        self.yellow_length.setValue(selected_object.yellow_light_length)
        layout.addRow(QLabel("Time Length:"), self.yellow_length)

        self.formGroupBox.setLayout(layout)

    def accept(self):
        global selected_object

        selected_object.set_yellow_length(self.yellow_length.value())

        self.close()


class AddCycleDialog(QDialog):
    global intersection

    name = None
    roads = []
    time = None

    def __init__(self):
        super(AddCycleDialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Stop Light")

    def createFormGroupBox(self):
        global selected_object
        layout = QFormLayout()

        self.roads = []

        self.formGroupBox = QGroupBox("Add New Cycle")
        self.name = QLineEdit(self)
        self.name.insert("New Cycle")
        layout.addRow(QLabel("Name:"), self.name)

        self.time = QSpinBox(self)
        self.time.setMinimum(5000)
        self.time.setMaximum(60000)
        self.time.setValue(10000)
        layout.addRow(QLabel("Light Time:"), self.time)

        i = 0

        for r in selected_object.connections:
            self.roads.append(QCheckBox(str(i)))
            self.roads[i].setChecked(False)
            layout.addRow(QLabel("Connection: "), self.roads[i])
            i = i + 1

        self.formGroupBox.setLayout(layout)

    def accept(self):
        global selected_object

        r = []
        i = 0

        for road_widget in self.roads:
            if road_widget.isChecked():
                r.append(i)
            i = i + 1

        # if no roads are selected for cycle, do not add cycle!
        if len(r) != 0:
            selected_object.add_cycle(self.name.text(), r, self.time.value())

        self.close()


class TestClass:

    def setup(self):
        global app

        app = QApplication(sys.argv)
        mb = MapBuilder()
        mb.first_road()

    def map_builder_start(self):
        global intersection

        self.setup()

        return intersection

    def add_dialog_road(self):
        global selected_object
        global road
        global intersection

        selected_object = intersection[0]

        dialog = AddDialog()
        dialog.accept()

        return road

    def edit_dialog_road(self):
        global selected_object
        global road
        global testing

        testing = True

        selected_object = road[0]

        dialog = EditDialog()
        dialog.accept()

        return selected_object

    def add_dialog_intersection(self):
        global selected_object
        global road
        global intersection

        selected_object = road[0]

        dialog = AddDialog()
        dialog.accept()

        return intersection

    def edit_dialog_intersection(self):
        global selected_object
        global road
        global testing

        testing = True

        selected_object = intersection[0]

        dialog = EditDialog()
        dialog.accept()

        return selected_object


    def get_empty_driver_profile_list(self):
        global driver_profiles

        return driver_profiles


    def get_empty_vehicle_profile_list(self):
        global vehicle_profiles

        return vehicle_profiles


    def populate_driver_profile_list(self):
        global profile_action_type
        global driver_profiles

        profile_action_type = 0

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return driver_profiles


    def populate_vehicle_profile_list(self):
        global profile_action_type
        global vehicle_profiles

        profile_action_type = 1

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return vehicle_profiles

    def delete_driver_profile(self):
        global profile_action_type
        global driver_profiles

        profile_action_type = 2

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return driver_profiles

    def delete_vehicle_profile(self):
        global  profile_action_type
        global  vehicle_profiles

        profile_action_type = 3

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return vehicle_profiles

    def populate_spawning_profile_list(self):
        global profile_action_type
        global vehicle_profiles
        global driver_profiles
        global spawning_profiles

        profile_action_type = 4

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return spawning_profiles

    def delete_spawning_profile(self):
        global profile_action_type
        global vehicle_profiles
        global driver_profiles
        global spawning_profiles

        profile_action_type = 5

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return spawning_profiles

    def add_spawning_profile_to_intersection(self):
        global intersection
        global profile_action_type

        profile_action_type = 6

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return intersection

    def delete_spawning_profile_from_intersection(self):
        global intersection
        global profile_action_type

        profile_action_type = 7

        pd = ProfileDialog()
        pd.createFormGroupBox()
        pd.accept()

        return intersection

    def connect_intersections(self):
        global intersection
        global selected_object

        selected_object = intersection[0]

        cd = ConnectDialog()
        cd.createFormGroupBox()
        cd.accept()

        return selected_object


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    mb.first_road()
    sys.exit(app.exec_())
