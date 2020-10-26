# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import requests
import urllib.request
import os
import ctypes


url_download_path = 'http://localhost:8000/media/file/HospiltalOS_NHSO_Update.exe'


class Ui_formProgressBar(object):
    def setupUi(self, formProgressBar):
        formProgressBar.setObjectName("formProgressBar")
        formProgressBar.resize(425, 117)
        formProgressBar.setMinimumSize(QtCore.QSize(425, 117))
        formProgressBar.setMaximumSize(QtCore.QSize(425, 117))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/download-files.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formProgressBar.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(formProgressBar)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 20, 391, 31))
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(170, 60, 93, 28))
        self.btn_download.setObjectName("btn_download")
        formProgressBar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(formProgressBar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 26))
        self.menubar.setObjectName("menubar")
        formProgressBar.setMenuBar(self.menubar)

        self.retranslateUi(formProgressBar)
        QtCore.QMetaObject.connectSlotsByName(formProgressBar)

        self.btn_download.clicked.connect(self.Download)

    def Download(self):
        try:
            self.btn_download.setEnabled(False)
            urllib.request.urlretrieve(url_download_path, "Update_HospitalOS.exe", self.Handel_Progress)
            self.run_patch()
        except :
            QMessageBox.warning(self, "Download Error", "Check Connection Internet")
            return


    def closescr(self, formProgressBar):
        # print("test2")
        # hide the screen on exit btn clicked
        formProgressBar.hide()


    def run_patch(self):
        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'Update_HospitalOS.exe', None, None, 10)

    def Handel_Progress(self, blocknum, blocksize, totalsize):
        readed_data = blocknum * blocksize
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)




    def retranslateUi(self, formProgressBar):
        _translate = QtCore.QCoreApplication.translate
        formProgressBar.setWindowTitle(_translate("formProgressBar", "Download"))
        self.btn_download.setText(_translate("formProgressBar", "Download"))
