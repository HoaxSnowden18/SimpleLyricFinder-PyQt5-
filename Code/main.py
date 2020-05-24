# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyLyrics import PyLyrics

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 573)
        MainWindow.setMinimumSize(QtCore.QSize(378, 573))
        MainWindow.setMaximumSize(QtCore.QSize(378, 573))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"    color: white;\n"
"    font-family: Cambria;\n"
"}\n"
"\n"
"QFrame{\n"
"    background-color: rgba(0,0,0,180);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QScrollArea QWidget{\n"
"    background-color: rgba(0,0,0,8);\n"
"}\n"
"\n"
"QLabel{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: white;\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"     border-bottom: 1px solid rgb(255, 18,1);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(10,10,10,100);\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 18,1);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 10, 301, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.find = QtWidgets.QPushButton(self.frame)
        self.find.setGeometry(QtCore.QRect(40, 130, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.find.setFont(font)
        self.find.setObjectName("find")
        self.songArt = QtWidgets.QLineEdit(self.frame)
        self.songArt.setGeometry(QtCore.QRect(10, 49, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.songArt.setFont(font)
        self.songArt.setObjectName("songArt")
        self.songTitle = QtWidgets.QLineEdit(self.frame)
        self.songTitle.setGeometry(QtCore.QRect(10, 90, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.songTitle.setFont(font)
        self.songTitle.setObjectName("songTitle")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 921, 611))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("images/11.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 190, 301, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 301, 371))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lyrics = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.lyrics.setGeometry(QtCore.QRect(10, 10, 281, 331))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lyrics.setFont(font)
        self.lyrics.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.lyrics.setReadOnly(True)
        self.lyrics.setObjectName("lyrics")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.bg.raise_()
        self.frame.raise_()
        self.scrollArea.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.find.clicked.connect(self.findLy)

    def findLy(self):
    	artist = self.songArt.text()
    	song = self.songTitle.text()
    	try:
    		ly = PyLyrics.getLyrics(artist, song)
    	except ValueError:
    		self.showDialog()
    	else:
    		self.lyrics.setPlainText(ly)

    def showDialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("Search Error")
        msg.setText("The Song Artist or Song Title You Entered is not Valid")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.find.setText(_translate("MainWindow", "Find!"))
        self.songArt.setPlaceholderText(_translate("MainWindow", "Enter Song Artist"))
        self.songTitle.setPlaceholderText(_translate("MainWindow", "Enter Song Title"))
        self.label.setText(_translate("MainWindow", "Song Lyric Finder"))
        self.lyrics.setPlainText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
