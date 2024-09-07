# create Pyside6 crash test
import sys
from PySide6.QtWidgets import QApplication
from controller.crash_test_controller import CrashController
import time
if __name__ == '__main__':
    app = QApplication(sys.argv)
    crash_controller = CrashController()
    crash_controller.show_login()
    app.exec()

