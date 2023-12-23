from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import sys


class main_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(618, 469)
        Dialog.setStyleSheet("background-color: rgb(0, 255, 255);")
        Dialog.setWindowIcon(QIcon('wed.jpg'))

        self.central_widget =QtWidgets.QWidget(Dialog)
        self.central_widget.setObjectName('central widget')

         

        self.labels = QtWidgets.QLabel(self.central_widget)
        self.labels.setGeometry(QtCore.QRect(200, 50, 300, 100))
        self.labels.setStyleSheet('background-color: yellow')
        self.labels.setObjectName('labels')

        
        self.button = QtWidgets.QPushButton(self.central_widget)
        self.button.setGeometry(QtCore.QRect(50, 50, 100, 100))
        self.button.setStyleSheet('background-color: yellow')
        self.button.setObjectName('button')

        self.button_video = QtWidgets.QPushButton(self.central_widget)
        self.button_video.setGeometry(QtCore.QRect(50, 150, 75, 150))
        self.button_video.setStyleSheet('background-color: yellow')
        self.button_video.setObjectName('button')

        self.button_photo = QtWidgets.QPushButton(self.central_widget)
        self.button_photo.setGeometry(QtCore.QRect(200, 200, 250, 250))
        self.button_photo.setStyleSheet('background-color: yellow')
        self.button_photo.setObjectName('button')


        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")

        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate('Dialog', 'Dialog'))

        self.button.setText(_translate('Dialog', 'кнопка'))
        self.button_video.setText(_translate('Dialog', 'видео'))
        self.button_photo.setText(_translate('Dialog', 'фото'))

        self.labels.setText(_translate("Dialog", "Анаконда"))

class another_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540,612)

        self.central_widget =QtWidgets.QWidget(Dialog)
        self.central_widget.setObjectName('central widget')

        self.labels = QtWidgets.QLabel(self.central_widget)
        self.labels.setGeometry(QtCore.QRect(40, 10, 60, 20))
        self.labels.setStyleSheet('background-color: red')
        self.labels.setObjectName('labels')
        
        self.button = QtWidgets.QPushButton(self.central_widget)
        self.button.setGeometry(QtCore.QRect(50, 50, 100, 100))
        self.button.setStyleSheet('background-color: red')
        self.button.setObjectName('button')

   
        self.menubar = QtWidgets.QMenuBar(Dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
  
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
     
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate


        self.button.setText(_translate('Dialog', 'назад'))

        self.labels.setText(_translate("Dialog", "текст"))