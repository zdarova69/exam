from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from main_ui import *
import cv2

def play_photo():
    img = cv2.imread('wed.jpg')
    cv2.imshow('Result', img)

def  Play_Video():
        cap = cv2.VideoCapture('video.mp4')

        while True:
            success, img = cap.read()
            cv2.imshow('Result', img)
            if cv2.waitKey(1) & ord('q') == 0xFF:
                break

class main(QtWidgets.QWidget, main_ui):
    def __init__(self):
        super().__init__()
        self.ui = main_ui()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.change_window)
        self.ui.button_video.clicked.connect(Play_Video)
        self.ui.button_photo.clicked.connect(play_photo)

    def change_window(self):
               
        self.comp = another_123()    
        self.comp.show()
    
    
        
class another_123(QtWidgets.QWidget, another_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.back_window)
        
        
    def back_window(self):
        
        self.comp = main() 
        self.comp.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = main()
    mywin.show()
    sys.exit(app.exec_())