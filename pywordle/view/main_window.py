"""The main window widget"""

from PySide2.QtWidgets import QMainWindow, QWidget

from pywordle.view.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window widget."""

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setupUi(self)
