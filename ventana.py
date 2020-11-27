# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1133, 874)
        venPrincipal.setLayoutDirection(QtCore.Qt.LeftToRight)
        venPrincipal.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1040, 680))
        self.tabWidget.setMaximumSize(QtCore.QSize(1041, 681))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.panelCli = QtWidgets.QWidget()
        self.panelCli.setObjectName("panelCli")
        self.layoutWidget = QtWidgets.QWidget(self.panelCli)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 995, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblXestCli = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblXestCli.setFont(font)
        self.lblXestCli.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.488636, y1:0, x2:0.506, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.lblXestCli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXestCli.setObjectName("lblXestCli")
        self.gridLayout_5.addWidget(self.lblXestCli, 0, 0, 1, 1)
        self.lineSup = QtWidgets.QFrame(self.layoutWidget)
        self.lineSup.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSup.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSup.setObjectName("lineSup")
        self.gridLayout_5.addWidget(self.lineSup, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(75, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 4, 1, 1)
        self.btnBuscarCli = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBuscarCli.sizePolicy().hasHeightForWidth())
        self.btnBuscarCli.setSizePolicy(sizePolicy)
        self.btnBuscarCli.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarCli.setIcon(icon)
        self.btnBuscarCli.setIconSize(QtCore.QSize(24, 24))
        self.btnBuscarCli.setObjectName("btnBuscarCli")
        self.gridLayout_3.addWidget(self.btnBuscarCli, 0, 5, 1, 1)
        self.btnReloadCli = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReloadCli.sizePolicy().hasHeightForWidth())
        self.btnReloadCli.setSizePolicy(sizePolicy)
        self.btnReloadCli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReloadCli.setIcon(icon1)
        self.btnReloadCli.setIconSize(QtCore.QSize(24, 24))
        self.btnReloadCli.setObjectName("btnReloadCli")
        self.gridLayout_3.addWidget(self.btnReloadCli, 0, 6, 1, 1)
        self.lblClialta = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblClialta.sizePolicy().hasHeightForWidth())
        self.lblClialta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblClialta.setFont(font)
        self.lblClialta.setObjectName("lblClialta")
        self.gridLayout_3.addWidget(self.lblClialta, 0, 8, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalendar.sizePolicy().hasHeightForWidth())
        self.btnCalendar.setSizePolicy(sizePolicy)
        self.btnCalendar.setMaximumSize(QtCore.QSize(32, 32))
        self.btnCalendar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon2)
        self.btnCalendar.setIconSize(QtCore.QSize(30, 30))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridLayout_3.addWidget(self.btnCalendar, 0, 10, 1, 1)
        self.lblDni = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDni.sizePolicy().hasHeightForWidth())
        self.lblDni.setSizePolicy(sizePolicy)
        self.lblDni.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDni.setFont(font)
        self.lblDni.setObjectName("lblDni")
        self.gridLayout_3.addWidget(self.lblDni, 0, 1, 1, 1)
        self.editClialta = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClialta.sizePolicy().hasHeightForWidth())
        self.editClialta.setSizePolicy(sizePolicy)
        self.editClialta.setMinimumSize(QtCore.QSize(0, 0))
        self.editClialta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editClialta.setStyleSheet("background-color: rgba(255, 0, 0, 50);")
        self.editClialta.setAlignment(QtCore.Qt.AlignCenter)
        self.editClialta.setObjectName("editClialta")
        self.gridLayout_3.addWidget(self.editClialta, 0, 9, 1, 1)
        self.lblValidar = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidar.sizePolicy().hasHeightForWidth())
        self.lblValidar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValidar.setFont(font)
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.gridLayout_3.addWidget(self.lblValidar, 0, 3, 1, 1)
        self.editDni = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDni.sizePolicy().hasHeightForWidth())
        self.editDni.setSizePolicy(sizePolicy)
        self.editDni.setMinimumSize(QtCore.QSize(110, 0))
        self.editDni.setMaximumSize(QtCore.QSize(110, 16777215))
        self.editDni.setStyleSheet("background-color: rgba(255, 0, 0, 50);")
        self.editDni.setObjectName("editDni")
        self.gridLayout_3.addWidget(self.editDni, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(270, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 7, 1, 1)
        self.lblCodcli = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodcli.sizePolicy().hasHeightForWidth())
        self.lblCodcli.setSizePolicy(sizePolicy)
        self.lblCodcli.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCodcli.setFont(font)
        self.lblCodcli.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.lblCodcli.setText("")
        self.lblCodcli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCodcli.setObjectName("lblCodcli")
        self.gridLayout_3.addWidget(self.lblCodcli, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.editNome = QtWidgets.QLineEdit(self.layoutWidget)
        self.editNome.setStyleSheet("background-color: rgba(255, 0, 0, 50);")
        self.editNome.setObjectName("editNome")
        self.gridLayout.addWidget(self.editNome, 0, 4, 1, 1)
        self.lblNome = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.gridLayout.addWidget(self.lblNome, 0, 3, 1, 1)
        self.editApel = QtWidgets.QLineEdit(self.layoutWidget)
        self.editApel.setStyleSheet("background-color: rgba(255, 0, 0, 50);")
        self.editApel.setObjectName("editApel")
        self.gridLayout.addWidget(self.editApel, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.lblApel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.gridLayout.addWidget(self.lblApel, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblProv = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProv.sizePolicy().hasHeightForWidth())
        self.lblProv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.gridLayout_2.addWidget(self.lblProv, 0, 3, 1, 1)
        self.editDir = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDir.sizePolicy().hasHeightForWidth())
        self.editDir.setSizePolicy(sizePolicy)
        self.editDir.setStyleSheet("background-color: rgb(255, 0, 0, 50);")
        self.editDir.setObjectName("editDir")
        self.gridLayout_2.addWidget(self.editDir, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        self.cmbProv = QtWidgets.QComboBox(self.layoutWidget)
        self.cmbProv.setObjectName("cmbProv")
        self.gridLayout_2.addWidget(self.cmbProv, 0, 4, 1, 1)
        self.lblDir = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDir.sizePolicy().hasHeightForWidth())
        self.lblDir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.gridLayout_2.addWidget(self.lblDir, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblSexo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSexo.setObjectName("lblSexo")
        self.gridLayout_4.addWidget(self.lblSexo, 0, 0, 1, 1)
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtFem.setObjectName("rbtFem")
        self.gridLayout_4.addWidget(self.rbtFem, 0, 1, 1, 1)
        self.rbtMasc = QtWidgets.QRadioButton(self.layoutWidget)
        self.rbtMasc.setObjectName("rbtMasc")
        self.gridLayout_4.addWidget(self.rbtMasc, 0, 2, 1, 1)
        self.lblEdad = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEdad.setFont(font)
        self.lblEdad.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEdad.setObjectName("lblEdad")
        self.gridLayout_4.addWidget(self.lblEdad, 0, 3, 1, 1)
        self.spinEdad = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinEdad.setObjectName("spinEdad")
        self.gridLayout_4.addWidget(self.spinEdad, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 5, 1, 1)
        self.lblPago = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.gridLayout_4.addWidget(self.lblPago, 0, 6, 1, 1)
        self.chkEfec = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkEfec.setObjectName("chkEfec")
        self.gridLayout_4.addWidget(self.chkEfec, 0, 7, 1, 1)
        self.chkTar = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkTar.setObjectName("chkTar")
        self.gridLayout_4.addWidget(self.chkTar, 0, 8, 1, 1)
        self.chkTrans = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkTrans.setObjectName("chkTrans")
        self.gridLayout_4.addWidget(self.chkTrans, 0, 9, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 5, 0, 1, 1)
        self.lineInf = QtWidgets.QFrame(self.layoutWidget)
        self.lineInf.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineInf.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineInf.setObjectName("lineInf")
        self.gridLayout_5.addWidget(self.lineInf, 6, 0, 1, 1)
        self.tableCli = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableCli.setObjectName("tableCli")
        self.tableCli.setColumnCount(3)
        self.tableCli.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(2, item)
        self.tableCli.horizontalHeader().setDefaultSectionSize(322)
        self.gridLayout_5.addWidget(self.tableCli, 7, 0, 1, 1)
        self.griBotonCli = QtWidgets.QGridLayout()
        self.griBotonCli.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.griBotonCli.setContentsMargins(250, 0, 250, 0)
        self.griBotonCli.setObjectName("griBotonCli")
        self.btnModifCli = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifCli.sizePolicy().hasHeightForWidth())
        self.btnModifCli.setSizePolicy(sizePolicy)
        self.btnModifCli.setObjectName("btnModifCli")
        self.griBotonCli.addWidget(self.btnModifCli, 0, 1, 1, 1)
        self.btnAltaCli = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaCli.sizePolicy().hasHeightForWidth())
        self.btnAltaCli.setSizePolicy(sizePolicy)
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.griBotonCli.addWidget(self.btnAltaCli, 0, 0, 1, 1)
        self.btnLimpiarCli = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiarCli.sizePolicy().hasHeightForWidth())
        self.btnLimpiarCli.setSizePolicy(sizePolicy)
        self.btnLimpiarCli.setObjectName("btnLimpiarCli")
        self.griBotonCli.addWidget(self.btnLimpiarCli, 0, 3, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setObjectName("btnSalir")
        self.griBotonCli.addWidget(self.btnSalir, 0, 4, 1, 1)
        self.btnBajaCli = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaCli.sizePolicy().hasHeightForWidth())
        self.btnBajaCli.setSizePolicy(sizePolicy)
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.griBotonCli.addWidget(self.btnBajaCli, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.griBotonCli, 8, 0, 1, 1)
        self.tabWidget.addTab(self.panelCli, "")
        self.panelFac = QtWidgets.QWidget()
        self.panelFac.setObjectName("panelFac")
        self.tabWidget.addTab(self.panelFac, "")
        self.panelPro = QtWidgets.QWidget()
        self.panelPro.setObjectName("panelPro")
        self.tabWidget.addTab(self.panelPro, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.lblstatusdate = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblstatusdate.sizePolicy().hasHeightForWidth())
        self.lblstatusdate.setSizePolicy(sizePolicy)
        self.lblstatusdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblstatusdate.setObjectName("lblstatusdate")
        self.gridLayout_6.addWidget(self.lblstatusdate, 1, 0, 1, 1)
        self.lblstatus = QtWidgets.QLabel(self.centralwidget)
        self.lblstatus.setMinimumSize(QtCore.QSize(1040, 13))
        self.lblstatus.setMaximumSize(QtCore.QSize(1041, 14))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblstatus.setFont(font)
        self.lblstatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblstatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblstatus.setObjectName("lblstatus")
        self.gridLayout_6.addWidget(self.lblstatus, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 1, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem7, 1, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem8, 3, 1, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(venPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 26))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(venPrincipal)
        self.toolBar.setObjectName("toolBar")
        venPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolbarSalir = QtWidgets.QAction(venPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/salir/iconsalir.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarSalir.setIcon(icon3)
        self.toolbarSalir.setObjectName("toolbarSalir")
        self.toolbarBackup = QtWidgets.QAction(venPrincipal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/backup/backup32.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarBackup.setIcon(icon4)
        self.toolbarBackup.setObjectName("toolbarBackup")
        self.toolbarAbrirDir = QtWidgets.QAction(venPrincipal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/carpeta/abrircarpeta.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarAbrirDir.setIcon(icon5)
        self.toolbarAbrirDir.setObjectName("toolbarAbrirDir")
        self.toolbarPrinter = QtWidgets.QAction(venPrincipal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/printer/printer.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarPrinter.setIcon(icon6)
        self.toolbarPrinter.setObjectName("toolbarPrinter")
        self.menubarSalir = QtWidgets.QAction(venPrincipal)
        self.menubarSalir.setObjectName("menubarSalir")
        self.menuArchivo.addAction(self.menubarSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.toolBar.addAction(self.toolbarPrinter)
        self.toolBar.addAction(self.toolbarAbrirDir)
        self.toolBar.addAction(self.toolbarBackup)
        self.toolBar.addAction(self.toolbarSalir)

        self.retranslateUi(venPrincipal)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "MainWindow"))
        self.lblXestCli.setText(_translate("venPrincipal", "XESTIÓN CLIENTES"))
        self.lblClialta.setText(_translate("venPrincipal", "Fecha de Alta:"))
        self.lblDni.setText(_translate("venPrincipal", "DNI:"))
        self.lblNome.setText(_translate("venPrincipal", "Nome:"))
        self.lblApel.setText(_translate("venPrincipal", "Apelidos:"))
        self.lblProv.setText(_translate("venPrincipal", "Provincia:"))
        self.lblDir.setText(_translate("venPrincipal", "Dirección: "))
        self.lblSexo.setText(_translate("venPrincipal", "Sexo:  "))
        self.rbtFem.setText(_translate("venPrincipal", "Femenino"))
        self.rbtMasc.setText(_translate("venPrincipal", "Masculino"))
        self.lblEdad.setText(_translate("venPrincipal", "Edad:"))
        self.lblPago.setText(_translate("venPrincipal", "Métodos de Pago:  "))
        self.chkEfec.setText(_translate("venPrincipal", "Efectivo"))
        self.chkTar.setText(_translate("venPrincipal", "Tarjeta"))
        self.chkTrans.setText(_translate("venPrincipal", "Transferencia"))
        item = self.tableCli.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "DNI"))
        item = self.tableCli.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "Apelidos"))
        item = self.tableCli.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "Nome"))
        self.btnModifCli.setText(_translate("venPrincipal", "Modificar"))
        self.btnAltaCli.setText(_translate("venPrincipal", "Grabar"))
        self.btnLimpiarCli.setText(_translate("venPrincipal", "Limpiar"))
        self.btnSalir.setText(_translate("venPrincipal", "Salir"))
        self.btnBajaCli.setText(_translate("venPrincipal", "Eliminar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelCli), _translate("venPrincipal", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelFac), _translate("venPrincipal", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelPro), _translate("venPrincipal", "Productos"))
        self.lblstatusdate.setText(_translate("venPrincipal", "TextLabel"))
        self.lblstatus.setText(_translate("venPrincipal", "TextLabel"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.toolBar.setWindowTitle(_translate("venPrincipal", "toolBar"))
        self.toolbarSalir.setText(_translate("venPrincipal", "toolbarSalir"))
        self.toolbarSalir.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/salir/iconsalir.png\"/></p></body></html>"))
        self.toolbarBackup.setText(_translate("venPrincipal", "toolbarBackup"))
        self.toolbarBackup.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/backup/backup32.png\"/></p></body></html>"))
        self.toolbarAbrirDir.setText(_translate("venPrincipal", "toolbarAbrirDir"))
        self.toolbarAbrirDir.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/carpeta/abrircarpeta.png\"/></p></body></html>"))
        self.toolbarPrinter.setText(_translate("venPrincipal", "toolbarPrinter"))
        self.toolbarPrinter.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/printer/printer.png\"/><br/></p></body></html>"))
        self.menubarSalir.setText(_translate("venPrincipal", "menubarSalir"))
        self.menubarSalir.setShortcut(_translate("venPrincipal", "Alt+S"))
import abrirdirectorio_rc
import toolbarbackup_rc
import toolbarprinter_rc
import toolbarsalir_rc
