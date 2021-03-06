# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_database.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
import os.path
from os import path



class Ui_form_database(object):
    def setupUi(self, form_database):
        form_database.setObjectName("form_database")
        form_database.resize(245, 369)
        form_database.setMinimumSize(QtCore.QSize(245, 369))
        form_database.setMaximumSize(QtCore.QSize(245, 369))
        form_database.setWindowTitle("Database")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/database-storage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_database.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(form_database)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 221, 241))
        self.groupBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 40, 91, 21))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 91, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 41, 21))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 51, 21))
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 61, 21))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.txt_server = QtWidgets.QLineEdit(self.groupBox)
        self.txt_server.setGeometry(QtCore.QRect(100, 40, 113, 22))
        self.txt_server.setObjectName("txt_server")
        self.txt_databasename = QtWidgets.QLineEdit(self.groupBox)
        self.txt_databasename.setGeometry(QtCore.QRect(100, 80, 113, 22))
        self.txt_databasename.setObjectName("txt_databasename")
        self.txt_port = QtWidgets.QLineEdit(self.groupBox)
        self.txt_port.setGeometry(QtCore.QRect(100, 120, 113, 22))
        self.txt_port.setObjectName("txt_port")
        self.txt_user = QtWidgets.QLineEdit(self.groupBox)
        self.txt_user.setGeometry(QtCore.QRect(100, 160, 113, 22))
        self.txt_user.setObjectName("txt_user")
        self.txt_pass = QtWidgets.QLineEdit(self.groupBox)
        self.txt_pass.setGeometry(QtCore.QRect(100, 200, 113, 22))
        self.txt_pass.setObjectName("txt_pass")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setGeometry(QtCore.QRect(10, 280, 101, 41))
        self.btn_ok.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancal.setGeometry(QtCore.QRect(130, 280, 101, 41))
        self.btn_cancal.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.btn_cancal.setObjectName("btn_cancal")
        form_database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(form_database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 245, 26))
        self.menubar.setObjectName("menubar")
        form_database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form_database)
        self.statusbar.setObjectName("statusbar")
        form_database.setStatusBar(self.statusbar)

        self.retranslateUi(form_database)
        QtCore.QMetaObject.connectSlotsByName(form_database)

        if path.exists('config.ini') == True:
            config_object = ConfigParser()
            config_object.read("config.ini")
            # Get
            serverinfo = config_object["SERVERCONFIG"]
            self.txt_server.setText(serverinfo["host"])
            self.txt_databasename.setText(serverinfo["dbname"])
            self.txt_user.setText(serverinfo["user"])
            self.txt_pass.setText(serverinfo["passwd"])
            self.txt_port.setText(serverinfo["port"])

        else:
            config_object = ConfigParser()
            config_object["SERVERCONFIG"] = {
                "host": "",
                "dbname": "",
                "user": "",
                "passwd": "",
                "port": ""
            }


        # lambda is used when passing extra arg in the method
        self.btn_cancal.clicked.connect(lambda: self.closescr(form_database))
        self.btn_ok.clicked.connect(lambda: self.addConfigDB(form_database))
        # self.btn_ok.clicked.connect(self.addConfigDB)

    def addConfigDB(self, form_database):
        # Read config.ini file
        config_object = ConfigParser()
        config_object.read("config.ini")

        # Get the serverinfo section
        config_object["SERVERCONFIG"] = {
            "host": self.txt_server.text(),
            "dbname": self.txt_databasename.text(),
            "user": self.txt_user.text(),
            "passwd": self.txt_pass.text(),
            "port": self.txt_port.text()
        }

        # Write changes back to file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)

        form_database.hide()

    def closescr(self, form_database):
        # print("test2")
        # hide the screen on exit btn clicked
        form_database.hide()

    def retranslateUi(self, form_database):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("form_database", "ฐานข้อมูล"))
        self.label.setText(_translate("form_database", "เครื่องแม่ข่าย"))
        self.label_2.setText(_translate("form_database", "ชื่อฐานข้อมูล"))
        self.label_3.setText(_translate("form_database", "พอร์ต"))
        self.label_4.setText(_translate("form_database", "ชื่อผู้ใช้"))
        self.label_5.setText(_translate("form_database", "รหัสผ่าน"))
        self.btn_ok.setText(_translate("form_database", "ตกลง"))
        self.btn_cancal.setText(_translate("form_database", "ยกเลิก"))



