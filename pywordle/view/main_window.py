from PySide2.QtWidgets import QMainWindow, QWidget

from pywordle.view.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setupUi(self)
