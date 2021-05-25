

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormCancelClaimcode(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(391, 91)
        Form.setMinimumSize(QtCore.QSize(391, 91))
        Form.setMaximumSize(QtCore.QSize(391, 91))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(50, 10, 291, 61))
        self.groupBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.txt_visit_vn = QtWidgets.QLineEdit(self.groupBox)
        self.txt_visit_vn.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.txt_visit_vn.setObjectName("txt_visit_vn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ยกเลิก ClaimCode"))
        self.groupBox.setTitle(_translate("Form", "VN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormCancelClaimcode()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

