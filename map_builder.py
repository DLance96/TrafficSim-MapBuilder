import sys

from PyQt5.QtWidgets import QApplication, QAction, QMainWindow


class MapBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MapBuilder()
    sys.exit(app.exec_())