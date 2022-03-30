import sys
import asyncio

from PySide2.QtWidgets import QApplication
from asyncqt import QEventLoop

from pywordle.view.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    with loop:
        sys.exit(loop.run_forever())


if __name__ == '__main__':
    main()
