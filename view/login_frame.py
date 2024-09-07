# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1320, 900)
        login.setMinimumSize(QSize(1320, 900))
        login.setMaximumSize(QSize(1320, 900))
        login.setStyleSheet(u"background:rgb(255, 238, 172)")
        self.login_main = QWidget(login)
        self.login_main.setObjectName(u"login_main")
        self.login_frame = QFrame(self.login_main)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setGeometry(QRect(410, 300, 500, 300))
        self.login_frame.setMinimumSize(QSize(500, 300))
        self.login_frame.setMaximumSize(QSize(500, 300))
        self.login_frame.setStyleSheet(u"background:rgb(167, 224, 255)")
        self.login_frame.setFrameShape(QFrame.Shape.Box)
        self.login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.login_frame.setLineWidth(3)
        self.user_label = QLabel(self.login_frame)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setGeometry(QRect(220, 15, 61, 51))
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(24)
        font.setBold(True)
        self.user_label.setFont(font)
        self.user_lineEdit = QLineEdit(self.login_frame)
        self.user_lineEdit.setObjectName(u"user_lineEdit")
        self.user_lineEdit.setGeometry(QRect(90, 65, 321, 41))
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.user_lineEdit.setFont(font1)
        self.user_lineEdit.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.user_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_label = QLabel(self.login_frame)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(190, 110, 121, 51))
        self.password_label.setFont(font)
        self.passwrod_lineEdit = QLineEdit(self.login_frame)
        self.passwrod_lineEdit.setObjectName(u"passwrod_lineEdit")
        self.passwrod_lineEdit.setGeometry(QRect(90, 165, 321, 41))
        self.passwrod_lineEdit.setFont(font1)
        self.passwrod_lineEdit.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.passwrod_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwrod_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.login_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 230, 181, 51))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background:rgb(72, 216, 0)")
        login.setCentralWidget(self.login_main)
        self.statusbar = QStatusBar(login)
        self.statusbar.setObjectName(u"statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"LOGIN", None))
        self.user_label.setText(QCoreApplication.translate("login", u"USER", None))
        self.password_label.setText(QCoreApplication.translate("login", u"PASSWORD", None))
        self.passwrod_lineEdit.setInputMask("")
        self.pushButton.setText(QCoreApplication.translate("login", u"LOGIN", None))
    # retranslateUi

