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
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 779)
        MainWindow.setStyleSheet("background-color: white;")
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalSpacer = QSpacerItem(
            0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 40)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(60, 60))
        self.pushButton_4.setMaximumSize(QSize(60, 60))
        self.pushButton_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(60, 60))
        self.pushButton_7.setMaximumSize(QSize(60, 60))
        self.pushButton_7.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_7.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(60, 60))
        self.pushButton_30.setMaximumSize(QSize(60, 60))
        self.pushButton_30.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_30.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_30, 7, 4, 1, 1)

        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(60, 60))
        self.pushButton_21.setMaximumSize(QSize(60, 60))
        self.pushButton_21.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_21.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_21, 5, 3, 1, 1)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(60, 60))
        self.pushButton_18.setMaximumSize(QSize(60, 60))
        self.pushButton_18.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_18.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_18, 3, 4, 1, 1)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(60, 60))
        self.pushButton_16.setMaximumSize(QSize(60, 60))
        self.pushButton_16.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_16.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_16, 3, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(60, 60))
        self.pushButton_17.setMaximumSize(QSize(60, 60))
        self.pushButton_17.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_17.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_17, 3, 3, 1, 1)

        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(60, 60))
        self.pushButton_19.setMaximumSize(QSize(60, 60))
        self.pushButton_19.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_19.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_19, 5, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.centralwidget)
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(60, 60))
        self.pushButton_28.setMaximumSize(QSize(60, 60))
        self.pushButton_28.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_28.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_28, 7, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(60, 60))
        self.pushButton_11.setMaximumSize(QSize(60, 60))
        self.pushButton_11.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_11.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(60, 60))
        self.pushButton_12.setMaximumSize(QSize(60, 60))
        self.pushButton_12.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_12.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(60, 60))
        self.pushButton_13.setMaximumSize(QSize(60, 60))
        self.pushButton_13.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_13.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_13, 2, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(60, 60))
        self.pushButton_10.setMaximumSize(QSize(60, 60))
        self.pushButton_10.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_10.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_10, 1, 4, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(60, 60))
        self.pushButton_9.setMaximumSize(QSize(60, 60))
        self.pushButton_9.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_9.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_9, 1, 3, 1, 1)

        self.pushButton_29 = QPushButton(self.centralwidget)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(60, 60))
        self.pushButton_29.setMaximumSize(QSize(60, 60))
        self.pushButton_29.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_29.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_29, 7, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(60, 60))
        self.pushButton_8.setMaximumSize(QSize(60, 60))
        self.pushButton_8.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_8.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(60, 60))
        self.pushButton_20.setMaximumSize(QSize(60, 60))
        self.pushButton_20.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_20.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_20, 5, 2, 1, 1)

        self.pushButton_26 = QPushButton(self.centralwidget)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(60, 60))
        self.pushButton_26.setMaximumSize(QSize(60, 60))
        self.pushButton_26.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_26.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_26, 6, 4, 1, 1)

        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(60, 60))
        self.pushButton_23.setMaximumSize(QSize(60, 60))
        self.pushButton_23.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_23.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_23, 6, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(60, 60))
        self.pushButton_14.setMaximumSize(QSize(60, 60))
        self.pushButton_14.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_14.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_14, 2, 4, 1, 1)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(60, 60))
        self.pushButton_25.setMaximumSize(QSize(60, 60))
        self.pushButton_25.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_25.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_25, 6, 3, 1, 1)

        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(60, 60))
        self.pushButton_22.setMaximumSize(QSize(60, 60))
        self.pushButton_22.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_22.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_22, 5, 4, 1, 1)

        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(60, 60))
        self.pushButton_24.setMaximumSize(QSize(60, 60))
        self.pushButton_24.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_24.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_24, 6, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.centralwidget)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(60, 60))
        self.pushButton_27.setMaximumSize(QSize(60, 60))
        self.pushButton_27.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_27.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_27, 7, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(60, 60))
        self.pushButton_5.setMaximumSize(QSize(60, 60))
        self.pushButton_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_5, 6, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(60, 60))
        self.pushButton_6.setMaximumSize(QSize(60, 60))
        self.pushButton_6.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_6.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_6, 7, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(60, 60))
        self.pushButton_2.setMaximumSize(QSize(60, 60))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 60))
        self.pushButton_3.setMaximumSize(QSize(60, 60))
        self.pushButton_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMinimumSize(QSize(60, 60))
        self.pushButton.setMaximumSize(QSize(60, 60))
        self.pushButton.setFocusPolicy(Qt.ClickFocus)
        self.pushButton.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(60, 60))
        self.pushButton_15.setMaximumSize(QSize(60, 60))
        self.pushButton_15.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_15.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #fdfdfd;\n"
            "color: black;\n"
            "border: 1px solid black;\n"
            "border-radius: 6px;\n"
            "font-size: 26pt;\n"
            "}\n"
            "\n"
            "QPushButton:focus\n"
            "{\n"
            " background-color: white;\n"
            "border: 2px solid black;\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton_15, 3, 1, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer_7 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.pushButton_Q = QPushButton(self.centralwidget)
        self.pushButton_Q.setObjectName("pushButton_Q")
        self.pushButton_Q.setMinimumSize(QSize(50, 50))
        self.pushButton_Q.setMaximumSize(QSize(50, 50))
        self.pushButton_Q.setFocusPolicy(Qt.NoFocus)
        self.pushButton_Q.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_Q)

        self.pushButton_W = QPushButton(self.centralwidget)
        self.pushButton_W.setObjectName("pushButton_W")
        self.pushButton_W.setMinimumSize(QSize(50, 50))
        self.pushButton_W.setMaximumSize(QSize(50, 50))
        self.pushButton_W.setFocusPolicy(Qt.NoFocus)
        self.pushButton_W.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_W)

        self.pushButton_E = QPushButton(self.centralwidget)
        self.pushButton_E.setObjectName("pushButton_E")
        self.pushButton_E.setMinimumSize(QSize(50, 50))
        self.pushButton_E.setMaximumSize(QSize(50, 50))
        self.pushButton_E.setFocusPolicy(Qt.NoFocus)
        self.pushButton_E.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_E)

        self.pushButton_R = QPushButton(self.centralwidget)
        self.pushButton_R.setObjectName("pushButton_R")
        self.pushButton_R.setMinimumSize(QSize(50, 50))
        self.pushButton_R.setMaximumSize(QSize(50, 50))
        self.pushButton_R.setFocusPolicy(Qt.NoFocus)
        self.pushButton_R.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_R)

        self.pushButton_T = QPushButton(self.centralwidget)
        self.pushButton_T.setObjectName("pushButton_T")
        self.pushButton_T.setMinimumSize(QSize(50, 50))
        self.pushButton_T.setMaximumSize(QSize(50, 50))
        self.pushButton_T.setFocusPolicy(Qt.NoFocus)
        self.pushButton_T.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_T)

        self.pushButton_Z = QPushButton(self.centralwidget)
        self.pushButton_Z.setObjectName("pushButton_Z")
        self.pushButton_Z.setMinimumSize(QSize(50, 50))
        self.pushButton_Z.setMaximumSize(QSize(50, 50))
        self.pushButton_Z.setFocusPolicy(Qt.NoFocus)
        self.pushButton_Z.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_Z)

        self.pushButton_U = QPushButton(self.centralwidget)
        self.pushButton_U.setObjectName("pushButton_U")
        self.pushButton_U.setMinimumSize(QSize(50, 50))
        self.pushButton_U.setMaximumSize(QSize(50, 50))
        self.pushButton_U.setFocusPolicy(Qt.NoFocus)
        self.pushButton_U.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_U)

        self.pushButton_I = QPushButton(self.centralwidget)
        self.pushButton_I.setObjectName("pushButton_I")
        self.pushButton_I.setMinimumSize(QSize(50, 50))
        self.pushButton_I.setMaximumSize(QSize(50, 50))
        self.pushButton_I.setFocusPolicy(Qt.NoFocus)
        self.pushButton_I.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_I)

        self.pushButton_O = QPushButton(self.centralwidget)
        self.pushButton_O.setObjectName("pushButton_O")
        self.pushButton_O.setMinimumSize(QSize(50, 50))
        self.pushButton_O.setMaximumSize(QSize(50, 50))
        self.pushButton_O.setFocusPolicy(Qt.NoFocus)
        self.pushButton_O.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_O)

        self.pushButton_P = QPushButton(self.centralwidget)
        self.pushButton_P.setObjectName("pushButton_P")
        self.pushButton_P.setMinimumSize(QSize(50, 50))
        self.pushButton_P.setMaximumSize(QSize(50, 50))
        self.pushButton_P.setFocusPolicy(Qt.NoFocus)
        self.pushButton_P.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_3.addWidget(self.pushButton_P)

        self.horizontalSpacer_8 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer_5 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pushButton_A = QPushButton(self.centralwidget)
        self.pushButton_A.setObjectName("pushButton_A")
        self.pushButton_A.setMinimumSize(QSize(50, 50))
        self.pushButton_A.setMaximumSize(QSize(50, 50))
        self.pushButton_A.setFocusPolicy(Qt.NoFocus)
        self.pushButton_A.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_A)

        self.pushButton_S = QPushButton(self.centralwidget)
        self.pushButton_S.setObjectName("pushButton_S")
        self.pushButton_S.setMinimumSize(QSize(50, 50))
        self.pushButton_S.setMaximumSize(QSize(50, 50))
        self.pushButton_S.setFocusPolicy(Qt.NoFocus)
        self.pushButton_S.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_S)

        self.pushButton_D = QPushButton(self.centralwidget)
        self.pushButton_D.setObjectName("pushButton_D")
        self.pushButton_D.setMinimumSize(QSize(50, 50))
        self.pushButton_D.setMaximumSize(QSize(50, 50))
        self.pushButton_D.setFocusPolicy(Qt.NoFocus)
        self.pushButton_D.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_D)

        self.pushButton_F = QPushButton(self.centralwidget)
        self.pushButton_F.setObjectName("pushButton_F")
        self.pushButton_F.setMinimumSize(QSize(50, 50))
        self.pushButton_F.setMaximumSize(QSize(50, 50))
        self.pushButton_F.setFocusPolicy(Qt.NoFocus)
        self.pushButton_F.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_F)

        self.pushButton_G = QPushButton(self.centralwidget)
        self.pushButton_G.setObjectName("pushButton_G")
        self.pushButton_G.setMinimumSize(QSize(50, 50))
        self.pushButton_G.setMaximumSize(QSize(50, 50))
        self.pushButton_G.setFocusPolicy(Qt.NoFocus)
        self.pushButton_G.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_G)

        self.pushButton_H = QPushButton(self.centralwidget)
        self.pushButton_H.setObjectName("pushButton_H")
        self.pushButton_H.setMinimumSize(QSize(50, 50))
        self.pushButton_H.setMaximumSize(QSize(50, 50))
        self.pushButton_H.setFocusPolicy(Qt.NoFocus)
        self.pushButton_H.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_H)

        self.pushButton_J = QPushButton(self.centralwidget)
        self.pushButton_J.setObjectName("pushButton_J")
        self.pushButton_J.setMinimumSize(QSize(50, 50))
        self.pushButton_J.setMaximumSize(QSize(50, 50))
        self.pushButton_J.setFocusPolicy(Qt.NoFocus)
        self.pushButton_J.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_J)

        self.pushButton_K = QPushButton(self.centralwidget)
        self.pushButton_K.setObjectName("pushButton_K")
        self.pushButton_K.setMinimumSize(QSize(50, 50))
        self.pushButton_K.setMaximumSize(QSize(50, 50))
        self.pushButton_K.setFocusPolicy(Qt.NoFocus)
        self.pushButton_K.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_K)

        self.pushButton_L = QPushButton(self.centralwidget)
        self.pushButton_L.setObjectName("pushButton_L")
        self.pushButton_L.setMinimumSize(QSize(50, 50))
        self.pushButton_L.setMaximumSize(QSize(50, 50))
        self.pushButton_L.setFocusPolicy(Qt.NoFocus)
        self.pushButton_L.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_4.addWidget(self.pushButton_L)

        self.horizontalSpacer_6 = QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer_9 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.pushButton_Y = QPushButton(self.centralwidget)
        self.pushButton_Y.setObjectName("pushButton_Y")
        self.pushButton_Y.setMinimumSize(QSize(50, 50))
        self.pushButton_Y.setMaximumSize(QSize(50, 50))
        self.pushButton_Y.setFocusPolicy(Qt.NoFocus)
        self.pushButton_Y.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_Y)

        self.pushButton_X = QPushButton(self.centralwidget)
        self.pushButton_X.setObjectName("pushButton_X")
        self.pushButton_X.setMinimumSize(QSize(50, 50))
        self.pushButton_X.setMaximumSize(QSize(50, 50))
        self.pushButton_X.setFocusPolicy(Qt.NoFocus)
        self.pushButton_X.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_X)

        self.pushButton_C = QPushButton(self.centralwidget)
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_C.setMinimumSize(QSize(50, 50))
        self.pushButton_C.setMaximumSize(QSize(50, 50))
        self.pushButton_C.setFocusPolicy(Qt.NoFocus)
        self.pushButton_C.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_C)

        self.pushButton_V = QPushButton(self.centralwidget)
        self.pushButton_V.setObjectName("pushButton_V")
        self.pushButton_V.setMinimumSize(QSize(50, 50))
        self.pushButton_V.setMaximumSize(QSize(50, 50))
        self.pushButton_V.setFocusPolicy(Qt.NoFocus)
        self.pushButton_V.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_V)

        self.pushButton_B = QPushButton(self.centralwidget)
        self.pushButton_B.setObjectName("pushButton_B")
        self.pushButton_B.setMinimumSize(QSize(50, 50))
        self.pushButton_B.setMaximumSize(QSize(50, 50))
        self.pushButton_B.setFocusPolicy(Qt.NoFocus)
        self.pushButton_B.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_B)

        self.pushButton_N = QPushButton(self.centralwidget)
        self.pushButton_N.setObjectName("pushButton_N")
        self.pushButton_N.setMinimumSize(QSize(50, 50))
        self.pushButton_N.setMaximumSize(QSize(50, 50))
        self.pushButton_N.setFocusPolicy(Qt.NoFocus)
        self.pushButton_N.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_N)

        self.pushButton_M = QPushButton(self.centralwidget)
        self.pushButton_M.setObjectName("pushButton_M")
        self.pushButton_M.setMinimumSize(QSize(50, 50))
        self.pushButton_M.setMaximumSize(QSize(50, 50))
        self.pushButton_M.setFocusPolicy(Qt.NoFocus)
        self.pushButton_M.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_5.addWidget(self.pushButton_M)

        self.horizontalSpacer_10 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(7, 7, 7, 7)
        self.horizontalSpacer_12 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.pushButton_SEND = QPushButton(self.centralwidget)
        self.pushButton_SEND.setObjectName("pushButton_SEND")
        self.pushButton_SEND.setMinimumSize(QSize(100, 50))
        self.pushButton_SEND.setSizeIncrement(QSize(100, 50))
        self.pushButton_SEND.setFocusPolicy(Qt.NoFocus)
        self.pushButton_SEND.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_SEND)

        self.pushButton_UE = QPushButton(self.centralwidget)
        self.pushButton_UE.setObjectName("pushButton_UE")
        self.pushButton_UE.setMinimumSize(QSize(50, 50))
        self.pushButton_UE.setMaximumSize(QSize(50, 50))
        self.pushButton_UE.setFocusPolicy(Qt.NoFocus)
        self.pushButton_UE.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_UE)

        self.pushButton_OE = QPushButton(self.centralwidget)
        self.pushButton_OE.setObjectName("pushButton_OE")
        self.pushButton_OE.setMinimumSize(QSize(50, 50))
        self.pushButton_OE.setMaximumSize(QSize(50, 50))
        self.pushButton_OE.setFocusPolicy(Qt.NoFocus)
        self.pushButton_OE.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_OE)

        self.pushButton_AE = QPushButton(self.centralwidget)
        self.pushButton_AE.setObjectName("pushButton_AE")
        self.pushButton_AE.setMinimumSize(QSize(50, 50))
        self.pushButton_AE.setMaximumSize(QSize(50, 50))
        self.pushButton_AE.setFocusPolicy(Qt.NoFocus)
        self.pushButton_AE.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_AE)

        self.pushButton_SS = QPushButton(self.centralwidget)
        self.pushButton_SS.setObjectName("pushButton_SS")
        self.pushButton_SS.setMinimumSize(QSize(50, 50))
        self.pushButton_SS.setMaximumSize(QSize(50, 50))
        self.pushButton_SS.setFocusPolicy(Qt.NoFocus)
        self.pushButton_SS.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_SS)

        self.pushButton_DEL = QPushButton(self.centralwidget)
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.pushButton_DEL.setMinimumSize(QSize(100, 50))
        self.pushButton_DEL.setSizeIncrement(QSize(100, 50))
        self.pushButton_DEL.setFocusPolicy(Qt.NoFocus)
        self.pushButton_DEL.setStyleSheet(
            "QPushButton\n"
            "{\n"
            "background-color: #d0d0d0;\n"
            "color: black;\n"
            "border: 0px;\n"
            "border-radius: 6px;\n"
            "font-size: 20pt;\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.pushButton_DEL)

        self.horizontalSpacer_11 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(
            0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(
            0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 658, 21))
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.pushButton_25)
        QWidget.setTabOrder(self.pushButton_25, self.pushButton_26)
        QWidget.setTabOrder(self.pushButton_26, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_27)
        QWidget.setTabOrder(self.pushButton_27, self.pushButton_28)
        QWidget.setTabOrder(self.pushButton_28, self.pushButton_29)
        QWidget.setTabOrder(self.pushButton_29, self.pushButton_30)
        QWidget.setTabOrder(self.pushButton_30, self.pushButton_Q)
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
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "pyWordle", None)
        )
        self.action_Close.setText(
            QCoreApplication.translate("MainWindow", "&Close", None)
        )
        self.actionAbout_Qt.setText(
            QCoreApplication.translate("MainWindow", "About &Qt", None)
        )
        self.pushButton_4.setText("")
        self.pushButton_7.setText("")
        self.pushButton_30.setText("")
        self.pushButton_21.setText("")
        self.pushButton_18.setText("")
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.pushButton_19.setText("")
        self.pushButton_28.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.pushButton_29.setText("")
        self.pushButton_8.setText("")
        self.pushButton_20.setText("")
        self.pushButton_26.setText("")
        self.pushButton_23.setText("")
        self.pushButton_14.setText("")
        self.pushButton_25.setText("")
        self.pushButton_22.setText("")
        self.pushButton_24.setText("")
        self.pushButton_27.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        # if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "QPushButton\n"
                "{\n"
                "background-color: white;\n"
                "color: black;\n"
                "border: 2px solid black;\n"
                "border-radius: 6px;\n"
                "}",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.pushButton.setText("")
        self.pushButton_15.setText("")
        self.pushButton_Q.setText(QCoreApplication.translate("MainWindow", "Q", None))
        self.pushButton_W.setText(QCoreApplication.translate("MainWindow", "W", None))
        self.pushButton_E.setText(QCoreApplication.translate("MainWindow", "E", None))
        self.pushButton_R.setText(QCoreApplication.translate("MainWindow", "R", None))
        self.pushButton_T.setText(QCoreApplication.translate("MainWindow", "T", None))
        self.pushButton_Z.setText(QCoreApplication.translate("MainWindow", "Z", None))
        self.pushButton_U.setText(QCoreApplication.translate("MainWindow", "U", None))
        self.pushButton_I.setText(QCoreApplication.translate("MainWindow", "I", None))
        self.pushButton_O.setText(QCoreApplication.translate("MainWindow", "O", None))
        self.pushButton_P.setText(QCoreApplication.translate("MainWindow", "P", None))
        self.pushButton_A.setText(QCoreApplication.translate("MainWindow", "A", None))
        self.pushButton_S.setText(QCoreApplication.translate("MainWindow", "S", None))
        self.pushButton_D.setText(QCoreApplication.translate("MainWindow", "D", None))
        self.pushButton_F.setText(QCoreApplication.translate("MainWindow", "F", None))
        self.pushButton_G.setText(QCoreApplication.translate("MainWindow", "G", None))
        self.pushButton_H.setText(QCoreApplication.translate("MainWindow", "H", None))
        self.pushButton_J.setText(QCoreApplication.translate("MainWindow", "J", None))
        self.pushButton_K.setText(QCoreApplication.translate("MainWindow", "K", None))
        self.pushButton_L.setText(QCoreApplication.translate("MainWindow", "L", None))
        self.pushButton_Y.setText(QCoreApplication.translate("MainWindow", "Y", None))
        self.pushButton_X.setText(QCoreApplication.translate("MainWindow", "X", None))
        self.pushButton_C.setText(QCoreApplication.translate("MainWindow", "C", None))
        self.pushButton_V.setText(QCoreApplication.translate("MainWindow", "V", None))
        self.pushButton_B.setText(QCoreApplication.translate("MainWindow", "B", None))
        self.pushButton_N.setText(QCoreApplication.translate("MainWindow", "N", None))
        self.pushButton_M.setText(QCoreApplication.translate("MainWindow", "M", None))
        self.pushButton_SEND.setText(
            QCoreApplication.translate("MainWindow", "SEND", None)
        )
        self.pushButton_UE.setText(
            QCoreApplication.translate("MainWindow", "\u00dc", None)
        )
        self.pushButton_OE.setText(
            QCoreApplication.translate("MainWindow", "\u00d6", None)
        )
        self.pushButton_AE.setText(
            QCoreApplication.translate("MainWindow", "\u00c4", None)
        )
        self.pushButton_SS.setText(
            QCoreApplication.translate("MainWindow", "\u1e9e", None)
        )
        self.pushButton_DEL.setText(
            QCoreApplication.translate("MainWindow", "DEL", None)
        )
        self.menu_About.setTitle(
            QCoreApplication.translate("MainWindow", "&About", None)
        )
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", "&File", None))

    # retranslateUi
