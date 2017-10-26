import sys
from src.map.road import Road
from src.map.coordinates import Coordinates
from src.map.intersection import Intersection

from PyQt5.QtWidgets import QApplication, QWidget, QAction, QMainWindow, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, QtCore


class MapBuilder(QMainWindow):
    start_coord_to_obj = {}
    roads = []
    intersections = []

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

        # buttons
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 440)
        button.clicked.connect(self.add_road)

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

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

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        for obj in self.roads:
            self.draw_road(obj.get_points(), qp)
        qp.end()

    def first_road(self):
        leng = 100
        start_coord = Coordinates(100 - (leng / 2), 140)
        r = Road(start_coord, leng, 1, 1)
        self.roads.append(r)
        self.start_coord_to_obj.update({str(50) + ' ' + str(140): r})
        self.update()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        converted_position = Coordinates(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        for obj in self.roads:
            if obj.is_on_road(converted_position):
                self.adds_road(obj)
                break

    @pyqtSlot()
    def add_road(self):
        prevr = self.roads[self.roads.__len__()-1]

        # self.sender().deleteLater()
        button2 = QPushButton('NEW', self)
        button2.setToolTip('This is an NEW button')
        leng = 100
        button2.move(prevr.get_end_coords().x + (leng/2), 440)
        start_coord = prevr.get_end_coords()
        r = Road(start_coord, leng, 1, 1)
        self.roads.append(r)
        self.start_coord_to_obj.update({str(start_coord.x) + ' ' + str(start_coord.y): r})
        button2.clicked.connect(self.add_road)

        self.x += 20
        # self.layout().addWidget(button2)
        self.update()

    def adds_road(self, prevr):
        # self.sender().deleteLater()
        button2 = QPushButton('NEW', self)
        button2.setToolTip('This is an NEW button')
        leng = 100
        button2.move(prevr.get_end_coords().x + (leng / 2), 440)
        start_coord = prevr.get_end_coords()
        r = Road(start_coord, leng, 1, 1)
        self.roads.append(r)
        self.start_coord_to_obj.update({str(start_coord.x) + ' ' + str(start_coord.y): r})
        button2.clicked.connect(self.add_road)

        self.x = self.x + 20
        # self.layout().addWidget(button2)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    mb.first_road()
    sys.exit(app.exec_())
