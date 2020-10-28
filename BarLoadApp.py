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



url_download_path = 'http://localhost:8000/media/file/Setup_Autoupdate.exe'

class Ui_formProgressBarApp(object):
    def setupUi(self, formProgressBarApp):
        formProgressBarApp.setObjectName("formProgressBarApp")
        formProgressBarApp.resize(425, 117)
        formProgressBarApp.setMinimumSize(QtCore.QSize(425, 117))
        formProgressBarApp.setMaximumSize(QtCore.QSize(425, 117))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/update_reload_sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formProgressBarApp.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(formProgressBarApp)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 20, 391, 31))
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.btn_cancal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancal.setGeometry(QtCore.QRect(170, 60, 93, 28))
        self.btn_cancal.setObjectName("btn_cancal")
        formProgressBarApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(formProgressBarApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 26))
        self.menubar.setObjectName("menubar")
        formProgressBarApp.setMenuBar(self.menubar)

        self.retranslateUi(formProgressBarApp)
        QtCore.QMetaObject.connectSlotsByName(formProgressBarApp)

        self.btn_cancal.clicked.connect(lambda: self.Download(formProgressBarApp))

    def retranslateUi(self, formProgressBarApp):
        _translate = QtCore.QCoreApplication.translate
        formProgressBarApp.setWindowTitle(_translate("formProgressBarApp", "AutoUpdate"))
        self.btn_cancal.setText(_translate("formProgressBarApp", "Download"))

    def Download(self,formProgressBarApp):
        try:
            self.btn_cancal.setEnabled(False)
            urllib.request.urlretrieve(url_download_path, "Setup_Autoupdate.exe", self.Handel_Progress)
            formProgressBarApp.close()

            # self.run_patch()
        except :
            QMessageBox.warning(self, "Download Error", "Check Connection Internet")
            return

    def Handel_Progress(self, blocknum, blocksize, totalsize):
        readed_data = blocknum * blocksize
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)

    def run_patch(self):
        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'Setup_Autoupdate.exe', None, None, 10)



