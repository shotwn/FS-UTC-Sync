﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Mon Nov 11 00:33:31 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 162)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background-color: #151515;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"color: #ffffff;\n"
"}\n"
"\n"
"QToolButton {\n"
"    color: #ffffff;\n"
"    background-color: #151515;\n"
"    border: 0px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.real_time_hour = QtWidgets.QLabel(self.centralwidget)
        self.real_time_hour.setGeometry(QtCore.QRect(0, 20, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(90)
        self.real_time_hour.setFont(font)
        self.real_time_hour.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.real_time_hour.setObjectName("real_time_hour")
        self.real_date = QtWidgets.QLabel(self.centralwidget)
        self.real_date.setGeometry(QtCore.QRect(251, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.real_date.setFont(font)
        self.real_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.real_date.setObjectName("real_date")
        self.utc_label = QtWidgets.QLabel(self.centralwidget)
        self.utc_label.setGeometry(QtCore.QRect(261, 126, 51, 13))
        self.utc_label.setStyleSheet("")
        self.utc_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.utc_label.setObjectName("utc_label")
        self.sim_label = QtWidgets.QLabel(self.centralwidget)
        self.sim_label.setGeometry(QtCore.QRect(331, 29, 111, 16))
        self.sim_label.setObjectName("sim_label")
        self.sim_time_hour = QtWidgets.QLabel(self.centralwidget)
        self.sim_time_hour.setGeometry(QtCore.QRect(429, 7, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sim_time_hour.setFont(font)
        self.sim_time_hour.setObjectName("sim_time_hour")
        self.sim_date = QtWidgets.QLabel(self.centralwidget)
        self.sim_date.setGeometry(QtCore.QRect(411, 31, 81, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sim_date.setFont(font)
        self.sim_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sim_date.setObjectName("sim_date")
        self.left_status = QtWidgets.QLabel(self.centralwidget)
        self.left_status.setGeometry(QtCore.QRect(18, 126, 221, 13))
        self.left_status.setText("")
        self.left_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.left_status.setObjectName("left_status")
        self.left_value = QtWidgets.QLabel(self.centralwidget)
        self.left_value.setGeometry(QtCore.QRect(18, 140, 221, 13))
        self.left_value.setText("")
        self.left_value.setObjectName("left_value")
        self.live_button = QtWidgets.QToolButton(self.centralwidget)
        self.live_button.setGeometry(QtCore.QRect(342, 60, 60, 60))
        self.live_button.setStyleSheet("")
        self.live_button.setObjectName("live_button")
        self.sync_button = QtWidgets.QToolButton(self.centralwidget)
        self.sync_button.setGeometry(QtCore.QRect(418, 60, 60, 60))
        self.sync_button.setObjectName("sync_button")
        self.source_button = QtWidgets.QToolButton(self.centralwidget)
        self.source_button.setGeometry(QtCore.QRect(275, 139, 41, 13))
        self.source_button.setObjectName("source_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 6, 81, 16))
        self.label_2.setObjectName("label_2")
        self.real_time_minute = QtWidgets.QLabel(self.centralwidget)
        self.real_time_minute.setGeometry(QtCore.QRect(158, 20, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(90)
        self.real_time_minute.setFont(font)
        self.real_time_minute.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.real_time_minute.setObjectName("real_time_minute")
        self.real_time_seperator = QtWidgets.QLabel(self.centralwidget)
        self.real_time_seperator.setGeometry(QtCore.QRect(139, 20, 21, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(70)
        self.real_time_seperator.setFont(font)
        self.real_time_seperator.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.real_time_seperator.setObjectName("real_time_seperator")
        self.sim_time_minute = QtWidgets.QLabel(self.centralwidget)
        self.sim_time_minute.setGeometry(QtCore.QRect(457, 7, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sim_time_minute.setFont(font)
        self.sim_time_minute.setObjectName("sim_time_minute")
        self.sim_time_seperator = QtWidgets.QLabel(self.centralwidget)
        self.sim_time_seperator.setGeometry(QtCore.QRect(451, 10, 5, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sim_time_seperator.setFont(font)
        self.sim_time_seperator.setObjectName("sim_time_seperator")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 10, 1, 141))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.line.setFont(font)
        self.line.setStyleSheet("border-color: #ffffff")
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.real_time_second = QtWidgets.QLabel(self.centralwidget)
        self.real_time_second.setGeometry(QtCore.QRect(292, 90, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(15)
        self.real_time_second.setFont(font)
        self.real_time_second.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.real_time_second.setObjectName("real_time_second")
        self.source_button_2 = QtWidgets.QToolButton(self.centralwidget)
        self.source_button_2.setGeometry(QtCore.QRect(13, 112, 41, 13))
        self.source_button_2.setObjectName("source_button_2")
        self.right_status = QtWidgets.QLabel(self.centralwidget)
        self.right_status.setGeometry(QtCore.QRect(330, 121, 161, 20))
        self.right_status.setText("")
        self.right_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.right_status.setObjectName("right_status")
        self.sim_time_second = QtWidgets.QLabel(self.centralwidget)
        self.sim_time_second.setGeometry(QtCore.QRect(481, 11, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sim_time_second.setFont(font)
        self.sim_time_second.setObjectName("sim_time_second")
        self.right_status_2 = QtWidgets.QLabel(self.centralwidget)
        self.right_status_2.setGeometry(QtCore.QRect(330, 135, 161, 20))
        self.right_status_2.setText("")
        self.right_status_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.right_status_2.setObjectName("right_status_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.real_time_hour.setText(QtWidgets.QApplication.translate("MainWindow", "12", None, -1))
        self.real_date.setText(QtWidgets.QApplication.translate("MainWindow", "12.12.2019", None, -1))
        self.utc_label.setToolTip(QtWidgets.QApplication.translate("MainWindow", "UTC.S : Using System Time", None, -1))
        self.utc_label.setText(QtWidgets.QApplication.translate("MainWindow", "UTC.S", None, -1))
        self.sim_label.setText(QtWidgets.QApplication.translate("MainWindow", "Waiting Simulator", None, -1))
        self.sim_time_hour.setText(QtWidgets.QApplication.translate("MainWindow", "01", None, -1))
        self.sim_date.setText(QtWidgets.QApplication.translate("MainWindow", "12.12.2019", None, -1))
        self.live_button.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Live Sync: Disabled", None, -1))
        self.live_button.setText(QtWidgets.QApplication.translate("MainWindow", "Live Sync", None, -1))
        self.sync_button.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Sync Now", None, -1))
        self.sync_button.setText(QtWidgets.QApplication.translate("MainWindow", "Sync Now", None, -1))
        self.source_button.setText(QtWidgets.QApplication.translate("MainWindow", "Source", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Simulator", None, -1))
        self.real_time_minute.setText(QtWidgets.QApplication.translate("MainWindow", "30", None, -1))
        self.real_time_seperator.setText(QtWidgets.QApplication.translate("MainWindow", ":", None, -1))
        self.sim_time_minute.setText(QtWidgets.QApplication.translate("MainWindow", "30", None, -1))
        self.sim_time_seperator.setText(QtWidgets.QApplication.translate("MainWindow", ":", None, -1))
        self.real_time_second.setText(QtWidgets.QApplication.translate("MainWindow", "00", None, -1))
        self.source_button_2.setText(QtWidgets.QApplication.translate("MainWindow", "Offset", None, -1))
        self.sim_time_second.setText(QtWidgets.QApplication.translate("MainWindow", "00", None, -1))

