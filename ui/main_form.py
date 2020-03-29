# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txtSource = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSource.setObjectName("txtSource")
        self.gridLayout.addWidget(self.txtSource, 1, 0, 1, 3)
        self.lblEnterWord = QtWidgets.QLabel(self.centralwidget)
        self.lblEnterWord.setObjectName("lblEnterWord")
        self.gridLayout.addWidget(self.lblEnterWord, 0, 0, 1, 3)
        self.wpmSlider = QtWidgets.QSlider(self.centralwidget)
        self.wpmSlider.setMaximum(50)
        self.wpmSlider.setSingleStep(1)
        self.wpmSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wpmSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.wpmSlider.setObjectName("wpmSlider")
        self.gridLayout.addWidget(self.wpmSlider, 4, 0, 1, 1)
        self.gbSoundType = QtWidgets.QGroupBox(self.centralwidget)
        self.gbSoundType.setAlignment(QtCore.Qt.AlignCenter)
        self.gbSoundType.setObjectName("gbSoundType")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbSoundType)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addWidget(self.gbSoundType, 2, 0, 1, 1)
        self.lblTranspeed = QtWidgets.QLabel(self.centralwidget)
        self.lblTranspeed.setObjectName("lblTranspeed")
        self.gridLayout.addWidget(self.lblTranspeed, 3, 0, 1, 1)
        self.btnSendMorse = QtWidgets.QPushButton(self.centralwidget)
        self.btnSendMorse.setObjectName("btnSendMorse")
        self.gridLayout.addWidget(self.btnSendMorse, 5, 0, 1, 1)
        self.lblAlpha = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAlpha.sizePolicy().hasHeightForWidth())
        self.lblAlpha.setSizePolicy(sizePolicy)
        self.lblAlpha.setMinimumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lblAlpha.setFont(font)
        self.lblAlpha.setStyleSheet("color: rgb(255, 255, 0);\n"
"")
        self.lblAlpha.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblAlpha.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblAlpha.setText("")
        self.lblAlpha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAlpha.setObjectName("lblAlpha")
        self.gridLayout.addWidget(self.lblAlpha, 3, 1, 3, 1)
        self.lblMorse = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMorse.sizePolicy().hasHeightForWidth())
        self.lblMorse.setSizePolicy(sizePolicy)
        self.lblMorse.setMinimumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lblMorse.setFont(font)
        self.lblMorse.setStyleSheet("color: rgb(255, 255, 0);")
        self.lblMorse.setText("")
        self.lblMorse.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMorse.setObjectName("lblMorse")
        self.gridLayout.addWidget(self.lblMorse, 3, 2, 3, 1)
        self.txtCypher = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCypher.setObjectName("txtCypher")
        self.gridLayout.addWidget(self.txtCypher, 6, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuMorse = QtWidgets.QMenu(self.menubar)
        self.menuMorse.setObjectName("menuMorse")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.actionLearn = QtWidgets.QAction(MainWindow)
        self.actionLearn.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/imgs/mkey2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLearn.setIcon(icon)
        self.actionLearn.setObjectName("actionLearn")
        self.actionLetter = QtWidgets.QAction(MainWindow)
        self.actionLetter.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/imgs/morse-code.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLetter.setIcon(icon1)
        self.actionLetter.setObjectName("actionLetter")
        self.actionPlay_space_holder = QtWidgets.QAction(MainWindow)
        self.actionPlay_space_holder.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/imgs/morsekey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay_space_holder.setIcon(icon2)
        self.actionPlay_space_holder.setObjectName("actionPlay_space_holder")
        self.actionLightbulb_simmulator = QtWidgets.QAction(MainWindow)
        self.actionLightbulb_simmulator.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/imgs/flashlight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLightbulb_simmulator.setIcon(icon3)
        self.actionLightbulb_simmulator.setObjectName("actionLightbulb_simmulator")
        self.menu_File.addAction(self.actionE_xit)
        self.menuMorse.addAction(self.actionLearn)
        self.menuMorse.addAction(self.actionLetter)
        self.menuMorse.addAction(self.actionPlay_space_holder)
        self.menuMorse.addAction(self.actionLightbulb_simmulator)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuMorse.menuAction())
        self.toolBar.addAction(self.actionLearn)
        self.toolBar.addAction(self.actionLetter)
        self.toolBar.addAction(self.actionPlay_space_holder)
        self.toolBar.addAction(self.actionLightbulb_simmulator)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblEnterWord.setText(_translate("MainWindow", "Enter the word or phrase you want to send in morse code:"))
        self.gbSoundType.setTitle(_translate("MainWindow", "Sound type"))
        self.lblTranspeed.setText(_translate("MainWindow", "Transmission speed:"))
        self.btnSendMorse.setText(_translate("MainWindow", "Send Morse"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuMorse.setTitle(_translate("MainWindow", "Morse"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit"))
        self.actionLearn.setText(_translate("MainWindow", "Sound for each letter"))
        self.actionLearn.setToolTip(_translate("MainWindow", "Sound for each letter"))
        self.actionLearn.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionLetter.setText(_translate("MainWindow", "Sound between letters"))
        self.actionLetter.setToolTip(_translate("MainWindow", "Sound between letters"))
        self.actionPlay_space_holder.setText(_translate("MainWindow", "Play space holder"))
        self.actionLightbulb_simmulator.setText(_translate("MainWindow", "Lightbulb simulator"))
import images_rc
