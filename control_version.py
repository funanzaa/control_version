# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_version.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import subprocess
import win32api
import ctypes
import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

_AppName_ = 'AutoUpdate'
_AppHos_ = 'Hos3.9'

__version__ = '1.0'  # version program


class Ui_Main(object):
    def setupUi(self, Main):
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # print(BASE_DIR)
        Main.setObjectName("Main")
        Main.resize(506, 252)
        Main.setMinimumSize(QtCore.QSize(506, 252))
        Main.setMaximumSize(QtCore.QSize(506, 252))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/update_reload_sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHos = QtWidgets.QPushButton(self.centralwidget)
        self.btnHos.setGeometry(QtCore.QRect(50, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("TH Sarabun New")
        font.setPointSize(14)
        self.btnHos.setFont(font)
        self.btnHos.setObjectName("btnHos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 91, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/IconLogo.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 40, 91, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("icon/admin.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdmin.setGeometry(QtCore.QRect(190, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("TH Sarabun New")
        font.setPointSize(14)
        self.btnAdmin.setFont(font)
        self.btnAdmin.setObjectName("btnAdmin")
        self.btnReportCenter = QtWidgets.QPushButton(self.centralwidget)
        self.btnReportCenter.setGeometry(QtCore.QRect(330, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("TH Sarabun New")
        font.setPointSize(14)
        self.btnReportCenter.setFont(font)
        self.btnReportCenter.setObjectName("btnReportCenter")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 50, 91, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icon/icon_report.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.actionabout = QtWidgets.QAction(Main)
        self.actionabout.setObjectName("actionabout")
        self.actionDatabase = QtWidgets.QAction(Main)
        self.actionDatabase.setObjectName("actionDatabase")
        self.actionAbout = QtWidgets.QAction(Main)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionDatabase)
        self.menuHelp.addAction(self.actionabout)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.btnHos.clicked.connect(self.open_hos)
        self.btnAdmin.clicked.connect(self.open_admin)
        self.btnReportCenter.clicked.connect(self.open_report)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", (_AppName_ + ' ' + str(__version__))))
        self.btnHos.setText(_translate("Main", "HospitalOS"))
        self.btnAdmin.setText(_translate("Main", "Admin"))
        self.btnReportCenter.setText(_translate("Main", "Report Center"))
        self.menuFile.setTitle(_translate("Main", "File"))
        self.menuHelp.setTitle(_translate("Main", "Settings"))
        self.menuAbout.setTitle(_translate("Main", "Help"))
        self.actionabout.setText(_translate("Main", "Database"))
        self.actionDatabase.setText(_translate("Main", "Quit"))
        self.actionAbout.setText(_translate("Main", "About"))

    def open_hos(self):
        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'HospitalOS.exe', None, None, 10)


    def open_admin(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        APP_DIR = os.path.join(BASE_DIR, 'Hos3.9')
        print(APP_DIR)
        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'run_mod.bat', None, None, 10)

    def open_report(self):
        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'Report.exe', None, None, 10)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
