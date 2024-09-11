# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1320, 900)
        MainWindow.setMinimumSize(QSize(1320, 900))
        MainWindow.setMaximumSize(QSize(1320, 900))
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(20)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background:rgb(255, 238, 172)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.data_output_frame = QFrame(self.centralwidget)
        self.data_output_frame.setObjectName(u"data_output_frame")
        self.data_output_frame.setGeometry(QRect(10, 89, 1120, 781))
        self.data_output_frame.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.data_output_frame.setFrameShape(QFrame.Shape.Box)
        self.data_output_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.data_output_frame.setLineWidth(3)
        self.comport_label = QLabel(self.centralwidget)
        self.comport_label.setObjectName(u"comport_label")
        self.comport_label.setGeometry(QRect(20, 20, 101, 41))
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.comport_label.setFont(font1)
        self.comport_comboBox = QComboBox(self.centralwidget)
        self.comport_comboBox.addItem("")
        self.comport_comboBox.setObjectName(u"comport_comboBox")
        self.comport_comboBox.setGeometry(QRect(140, 20, 191, 41))
        font2 = QFont()
        font2.setFamilies([u"TH Niramit AS"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.comport_comboBox.setFont(font2)
        self.comport_comboBox.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.connect_pushButton = QPushButton(self.centralwidget)
        self.connect_pushButton.setObjectName(u"connect_pushButton")
        self.connect_pushButton.setGeometry(QRect(350, 15, 191, 51))
        self.connect_pushButton.setFont(font2)
        self.connect_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aaff7f, stop: 1 #aaff7f);")
        self.weight_label = QLabel(self.centralwidget)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setGeometry(QRect(790, 20, 141, 41))
        self.weight_label.setFont(font1)
        self.weight_lineEdit = QLineEdit(self.centralwidget)
        self.weight_lineEdit.setObjectName(u"weight_lineEdit")
        self.weight_lineEdit.setGeometry(QRect(950, 20, 131, 41))
        self.weight_lineEdit.setFont(font2)
        self.weight_lineEdit.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.weight_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weight_unit_label = QLabel(self.centralwidget)
        self.weight_unit_label.setObjectName(u"weight_unit_label")
        self.weight_unit_label.setGeometry(QRect(1100, 20, 41, 41))
        self.weight_unit_label.setFont(font1)
        self.set_zero_pushButton = QPushButton(self.centralwidget)
        self.set_zero_pushButton.setObjectName(u"set_zero_pushButton")
        self.set_zero_pushButton.setGeometry(QRect(1150, 15, 161, 51))
        self.set_zero_pushButton.setFont(font2)
        self.set_zero_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0000ff, stop: 1 #ffffff);")
        self.set_zero_pushButton.setAutoRepeatDelay(300)
        self.set_zero_pushButton.setAutoRepeatInterval(100)
        self.start_pushButton = QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setGeometry(QRect(1150, 100, 161, 51))
        self.start_pushButton.setFont(font2)
        self.start_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #62c300, stop: 1 #ffffff);")
        self.stop_pushButton = QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        self.stop_pushButton.setGeometry(QRect(1150, 190, 161, 51))
        self.stop_pushButton.setFont(font2)
        self.stop_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff0000, stop: 1 #ffffff);")
        self.stop_pushButton.setCheckable(False)
        self.stop_pushButton.setChecked(False)
        self.stop_pushButton.setAutoRepeat(False)
        self.stop_pushButton.setAutoExclusive(False)
        self.stop_pushButton.setAutoDefault(False)
        self.stop_pushButton.setFlat(False)
        self.save_pushButton = QPushButton(self.centralwidget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setGeometry(QRect(1150, 280, 161, 51))
        self.save_pushButton.setFont(font2)
        self.save_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00ffff, stop: 1 #ffffff);")
        self.logout_pushButton = QPushButton(self.centralwidget)
        self.logout_pushButton.setObjectName(u"logout_pushButton")
        self.logout_pushButton.setGeometry(QRect(1150, 820, 161, 51))
        self.logout_pushButton.setFont(font2)
        self.logout_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #000000, stop: 1 #ffffff);")
        self.disconnect_pushButton = QPushButton(self.centralwidget)
        self.disconnect_pushButton.setObjectName(u"disconnect_pushButton")
        self.disconnect_pushButton.setGeometry(QRect(560, 15, 191, 51))
        self.disconnect_pushButton.setFont(font2)
        self.disconnect_pushButton.setStyleSheet(u"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aefeff, stop: 1 #aefeff);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stop_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comport_label.setText(QCoreApplication.translate("MainWindow", u"COMPORT", None))
        self.comport_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"NONE", None))

        self.connect_pushButton.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.weight_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e1b\u0e31\u0e08\u0e08\u0e38\u0e1a\u0e31\u0e19", None))
        self.weight_unit_label.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.set_zero_pushButton.setText(QCoreApplication.translate("MainWindow", u"SET ZERO", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.save_pushButton.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.logout_pushButton.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.disconnect_pushButton.setText(QCoreApplication.translate("MainWindow", u"DISCONNECT", None))
    # retranslateUi

