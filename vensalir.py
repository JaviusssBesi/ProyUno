# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vensalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgSalir(object):
    def setupUi(self, dlgSalir):
        dlgSalir.setObjectName("dlgSalir")
        dlgSalir.resize(376, 150)
        dlgSalir.setModal(True)
        self.btnBoxSalir = QtWidgets.QDialogButtonBox(dlgSalir)
        self.btnBoxSalir.setGeometry(QtCore.QRect(150, 80, 161, 32))
        self.btnBoxSalir.setOrientation(QtCore.Qt.Horizontal)
        self.btnBoxSalir.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxSalir.setCenterButtons(True)
        self.btnBoxSalir.setObjectName("btnBoxSalir")
        self.lblMensalir = QtWidgets.QLabel(dlgSalir)
        self.lblMensalir.setGeometry(QtCore.QRect(90, 40, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblMensalir.setFont(font)
        self.lblMensalir.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblMensalir.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblMensalir.setObjectName("lblMensalir")
        self.label = QtWidgets.QLabel(dlgSalir)
        self.label.setGeometry(QtCore.QRect(20, 40, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/iconoaviso.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(dlgSalir)
        self.btnBoxSalir.accepted.connect(dlgSalir.accept)
        self.btnBoxSalir.rejected.connect(dlgSalir.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgSalir)

    def retranslateUi(self, dlgSalir):
        _translate = QtCore.QCoreApplication.translate
        dlgSalir.setWindowTitle(_translate("dlgSalir", "Salir"))
        self.lblMensalir.setText(_translate("dlgSalir", "¿Está seguro que desea salir de la aplicación?"))
import avisosalir_rc
