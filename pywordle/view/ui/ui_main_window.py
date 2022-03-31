# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(658, 779)
        MainWindow.setStyleSheet(u"background-color: white;")
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName(u"action_Close")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 40)
        self.frame_run_1 = QFrame(self.centralwidget)
        self.frame_run_1.setObjectName(u"frame_run_1")
        self.frame_run_1.setLineWidth(0)
        self.gridLayout_run1 = QGridLayout(self.frame_run_1)
        self.gridLayout_run1.setSpacing(10)
        self.gridLayout_run1.setObjectName(u"gridLayout_run1")
        self.gridLayout_run1.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1_4 = QPushButton(self.frame_run_1)
        self.pushButton_1_4.setObjectName(u"pushButton_1_4")
        self.pushButton_1_4.setMinimumSize(QSize(60, 60))
        self.pushButton_1_4.setMaximumSize(QSize(60, 60))
        self.pushButton_1_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_1_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run1.addWidget(self.pushButton_1_4, 0, 3, 1, 1)

        self.pushButton_1_5 = QPushButton(self.frame_run_1)
        self.pushButton_1_5.setObjectName(u"pushButton_1_5")
        self.pushButton_1_5.setMinimumSize(QSize(60, 60))
        self.pushButton_1_5.setMaximumSize(QSize(60, 60))
        self.pushButton_1_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_1_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run1.addWidget(self.pushButton_1_5, 0, 4, 1, 1)

        self.pushButton_1_1 = QPushButton(self.frame_run_1)
        self.pushButton_1_1.setObjectName(u"pushButton_1_1")
        self.pushButton_1_1.setMinimumSize(QSize(60, 60))
        self.pushButton_1_1.setMaximumSize(QSize(60, 60))
        self.pushButton_1_1.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_1_1.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run1.addWidget(self.pushButton_1_1, 0, 0, 1, 1)

        self.pushButton_1_2 = QPushButton(self.frame_run_1)
        self.pushButton_1_2.setObjectName(u"pushButton_1_2")
        self.pushButton_1_2.setMinimumSize(QSize(60, 60))
        self.pushButton_1_2.setMaximumSize(QSize(60, 60))
        self.pushButton_1_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_1_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run1.addWidget(self.pushButton_1_2, 0, 1, 1, 1)

        self.pushButton_1_3 = QPushButton(self.frame_run_1)
        self.pushButton_1_3.setObjectName(u"pushButton_1_3")
        self.pushButton_1_3.setMinimumSize(QSize(60, 60))
        self.pushButton_1_3.setMaximumSize(QSize(60, 60))
        self.pushButton_1_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_1_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run1.addWidget(self.pushButton_1_3, 0, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_run_1)

        self.frame_run_2 = QFrame(self.centralwidget)
        self.frame_run_2.setObjectName(u"frame_run_2")
        self.frame_run_2.setEnabled(False)
        self.frame_run_2.setLineWidth(0)
        self.gridLayout_run2 = QGridLayout(self.frame_run_2)
        self.gridLayout_run2.setSpacing(10)
        self.gridLayout_run2.setObjectName(u"gridLayout_run2")
        self.gridLayout_run2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2_3 = QPushButton(self.frame_run_2)
        self.pushButton_2_3.setObjectName(u"pushButton_2_3")
        self.pushButton_2_3.setMinimumSize(QSize(60, 60))
        self.pushButton_2_3.setMaximumSize(QSize(60, 60))
        self.pushButton_2_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run2.addWidget(self.pushButton_2_3, 0, 2, 1, 1)

        self.pushButton_2_4 = QPushButton(self.frame_run_2)
        self.pushButton_2_4.setObjectName(u"pushButton_2_4")
        self.pushButton_2_4.setMinimumSize(QSize(60, 60))
        self.pushButton_2_4.setMaximumSize(QSize(60, 60))
        self.pushButton_2_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run2.addWidget(self.pushButton_2_4, 0, 3, 1, 1)

        self.pushButton_2_1 = QPushButton(self.frame_run_2)
        self.pushButton_2_1.setObjectName(u"pushButton_2_1")
        self.pushButton_2_1.setMinimumSize(QSize(60, 60))
        self.pushButton_2_1.setMaximumSize(QSize(60, 60))
        self.pushButton_2_1.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2_1.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run2.addWidget(self.pushButton_2_1, 0, 0, 1, 1)

        self.pushButton_2_5 = QPushButton(self.frame_run_2)
        self.pushButton_2_5.setObjectName(u"pushButton_2_5")
        self.pushButton_2_5.setMinimumSize(QSize(60, 60))
        self.pushButton_2_5.setMaximumSize(QSize(60, 60))
        self.pushButton_2_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run2.addWidget(self.pushButton_2_5, 0, 4, 1, 1)

        self.pushButton_2_2 = QPushButton(self.frame_run_2)
        self.pushButton_2_2.setObjectName(u"pushButton_2_2")
        self.pushButton_2_2.setMinimumSize(QSize(60, 60))
        self.pushButton_2_2.setMaximumSize(QSize(60, 60))
        self.pushButton_2_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_run2.addWidget(self.pushButton_2_2, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_run_2)

        self.frame_run_3 = QFrame(self.centralwidget)
        self.frame_run_3.setObjectName(u"frame_run_3")
        self.frame_run_3.setEnabled(False)
        self.frame_run_3.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame_run_3)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3_1 = QPushButton(self.frame_run_3)
        self.pushButton_3_1.setObjectName(u"pushButton_3_1")
        self.pushButton_3_1.setMinimumSize(QSize(60, 60))
        self.pushButton_3_1.setMaximumSize(QSize(60, 60))
        self.pushButton_3_1.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3_1.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3_1, 0, 0, 1, 1)

        self.pushButton_3_2 = QPushButton(self.frame_run_3)
        self.pushButton_3_2.setObjectName(u"pushButton_3_2")
        self.pushButton_3_2.setMinimumSize(QSize(60, 60))
        self.pushButton_3_2.setMaximumSize(QSize(60, 60))
        self.pushButton_3_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3_2, 0, 1, 1, 1)

        self.pushButton_3_3 = QPushButton(self.frame_run_3)
        self.pushButton_3_3.setObjectName(u"pushButton_3_3")
        self.pushButton_3_3.setMinimumSize(QSize(60, 60))
        self.pushButton_3_3.setMaximumSize(QSize(60, 60))
        self.pushButton_3_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3_3, 0, 2, 1, 1)

        self.pushButton_3_4 = QPushButton(self.frame_run_3)
        self.pushButton_3_4.setObjectName(u"pushButton_3_4")
        self.pushButton_3_4.setMinimumSize(QSize(60, 60))
        self.pushButton_3_4.setMaximumSize(QSize(60, 60))
        self.pushButton_3_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3_4, 0, 3, 1, 1)

        self.pushButton_3_5 = QPushButton(self.frame_run_3)
        self.pushButton_3_5.setObjectName(u"pushButton_3_5")
        self.pushButton_3_5.setMinimumSize(QSize(60, 60))
        self.pushButton_3_5.setMaximumSize(QSize(60, 60))
        self.pushButton_3_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3_5, 0, 4, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_run_3)

        self.frame_run_4 = QFrame(self.centralwidget)
        self.frame_run_4.setObjectName(u"frame_run_4")
        self.frame_run_4.setEnabled(False)
        self.frame_run_4.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame_run_4)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4_4 = QPushButton(self.frame_run_4)
        self.pushButton_4_4.setObjectName(u"pushButton_4_4")
        self.pushButton_4_4.setMinimumSize(QSize(60, 60))
        self.pushButton_4_4.setMaximumSize(QSize(60, 60))
        self.pushButton_4_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_4_4, 0, 3, 1, 1)

        self.pushButton_4_3 = QPushButton(self.frame_run_4)
        self.pushButton_4_3.setObjectName(u"pushButton_4_3")
        self.pushButton_4_3.setMinimumSize(QSize(60, 60))
        self.pushButton_4_3.setMaximumSize(QSize(60, 60))
        self.pushButton_4_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_4_3, 0, 2, 1, 1)

        self.pushButton_4_1 = QPushButton(self.frame_run_4)
        self.pushButton_4_1.setObjectName(u"pushButton_4_1")
        self.pushButton_4_1.setMinimumSize(QSize(60, 60))
        self.pushButton_4_1.setMaximumSize(QSize(60, 60))
        self.pushButton_4_1.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4_1.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_4_1, 0, 0, 1, 1)

        self.pushButton_4_2 = QPushButton(self.frame_run_4)
        self.pushButton_4_2.setObjectName(u"pushButton_4_2")
        self.pushButton_4_2.setMinimumSize(QSize(60, 60))
        self.pushButton_4_2.setMaximumSize(QSize(60, 60))
        self.pushButton_4_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_4_2, 0, 1, 1, 1)

        self.pushButton_4_5 = QPushButton(self.frame_run_4)
        self.pushButton_4_5.setObjectName(u"pushButton_4_5")
        self.pushButton_4_5.setMinimumSize(QSize(60, 60))
        self.pushButton_4_5.setMaximumSize(QSize(60, 60))
        self.pushButton_4_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_4_5, 0, 4, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_run_4)

        self.frame_run_5 = QFrame(self.centralwidget)
        self.frame_run_5.setObjectName(u"frame_run_5")
        self.frame_run_5.setEnabled(False)
        self.frame_run_5.setLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.frame_run_5)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5_3 = QPushButton(self.frame_run_5)
        self.pushButton_5_3.setObjectName(u"pushButton_5_3")
        self.pushButton_5_3.setMinimumSize(QSize(60, 60))
        self.pushButton_5_3.setMaximumSize(QSize(60, 60))
        self.pushButton_5_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_5_3, 0, 2, 1, 1)

        self.pushButton_5_4 = QPushButton(self.frame_run_5)
        self.pushButton_5_4.setObjectName(u"pushButton_5_4")
        self.pushButton_5_4.setMinimumSize(QSize(60, 60))
        self.pushButton_5_4.setMaximumSize(QSize(60, 60))
        self.pushButton_5_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_5_4, 0, 3, 1, 1)

        self.pushButton_5_1 = QPushButton(self.frame_run_5)
        self.pushButton_5_1.setObjectName(u"pushButton_5_1")
        self.pushButton_5_1.setMinimumSize(QSize(60, 60))
        self.pushButton_5_1.setMaximumSize(QSize(60, 60))
        self.pushButton_5_1.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5_1.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_5_1, 0, 0, 1, 1)

        self.pushButton_5_5 = QPushButton(self.frame_run_5)
        self.pushButton_5_5.setObjectName(u"pushButton_5_5")
        self.pushButton_5_5.setMinimumSize(QSize(60, 60))
        self.pushButton_5_5.setMaximumSize(QSize(60, 60))
        self.pushButton_5_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_5_5, 0, 4, 1, 1)

        self.pushButton_5_2 = QPushButton(self.frame_run_5)
        self.pushButton_5_2.setObjectName(u"pushButton_5_2")
        self.pushButton_5_2.setMinimumSize(QSize(60, 60))
        self.pushButton_5_2.setMaximumSize(QSize(60, 60))
        self.pushButton_5_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton_5_2, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_run_5)

        self.frame_run_6 = QFrame(self.centralwidget)
        self.frame_run_6.setObjectName(u"frame_run_6")
        self.frame_run_6.setEnabled(False)
        self.frame_run_6.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.frame_run_6)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6_1 = QPushButton(self.frame_run_6)
        self.pushButton_6_1.setObjectName(u"pushButton_6_1")
        self.pushButton_6_1.setMinimumSize(QSize(60, 60))
        self.pushButton_6_1.setMaximumSize(QSize(60, 60))
        self.pushButton_6_1.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_6_1.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_6_1, 0, 0, 1, 1)

        self.pushButton_6_5 = QPushButton(self.frame_run_6)
        self.pushButton_6_5.setObjectName(u"pushButton_6_5")
        self.pushButton_6_5.setMinimumSize(QSize(60, 60))
        self.pushButton_6_5.setMaximumSize(QSize(60, 60))
        self.pushButton_6_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_6_5.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_6_5, 0, 4, 1, 1)

        self.pushButton_6_4 = QPushButton(self.frame_run_6)
        self.pushButton_6_4.setObjectName(u"pushButton_6_4")
        self.pushButton_6_4.setMinimumSize(QSize(60, 60))
        self.pushButton_6_4.setMaximumSize(QSize(60, 60))
        self.pushButton_6_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_6_4.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_6_4, 0, 3, 1, 1)

        self.pushButton_6_3 = QPushButton(self.frame_run_6)
        self.pushButton_6_3.setObjectName(u"pushButton_6_3")
        self.pushButton_6_3.setMinimumSize(QSize(60, 60))
        self.pushButton_6_3.setMaximumSize(QSize(60, 60))
        self.pushButton_6_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_6_3.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_6_3, 0, 2, 1, 1)

        self.pushButton_6_2 = QPushButton(self.frame_run_6)
        self.pushButton_6_2.setObjectName(u"pushButton_6_2")
        self.pushButton_6_2.setMinimumSize(QSize(60, 60))
        self.pushButton_6_2.setMaximumSize(QSize(60, 60))
        self.pushButton_6_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_6_2.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"font-size: 26pt;\n"
"}\n"
"\n"
"QPushButton:focus\n"
"{\n"
"background-color: white;\n"
"border: 2px solid black;\n"
"}")

        self.gridLayout_4.addWidget(self.pushButton_6_2, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_run_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame_inputs = QFrame(self.centralwidget)
        self.frame_inputs.setObjectName(u"frame_inputs")
        self.horizontalLayout = QHBoxLayout(self.frame_inputs)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.pushButton_Q = QPushButton(self.frame_inputs)
        self.pushButton_Q.setObjectName(u"pushButton_Q")
        self.pushButton_Q.setMinimumSize(QSize(50, 50))
        self.pushButton_Q.setMaximumSize(QSize(50, 50))
        self.pushButton_Q.setFocusPolicy(Qt.NoFocus)
        self.pushButton_Q.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_Q)

        self.pushButton_W = QPushButton(self.frame_inputs)
        self.pushButton_W.setObjectName(u"pushButton_W")
        self.pushButton_W.setMinimumSize(QSize(50, 50))
        self.pushButton_W.setMaximumSize(QSize(50, 50))
        self.pushButton_W.setFocusPolicy(Qt.NoFocus)
        self.pushButton_W.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_W)

        self.pushButton_E = QPushButton(self.frame_inputs)
        self.pushButton_E.setObjectName(u"pushButton_E")
        self.pushButton_E.setMinimumSize(QSize(50, 50))
        self.pushButton_E.setMaximumSize(QSize(50, 50))
        self.pushButton_E.setFocusPolicy(Qt.NoFocus)
        self.pushButton_E.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_E)

        self.pushButton_R = QPushButton(self.frame_inputs)
        self.pushButton_R.setObjectName(u"pushButton_R")
        self.pushButton_R.setMinimumSize(QSize(50, 50))
        self.pushButton_R.setMaximumSize(QSize(50, 50))
        self.pushButton_R.setFocusPolicy(Qt.NoFocus)
        self.pushButton_R.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_R)

        self.pushButton_T = QPushButton(self.frame_inputs)
        self.pushButton_T.setObjectName(u"pushButton_T")
        self.pushButton_T.setMinimumSize(QSize(50, 50))
        self.pushButton_T.setMaximumSize(QSize(50, 50))
        self.pushButton_T.setFocusPolicy(Qt.NoFocus)
        self.pushButton_T.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_T)

        self.pushButton_Z = QPushButton(self.frame_inputs)
        self.pushButton_Z.setObjectName(u"pushButton_Z")
        self.pushButton_Z.setMinimumSize(QSize(50, 50))
        self.pushButton_Z.setMaximumSize(QSize(50, 50))
        self.pushButton_Z.setFocusPolicy(Qt.NoFocus)
        self.pushButton_Z.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_Z)

        self.pushButton_U = QPushButton(self.frame_inputs)
        self.pushButton_U.setObjectName(u"pushButton_U")
        self.pushButton_U.setMinimumSize(QSize(50, 50))
        self.pushButton_U.setMaximumSize(QSize(50, 50))
        self.pushButton_U.setFocusPolicy(Qt.NoFocus)
        self.pushButton_U.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_U)

        self.pushButton_I = QPushButton(self.frame_inputs)
        self.pushButton_I.setObjectName(u"pushButton_I")
        self.pushButton_I.setMinimumSize(QSize(50, 50))
        self.pushButton_I.setMaximumSize(QSize(50, 50))
        self.pushButton_I.setFocusPolicy(Qt.NoFocus)
        self.pushButton_I.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_I)

        self.pushButton_O = QPushButton(self.frame_inputs)
        self.pushButton_O.setObjectName(u"pushButton_O")
        self.pushButton_O.setMinimumSize(QSize(50, 50))
        self.pushButton_O.setMaximumSize(QSize(50, 50))
        self.pushButton_O.setFocusPolicy(Qt.NoFocus)
        self.pushButton_O.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_O)

        self.pushButton_P = QPushButton(self.frame_inputs)
        self.pushButton_P.setObjectName(u"pushButton_P")
        self.pushButton_P.setMinimumSize(QSize(50, 50))
        self.pushButton_P.setMaximumSize(QSize(50, 50))
        self.pushButton_P.setFocusPolicy(Qt.NoFocus)
        self.pushButton_P.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_P)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_A = QPushButton(self.frame_inputs)
        self.pushButton_A.setObjectName(u"pushButton_A")
        self.pushButton_A.setMinimumSize(QSize(50, 50))
        self.pushButton_A.setMaximumSize(QSize(50, 50))
        self.pushButton_A.setFocusPolicy(Qt.NoFocus)
        self.pushButton_A.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_A)

        self.pushButton_S = QPushButton(self.frame_inputs)
        self.pushButton_S.setObjectName(u"pushButton_S")
        self.pushButton_S.setMinimumSize(QSize(50, 50))
        self.pushButton_S.setMaximumSize(QSize(50, 50))
        self.pushButton_S.setFocusPolicy(Qt.NoFocus)
        self.pushButton_S.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_S)

        self.pushButton_D = QPushButton(self.frame_inputs)
        self.pushButton_D.setObjectName(u"pushButton_D")
        self.pushButton_D.setMinimumSize(QSize(50, 50))
        self.pushButton_D.setMaximumSize(QSize(50, 50))
        self.pushButton_D.setFocusPolicy(Qt.NoFocus)
        self.pushButton_D.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_D)

        self.pushButton_F = QPushButton(self.frame_inputs)
        self.pushButton_F.setObjectName(u"pushButton_F")
        self.pushButton_F.setMinimumSize(QSize(50, 50))
        self.pushButton_F.setMaximumSize(QSize(50, 50))
        self.pushButton_F.setFocusPolicy(Qt.NoFocus)
        self.pushButton_F.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_F)

        self.pushButton_G = QPushButton(self.frame_inputs)
        self.pushButton_G.setObjectName(u"pushButton_G")
        self.pushButton_G.setMinimumSize(QSize(50, 50))
        self.pushButton_G.setMaximumSize(QSize(50, 50))
        self.pushButton_G.setFocusPolicy(Qt.NoFocus)
        self.pushButton_G.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_G)

        self.pushButton_H = QPushButton(self.frame_inputs)
        self.pushButton_H.setObjectName(u"pushButton_H")
        self.pushButton_H.setMinimumSize(QSize(50, 50))
        self.pushButton_H.setMaximumSize(QSize(50, 50))
        self.pushButton_H.setFocusPolicy(Qt.NoFocus)
        self.pushButton_H.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_H)

        self.pushButton_J = QPushButton(self.frame_inputs)
        self.pushButton_J.setObjectName(u"pushButton_J")
        self.pushButton_J.setMinimumSize(QSize(50, 50))
        self.pushButton_J.setMaximumSize(QSize(50, 50))
        self.pushButton_J.setFocusPolicy(Qt.NoFocus)
        self.pushButton_J.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_J)

        self.pushButton_K = QPushButton(self.frame_inputs)
        self.pushButton_K.setObjectName(u"pushButton_K")
        self.pushButton_K.setMinimumSize(QSize(50, 50))
        self.pushButton_K.setMaximumSize(QSize(50, 50))
        self.pushButton_K.setFocusPolicy(Qt.NoFocus)
        self.pushButton_K.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_K)

        self.pushButton_L = QPushButton(self.frame_inputs)
        self.pushButton_L.setObjectName(u"pushButton_L")
        self.pushButton_L.setMinimumSize(QSize(50, 50))
        self.pushButton_L.setMaximumSize(QSize(50, 50))
        self.pushButton_L.setFocusPolicy(Qt.NoFocus)
        self.pushButton_L.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_L)

        self.horizontalSpacer_6 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer_9 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.pushButton_Y = QPushButton(self.frame_inputs)
        self.pushButton_Y.setObjectName(u"pushButton_Y")
        self.pushButton_Y.setMinimumSize(QSize(50, 50))
        self.pushButton_Y.setMaximumSize(QSize(50, 50))
        self.pushButton_Y.setFocusPolicy(Qt.NoFocus)
        self.pushButton_Y.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_Y)

        self.pushButton_X = QPushButton(self.frame_inputs)
        self.pushButton_X.setObjectName(u"pushButton_X")
        self.pushButton_X.setMinimumSize(QSize(50, 50))
        self.pushButton_X.setMaximumSize(QSize(50, 50))
        self.pushButton_X.setFocusPolicy(Qt.NoFocus)
        self.pushButton_X.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_X)

        self.pushButton_C = QPushButton(self.frame_inputs)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setMinimumSize(QSize(50, 50))
        self.pushButton_C.setMaximumSize(QSize(50, 50))
        self.pushButton_C.setFocusPolicy(Qt.NoFocus)
        self.pushButton_C.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_C)

        self.pushButton_V = QPushButton(self.frame_inputs)
        self.pushButton_V.setObjectName(u"pushButton_V")
        self.pushButton_V.setMinimumSize(QSize(50, 50))
        self.pushButton_V.setMaximumSize(QSize(50, 50))
        self.pushButton_V.setFocusPolicy(Qt.NoFocus)
        self.pushButton_V.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_V)

        self.pushButton_B = QPushButton(self.frame_inputs)
        self.pushButton_B.setObjectName(u"pushButton_B")
        self.pushButton_B.setMinimumSize(QSize(50, 50))
        self.pushButton_B.setMaximumSize(QSize(50, 50))
        self.pushButton_B.setFocusPolicy(Qt.NoFocus)
        self.pushButton_B.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_B)

        self.pushButton_N = QPushButton(self.frame_inputs)
        self.pushButton_N.setObjectName(u"pushButton_N")
        self.pushButton_N.setMinimumSize(QSize(50, 50))
        self.pushButton_N.setMaximumSize(QSize(50, 50))
        self.pushButton_N.setFocusPolicy(Qt.NoFocus)
        self.pushButton_N.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_N)

        self.pushButton_M = QPushButton(self.frame_inputs)
        self.pushButton_M.setObjectName(u"pushButton_M")
        self.pushButton_M.setMinimumSize(QSize(50, 50))
        self.pushButton_M.setMaximumSize(QSize(50, 50))
        self.pushButton_M.setFocusPolicy(Qt.NoFocus)
        self.pushButton_M.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_M)

        self.horizontalSpacer_10 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(7, 7, 7, 7)
        self.horizontalSpacer_12 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.pushButton_SEND = QPushButton(self.frame_inputs)
        self.pushButton_SEND.setObjectName(u"pushButton_SEND")
        self.pushButton_SEND.setMinimumSize(QSize(100, 50))
        self.pushButton_SEND.setSizeIncrement(QSize(100, 50))
        self.pushButton_SEND.setFocusPolicy(Qt.NoFocus)
        self.pushButton_SEND.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_SEND)

        self.pushButton_UE = QPushButton(self.frame_inputs)
        self.pushButton_UE.setObjectName(u"pushButton_UE")
        self.pushButton_UE.setMinimumSize(QSize(50, 50))
        self.pushButton_UE.setMaximumSize(QSize(50, 50))
        self.pushButton_UE.setFocusPolicy(Qt.NoFocus)
        self.pushButton_UE.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_UE)

        self.pushButton_OE = QPushButton(self.frame_inputs)
        self.pushButton_OE.setObjectName(u"pushButton_OE")
        self.pushButton_OE.setMinimumSize(QSize(50, 50))
        self.pushButton_OE.setMaximumSize(QSize(50, 50))
        self.pushButton_OE.setFocusPolicy(Qt.NoFocus)
        self.pushButton_OE.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_OE)

        self.pushButton_AE = QPushButton(self.frame_inputs)
        self.pushButton_AE.setObjectName(u"pushButton_AE")
        self.pushButton_AE.setMinimumSize(QSize(50, 50))
        self.pushButton_AE.setMaximumSize(QSize(50, 50))
        self.pushButton_AE.setFocusPolicy(Qt.NoFocus)
        self.pushButton_AE.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_AE)

        self.pushButton_SS = QPushButton(self.frame_inputs)
        self.pushButton_SS.setObjectName(u"pushButton_SS")
        self.pushButton_SS.setMinimumSize(QSize(50, 50))
        self.pushButton_SS.setMaximumSize(QSize(50, 50))
        self.pushButton_SS.setFocusPolicy(Qt.NoFocus)
        self.pushButton_SS.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_SS)

        self.pushButton_DEL = QPushButton(self.frame_inputs)
        self.pushButton_DEL.setObjectName(u"pushButton_DEL")
        self.pushButton_DEL.setMinimumSize(QSize(100, 50))
        self.pushButton_DEL.setSizeIncrement(QSize(100, 50))
        self.pushButton_DEL.setFocusPolicy(Qt.NoFocus)
        self.pushButton_DEL.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: #d0d0d0;\n"
"color: black;\n"
"border: 0px;\n"
"border-radius: 6px;\n"
"font-size: 20pt;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_DEL)

        self.horizontalSpacer_11 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_inputs)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 658, 21))
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.pushButton_Q, self.pushButton_W)
        QWidget.setTabOrder(self.pushButton_W, self.pushButton_E)
        QWidget.setTabOrder(self.pushButton_E, self.pushButton_R)
        QWidget.setTabOrder(self.pushButton_R, self.pushButton_T)
        QWidget.setTabOrder(self.pushButton_T, self.pushButton_Z)
        QWidget.setTabOrder(self.pushButton_Z, self.pushButton_U)
        QWidget.setTabOrder(self.pushButton_U, self.pushButton_I)
        QWidget.setTabOrder(self.pushButton_I, self.pushButton_O)
        QWidget.setTabOrder(self.pushButton_O, self.pushButton_P)
        QWidget.setTabOrder(self.pushButton_P, self.pushButton_A)
        QWidget.setTabOrder(self.pushButton_A, self.pushButton_S)
        QWidget.setTabOrder(self.pushButton_S, self.pushButton_D)
        QWidget.setTabOrder(self.pushButton_D, self.pushButton_F)
        QWidget.setTabOrder(self.pushButton_F, self.pushButton_G)
        QWidget.setTabOrder(self.pushButton_G, self.pushButton_H)
        QWidget.setTabOrder(self.pushButton_H, self.pushButton_J)
        QWidget.setTabOrder(self.pushButton_J, self.pushButton_K)
        QWidget.setTabOrder(self.pushButton_K, self.pushButton_L)
        QWidget.setTabOrder(self.pushButton_L, self.pushButton_Y)
        QWidget.setTabOrder(self.pushButton_Y, self.pushButton_X)
        QWidget.setTabOrder(self.pushButton_X, self.pushButton_C)
        QWidget.setTabOrder(self.pushButton_C, self.pushButton_V)
        QWidget.setTabOrder(self.pushButton_V, self.pushButton_B)
        QWidget.setTabOrder(self.pushButton_B, self.pushButton_N)
        QWidget.setTabOrder(self.pushButton_N, self.pushButton_M)
        QWidget.setTabOrder(self.pushButton_M, self.pushButton_SEND)
        QWidget.setTabOrder(self.pushButton_SEND, self.pushButton_UE)
        QWidget.setTabOrder(self.pushButton_UE, self.pushButton_OE)
        QWidget.setTabOrder(self.pushButton_OE, self.pushButton_AE)
        QWidget.setTabOrder(self.pushButton_AE, self.pushButton_SS)
        QWidget.setTabOrder(self.pushButton_SS, self.pushButton_DEL)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menu_About.addAction(self.actionAbout_Qt)
        self.menu_File.addAction(self.action_Close)

        self.retranslateUi(MainWindow)
        self.action_Close.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyWordle", None))
        self.action_Close.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About &Qt", None))
        self.pushButton_1_4.setText("")
        self.pushButton_1_5.setText("")
        self.pushButton_1_1.setText("")
        self.pushButton_1_2.setText("")
        self.pushButton_1_3.setText("")
        self.pushButton_2_3.setText("")
        self.pushButton_2_4.setText("")
        self.pushButton_2_1.setText("")
#if QT_CONFIG(whatsthis)
        self.pushButton_2_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"QPushButton\n"
"{\n"
"background-color: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"border-radius: 6px;\n"
"}", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_2_5.setText("")
        self.pushButton_2_2.setText("")
        self.pushButton_3_1.setText("")
        self.pushButton_3_2.setText("")
        self.pushButton_3_3.setText("")
        self.pushButton_3_4.setText("")
        self.pushButton_3_5.setText("")
        self.pushButton_4_4.setText("")
        self.pushButton_4_3.setText("")
        self.pushButton_4_1.setText("")
        self.pushButton_4_2.setText("")
        self.pushButton_4_5.setText("")
        self.pushButton_5_3.setText("")
        self.pushButton_5_4.setText("")
        self.pushButton_5_1.setText("")
        self.pushButton_5_5.setText("")
        self.pushButton_5_2.setText("")
        self.pushButton_6_1.setText("")
        self.pushButton_6_5.setText("")
        self.pushButton_6_4.setText("")
        self.pushButton_6_3.setText("")
        self.pushButton_6_2.setText("")
        self.pushButton_Q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.pushButton_W.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.pushButton_E.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.pushButton_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.pushButton_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_U.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.pushButton_I.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.pushButton_O.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.pushButton_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.pushButton_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.pushButton_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_F.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.pushButton_G.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.pushButton_H.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.pushButton_J.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.pushButton_K.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.pushButton_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.pushButton_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_V.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.pushButton_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushButton_N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.pushButton_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.pushButton_SEND.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.pushButton_UE.setText(QCoreApplication.translate("MainWindow", u"\u00dc", None))
        self.pushButton_OE.setText(QCoreApplication.translate("MainWindow", u"\u00d6", None))
        self.pushButton_AE.setText(QCoreApplication.translate("MainWindow", u"\u00c4", None))
        self.pushButton_SS.setText(QCoreApplication.translate("MainWindow", u"\u1e9e", None))
        self.pushButton_DEL.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"&About", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

