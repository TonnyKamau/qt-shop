# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 656)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: #00394D;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(611, 461))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(-260, 30, 16, 451))
        self.line.setStyleSheet("border-left:2px solid #8585ad;\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(220, 80, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(72)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:transparent;\n"
"color:green;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(180, 200, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:transparent;\n"
"color:white;\n"
"font: 87 11pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.pin = QtWidgets.QLineEdit(self.frame)
        self.pin.setGeometry(QtCore.QRect(90, 260, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pin.setFont(font)
        self.pin.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"border-radius:5px;\n"
"border: 2px solid #8585ad;\n"
"color:white;\n"
"    font: 87 11pt \"Arial Black\";\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid #00b36b;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")
        self.pin.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.pin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pin.setAlignment(QtCore.Qt.AlignCenter)
        self.pin.setDragEnabled(False)
        self.pin.setClearButtonEnabled(True)
        self.pin.setObjectName("pin")
        self.loginbtn = QtWidgets.QPushButton(self.frame)
        self.loginbtn.setGeometry(QtCore.QRect(460, 260, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.loginbtn.setFont(font)
        self.loginbtn.setStyleSheet("\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border-radius:15px;\n"
"color:white;\n"
"    font: 87 12pt \"Arial Black\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.loginbtn.setObjectName("loginbtn")
        self.frame_error = QtWidgets.QFrame(self.frame)
        self.frame_error.setGeometry(QtCore.QRect(80, 10, 450, 30))
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.gridLayout.addWidget(self.frame, 1, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "֎"))
        self.label_4.setText(_translate("MainWindow", "Welcome To Shopify"))
        self.pin.setPlaceholderText(_translate("MainWindow", "Enter pin-Code"))
        self.loginbtn.setText(_translate("MainWindow", "Access"))
        self.loginbtn.setShortcut(_translate("MainWindow", "Return"))
        self.label_error.setText(_translate("MainWindow", "Error"))
