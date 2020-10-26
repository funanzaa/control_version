# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_version.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
from form_database import Ui_form_database # import form database screen
from progressBar import Ui_formProgressBar
import psycopg2
from os import path
import requests
from PyQt5.QtWidgets import QMessageBox, QProgressBar, QVBoxLayout
from tqdm import tqdm
import ctypes

__version__ = '1.0'
r_hos_version = requests.get('http://localhost:8000/media/file/hospitalos_version.txt')
r_sql_hos43 = requests.get('http://localhost:8000/media/file/updateV3_9_43.txt')
sql_hos43 = r_sql_hos43.text
server_version_hos = r_hos_version.text
class Ui_Main(object):
    def setupUi(self, Main):
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
        self.actionSetting = QtWidgets.QAction(Main)
        self.actionSetting.setObjectName("actionSetting")
        self.actionFlie = QtWidgets.QAction(Main)

        self.actionFlie.setObjectName("actionFlie")
        self.actionAbout = QtWidgets.QAction(Main)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionFlie)
        self.menuHelp.addAction(self.actionSetting)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

        #code


        self.actionSetting.triggered.connect(self.databaseForm) # call form form database
        # self.btnHos.clicked.connect(self.checkVersion)
        self.btnHos.clicked.connect(lambda: self.checkVersion("Hos"))
        self.btnAdmin.clicked.connect(lambda: self.checkVersion("Admin"))
        self.btnReportCenter.clicked.connect(lambda: self.checkVersion("Report"))


    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Autoupdate" + __version__))
        self.btnHos.setText(_translate("Main", "HospitalOS"))
        self.btnAdmin.setText(_translate("Main", "Admin"))
        self.btnReportCenter.setText(_translate("Main", "Report Center"))
        self.menuFile.setTitle(_translate("Main", "File"))
        self.menuHelp.setTitle(_translate("Main", "Settings"))
        self.menuAbout.setTitle(_translate("Main", "Help"))
        self.actionSetting.setText(_translate("Main", "Database"))
        self.actionFlie.setText(_translate("Main", "Quit"))
        self.actionAbout.setText(_translate("Main", "About"))


    def get_config(self):
        config_object = ConfigParser()
        config_object.read("config.ini")
        serverinfo = config_object["SERVERCONFIG"]
        dbname = serverinfo["dbname"]
        user = serverinfo["user"]
        host = serverinfo["host"]
        password = serverinfo["passwd"]
        return dbname, user, host, password

    def config_test(self):
        if path.exists('config.ini') == True:
            dbname, user, host, password = self.get_config()  # get function get_config
            conn = self.postgres_test(dbname, user, host, password)
            return conn
        else:
            return False

    def file_app_version_test(self):
        if path.exists('current_versions.txt') == True:
            f = open("current_versions.txt", "r")
            return f.read()
        else:
            return False

    def postgres_test(self, dbname, user, host, password ):
        text = "dbname={} user={} host={} password={} connect_timeout=1".format(dbname, user, host, password)
        try:
            conn = psycopg2.connect(text)
            conn.close()
            return True
        except:
            return False


    def databaseForm(self):
        self.form_database = QtWidgets.QMainWindow()
        self.ui = Ui_form_database()
        self.ui.setupUi(self.form_database)
        self.form_database.show()

    def checkVersion(self, choice):
        # print(choice)
        # select version hos
        select_version = "select max(replace(version_db,'.','')) from s_version;"
        if self.config_test() == True:
            dbname, user, host, password = self.get_config() # get function get_config
            text = "dbname={} user={} host={} password={} connect_timeout=1".format(dbname, user, host, password)
            # Connect to your postgres DB
            conn = psycopg2.connect(text)
            # Open a cursor to perform database operations
            cur = conn.cursor()
            # Execute a query
            cur.execute("select max(replace(version_db,'.','')) from s_version")
            # Retrieve query results
            records = cur.fetchone()
            cur.close()
            conn.close()
            # r_hos_version = requests.get('http://localhost:8000/media/file/hospitalos_version.txt')
            # r_sql_hos43 = requests.get('http://localhost:8000/media/file/updateV3_9_43.txt')
            # server_version_hos = r_hos_version.text
            local_version_hos = records[0]
            # print(self.file_app_version_test())
            #  case 1) No update DB and No file verions_current
            if int(local_version_hos) < int(server_version_hos) and self.file_app_version_test() == False:
                self.show_popup1(r_hos_version.text, records[0])
            # update DB but No file verions_current
            elif int(local_version_hos) == int(server_version_hos) and self.file_app_version_test() == False:
                self.show_popup2(r_hos_version.text, records[0])
            # No update DB but have file verions_current
            elif int(local_version_hos) < int(server_version_hos) and int(self.file_app_version_test()) == int(server_version_hos):
                self.show_popup1(r_hos_version.text, records[0])
            else:
                if choice == "Hos":
                    print("run hospital.exe")
                elif choice == "Admin":
                    print("run admin.exe")
                elif choice == "Report":
                    print("run Report.exe")
        else:
            self.databaseForm()

    def show_popup1(self, records, local_version_hos):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("ตรวจพบ Hospital-OS NHSO มีเวอร์ชั่นใหม่ " + records + " !! ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("ต้องการอัพเดท หรือไม่")
        msg.setDetailedText("**ปัจจุบัน Hospital-OS NHSO verion" + local_version_hos)

        msg.buttonClicked.connect(self.popup_button1)


        x = msg.exec_()

    def show_popup2(self, records, local_version_hos):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("ตรวจพบ Hospital-OS NHSO มีเวอร์ชั่นใหม่ " + records + " !! ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("ต้องการอัพเดท หรือไม่")
        msg.setDetailedText("**ปัจจุบัน (Versions Database อัพเดทแล้ว)" + local_version_hos)

        msg.buttonClicked.connect(self.popup_button2)


        x = msg.exec_()

    def popup_button1(self, answer):
        if answer.text() == 'OK':
            dbname, user, host, password = self.get_config()
            text = "dbname={} user={} host={} password={} connect_timeout=1".format(dbname, user, host, password)
            conn = psycopg2.connect(text)
            cur = conn.cursor()
            cur.execute(sql_hos43)
            conn.commit()
            cur.close()
            conn.close()
            print(answer.text())

    def popup_button2(self, answer):
        if answer.text() == 'OK':
            self.bar_download()

    def bar_download(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_formProgressBar()
        self.ui.setupUi(self.window)
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
