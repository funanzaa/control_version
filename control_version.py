from PyQt5 import QtCore, QtGui, QtWidgets
from configparser import ConfigParser
from form_database import Ui_form_database # import form database screen
from progressBar import Ui_formProgressBar
from BarLoadApp import Ui_formProgressBarApp
import psycopg2
from os import path
import os
import requests
from PyQt5.QtWidgets import *
import ctypes
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import datetime
import pytz

# __domain__ = 'http://localhost:8000'

__domain__ = 'http://bkk.hospital-os.com/'

__version__ = '1.13'

serverVersionAutoUpdate = __domain__ + '/media/file/version_AppAutoUpdate.txt'
serverVersionHosVersion = __domain__ + '/media/file/hospitalos_version.txt'
serverVersionSqlHos = __domain__ + '/media/file/sql_update.txt'

req = Request(serverVersionAutoUpdate)
req_HosVersion = Request(serverVersionHosVersion)


# api send version

def get_config():
    config_object = ConfigParser()
    config_object.read("config.ini")
    serverinfo = config_object["SERVERCONFIG"]
    dbname = serverinfo["dbname"]
    user = serverinfo["user"]
    host = serverinfo["host"]
    password = serverinfo["passwd"]
    return dbname, user, host, password

# def get_Token():
#     url = f'{__domain__}/crm/api/auth/'
#
#     response = requests.post(url, data={'username': 'eakachai', 'password': 'passwordtest'})
#     return response.json()

def get_data(hcode):
    # url = f"{__domain__}/crm/api/ControlVersionDetail/{hcode}"
    # header = {'Authorization': f'Token {get_Token()}'}
    url = "http://bkk.hospital-os.com//crm/api/ControlVersionDetail/" + hcode
    respones = requests.get(url)
    return respones.json()

# print(get_data(12345))

def test_sql(sql):
    try:
        dbname, user, host, password = get_config()
        text = "dbname={} user={} host={} password={} connect_timeout=1".format(dbname, user, host, password)
        conn = psycopg2.connect(text)
        cur = conn.cursor()
        cur.execute(sql)
        records = cur.fetchone()
        return records[0]
        # conn.commit()
    except:
        return 'sql fail'
    else:
        cur.close()
        conn.close()


def send_api():
    hcode =  test_sql('select b_visit_office_id from b_site;')
    hos_version = test_sql("select max(replace(version_db,'.','')) from s_version;")
    hos_version_stock = test_sql("select max(replace(version_app,'.',''))|| ',' ||max(replace(version_db,'.','')) from s_stock_version;")
    hos_version_erefer = test_sql("select max(replace(version_app,'.',''))|| ',' ||max(replace(version_db,'.',''))from s_ereferral_version;")
    tz = pytz.timezone('Asia/Bangkok')
    now = (datetime.datetime.now(tz=tz))
    if get_data(hcode) == 'Not Found': ## ถ้า server ไม่มี hcode
        # url = f"{__domain__}/crm/api/ControlVersionList/"
        url = "http://bkk.hospital-os.com/crm/api/ControlVersionList/"
        # header = {'Authorization': f'Token {get_Token()}'}
        data = {
            "app_controlVersion": __version__,
            "hos_s_version": hos_version,
            "hos_stock_version": hos_version_stock,
            "hos_ereferral_version": hos_version_erefer,
            "hcode": hcode,
            "date_created": now
        }
        requests.post(url, data=data)
    else:
        # url = f"{__domain__}/crm/api/ControlVersionDetail/{hcode}/"
        url = "http://bkk.hospital-os.com/crm/api/ControlVersionDetail/" + hcode
        # header = {'Authorization': f'Token {get_Token()}'}
        data = {
            "app_controlVersion": __version__,
            "hos_s_version": hos_version,
            "hos_stock_version": hos_version_stock,
            "hos_ereferral_version": hos_version_erefer,
            "hcode": hcode,
            "date_created": now
        }
        requests.put(url, data=data)

send_api() ## send api version


def TestURL():
    try:
        response = urlopen(req)
    except HTTPError as e:
        return 'offline'
        # print('The server couldn\'t fulfill the request. Error code: ', e.code)
    except URLError as e:
        # print(e.reason)
        return 'offline'
    else:
        # print('Website is working fine')
        serverVersionAutoUpdate = requests.get(__domain__ + '/media/file/version_AppAutoUpdate.txt')
        ServerAutoUpdate = serverVersionAutoUpdate.text
        return float(ServerAutoUpdate)

ServerAutoUpdate = TestURL()


def TestURL_HosVer():
    try:
        response = urlopen(req_HosVersion)
    except HTTPError as e:
        return 'offline'
        # print('The server couldn\'t fulfill the request. Error code: ', e.code)
    except URLError as e:
        return 'offline'
    else:
        # print ('Website is  URL_SQL working fine')
        r_hos_version = requests.get(__domain__ + '/media/file/hospitalos_version.txt')
        server_version_hos = r_hos_version.text
        return server_version_hos

server_version_hos = TestURL_HosVer()


def TestURL_HosDB():
    try:
        response = urlopen(req_HosVersion)
    except HTTPError as e:
        return 'offline'
        # print('The server couldn\'t fulfill the request. Error code: ', e.code)
    except URLError as e:
        return 'offline'
    else:
        # print ('Website is  URL_SQL working fine')
        r_hos_version = requests.get(__domain__ + '/media/file/hospitalos_version_db.txt')
        server_version_hos = r_hos_version.text
        return server_version_hos

server_version_hos_db = TestURL_HosDB()

def TestURL_SQLHOS():
    try:
        response = urlopen(serverVersionSqlHos)
    except HTTPError as e:
        return 'offline'
    except URLError as e:
        # print(e.reason)
        return 'offline'
    else:
        # print ('Website is  serverVersionSqlHos working fine')
        r_sql_hos = requests.get(__domain__ + '/media/file/sql_update.txt')
        sql_hos_update_server = r_sql_hos.text
        return sql_hos_update_server

sql_hos_update_server = TestURL_SQLHOS()

# delete file StockModule.jar
if path.exists('./config/ext_module/stock.xml') == True:
    if path.exists('./lib/module/StockModule.jar') == True:
        os.remove('./lib/module/StockModule.jar')



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
        self.menuPlus = QtWidgets.QMenu(self.menubar)
        self.menuPlus.setObjectName("menuPlus")
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
        self.actionVersion_Postgres = QtWidgets.QAction(Main)
        self.actionVersion_Postgres.setObjectName("actionVersion_Postgres")
        self.action_ClaimCode = QtWidgets.QAction(Main)
        self.action_ClaimCode.setObjectName("action_ClaimCode")
        self.menuFile.addAction(self.actionFlie)
        self.menuHelp.addAction(self.actionSetting)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionVersion_Postgres)
        self.menuPlus.addAction(self.action_ClaimCode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuPlus.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

        # code

        if self.checkAutoUpdate() == True:
            self.AlertCheckVersionApp()

        self.actionSetting.triggered.connect(self.databaseForm) # call form form database
        self.actionFlie.triggered.connect(lambda: self.closescr(Main))
        self.actionAbout.triggered.connect(lambda: self.AlertCheckVersionInApp(Main))  # call Update app
        self.actionVersion_Postgres.triggered.connect(self.checkVersionPsql)
        self.btnHos.clicked.connect(lambda: self.checkVersion("Hos"))
        self.btnAdmin.clicked.connect(lambda: self.checkVersion("Admin"))
        self.btnReportCenter.clicked.connect(lambda: self.checkVersion("Report"))

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Autoupdate 1.4"))
        self.btnHos.setText(_translate("Main", "HospitalOS"))
        self.btnAdmin.setText(_translate("Main", "Admin"))
        self.btnReportCenter.setText(_translate("Main", "Report Center"))
        self.menuFile.setTitle(_translate("Main", "File"))
        self.menuHelp.setTitle(_translate("Main", "Settings"))
        self.menuAbout.setTitle(_translate("Main", "Help"))
        self.menuPlus.setTitle(_translate("Main", "Plus+"))
        self.actionSetting.setText(_translate("Main", "Database"))
        self.actionFlie.setText(_translate("Main", "Quit"))
        self.actionAbout.setText(_translate("Main", "About"))
        self.actionVersion_Postgres.setText(_translate("Main", "Version Postgres"))
        self.action_ClaimCode.setText(_translate("Main", "ยกเลิก ClaimCode"))




    def checkVersionPsql(self):

        if self.config_test() == True:
            dbname, user, host, password = self.get_config()  # get function get_config
            text = "dbname={} user={} host={} password={} connect_timeout=1".format(dbname, user, host, password)

            # Connect to your postgres DB
            conn = psycopg2.connect(text)
            # Open a cursor to perform database operations
            cur = conn.cursor()
            # Execute a query
            cur.execute("SHOW server_version;")
            # Retrieve query results
            records = cur.fetchone()
            cur.close()
            conn.close()
            # self.show_error_postgres(records[0])
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText(" Version Postgres " + records[0])
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)

            x = msg.exec_()
        else:
            self.databaseForm()


    def checkAutoUpdate(self):
        if ServerAutoUpdate == 'offline':
            print("offline")
            self.show_error_offline()
        else:
            if float(__version__) == float(ServerAutoUpdate):
                return False
            else:
                return True

    def closescr(self, Main): ## close App
        Main.close()


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
        # print(Main)
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

            local_version_hos = records[0]
            # print(self.file_app_version_test())
            #  No update DB and No file verions_current
            if server_version_hos == 'offline':
                self.show_error_offline()
                if choice == "Hos":
                    if path.exists('HospitalOS.exe') == True:
                        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'HospitalOS.exe', None, None, 10)
                        self.btnHos.setEnabled(False)
                        self.btnAdmin.setEnabled(True)
                        self.btnReportCenter.setEnabled(True)
                    else:
                        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'run_mod.bat', None, None, 10)
                        self.btnHos.setEnabled(False)
                        self.btnAdmin.setEnabled(True)
                        self.btnReportCenter.setEnabled(True)
                elif choice == "Admin":
                    if path.exists('HospitalOSSetup.exe') == True:
                        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'HospitalOSSetup.exe', None, None, 10)
                        self.btnHos.setEnabled(True)
                        self.btnAdmin.setEnabled(False)
                        self.btnReportCenter.setEnabled(True)
                    else:
                        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'setup_mod.bat', None, None, 10)
                        self.btnHos.setEnabled(True)
                        self.btnAdmin.setEnabled(False)
                        self.btnReportCenter.setEnabled(True)
                elif choice == "Report":
                    if path.exists('Report.exe') == True:
                        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'Report.exe', None, None, 10)
                        self.btnHos.setEnabled(True)
                        self.btnAdmin.setEnabled(True)
                        self.btnReportCenter.setEnabled(False)
                    else:
                        ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'report_mod.bat', None, None, 10)
                        self.btnHos.setEnabled(True)
                        self.btnAdmin.setEnabled(True)
                        self.btnReportCenter.setEnabled(False)
            else:

                if int(local_version_hos) < int(server_version_hos) and self.file_app_version_test() == False:
                    self.show_popup1(server_version_hos, records[0])
                # update DB but No file verions_current
                elif int(local_version_hos) == int(server_version_hos) and self.file_app_version_test() == False:
                    self.show_popup2(server_version_hos, records[0])
                # No update DB < server file < server = update
                elif int(self.file_app_version_test()) < int(server_version_hos):
                    self.show_popup1(server_version_hos, records[0])
                else:
                    if choice == "Hos":
                        if path.exists('HospitalOS.exe') == True:
                            ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'HospitalOS.exe', None, None, 10)
                            self.btnHos.setEnabled(False)
                            self.btnAdmin.setEnabled(True)
                            self.btnReportCenter.setEnabled(True)
                        else:
                            ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'run_mod.bat', None, None, 10)
                            self.btnHos.setEnabled(False)
                            self.btnAdmin.setEnabled(True)
                            self.btnReportCenter.setEnabled(True)
                    elif choice == "Admin":
                        if path.exists('HospitalOSSetup.exe') == True:
                            ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'HospitalOSSetup.exe', None, None, 10)
                            self.btnHos.setEnabled(True)
                            self.btnAdmin.setEnabled(False)
                            self.btnReportCenter.setEnabled(True)
                        else:
                            ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'setup_mod.bat', None, None, 10)
                            self.btnHos.setEnabled(True)
                            self.btnAdmin.setEnabled(False)
                            self.btnReportCenter.setEnabled(True)
                    elif choice == "Report":
                        if path.exists('Report.exe') == True:
                            ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'Report.exe', None, None, 10)
                            self.btnHos.setEnabled(True)
                            self.btnAdmin.setEnabled(True)
                            self.btnReportCenter.setEnabled(False)
                        else:
                            ctypes.windll.Shell32.ShellExecuteW(0, 'open', 'report_mod.bat', None, None, 10)
                            self.btnHos.setEnabled(True)
                            self.btnAdmin.setEnabled(True)
                            self.btnReportCenter.setEnabled(False)
        else:
            self.databaseForm()

    def AlertCheckVersionApp(self):

        msg = QMessageBox()
        msg.setWindowTitle("ตรวจพบ App มีเวอร์ชั่นใหม่ " + str(ServerAutoUpdate) + " !! ")
        msg.setText("เลือก Menu Help >> เลือก Update")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setDetailedText("**ปัจจุบัน Auto Update " + __version__)


        x = msg.exec_()

    def AlertCheckVersionInApp(self, Main):
        if ServerAutoUpdate == 'offline':
            # print('offline')
            self.show_error_offline()
        else:

            if float(__version__) == float(ServerAutoUpdate):
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("โปรแกรมเป็นเวอร์ชั่นปัจจุบันแล้ว")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setDetailedText("**ปัจจุบัน Auto Update " + __version__)
                x = msg.exec_()
            else:
                Main.close()
                self.bar_download_app()



    def show_popup1(self, records, server_version_hos):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("ตรวจพบ Hospital-OS NHSO มีเวอร์ชั่นใหม่ " + records + " !! ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText("ต้องการอัพเดท หรือไม่")
        msg.setDetailedText("**ปัจจุบัน Hospital-OS NHSO verion" + server_version_hos)

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


    def show_error_postgres(self, a ):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Error SQL Database HospitalOS : ")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText(a)

        x = msg.exec_()

    def show_error_offline(self):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Error Server Check Update Offline")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()



    def popup_button1(self, answer):
        if answer.text() == 'OK':
            try:
                dbname, user, host, password = self.get_config()
                text = "dbname={} user={} host={} password={} connect_timeout=1".format(dbname, user, host, password)
                conn = psycopg2.connect(text)
                cur = conn.cursor()
                cur2 = conn.cursor()
                cur2.execute("select max(replace(version_db,'.','')) from s_version")
                records2 = cur2.fetchone()
                if int(records2[0]) < int(server_version_hos_db):
                    cur.execute(sql_hos_update_server)
                    conn.commit()
            except:
                # self.show_error_database
                self.show_error_postgres("Postgresql unable to connect to the database.")
            else:
                cur.close()
                conn.close()
                # print(answer.text())
                self.bar_download() ## update patch

    def popup_button2(self, answer):
        if answer.text() == 'OK':
            self.bar_download()


    def bar_download(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_formProgressBar()
        self.ui.setupUi(self.window)
        self.window.show()

    def bar_download_app(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_formProgressBarApp()
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
