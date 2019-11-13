# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from forky import *
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(279, 592)

        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(120, 160, 16, 160))
        self.verticalSlider.setMinimum(-314)
        self.verticalSlider.setMaximum(314)
        self.verticalSlider.setProperty("value", 0)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.verticalSlider_2 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_2.setGeometry(QtCore.QRect(60, 80, 16, 160))
        self.verticalSlider_2.setMinimum(-314)
        self.verticalSlider_2.setMaximum(314)
        self.verticalSlider_2.setProperty("value", 0)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_3.setGeometry(QtCore.QRect(10, 10, 16, 160))
        self.verticalSlider_3.setMinimum(-314)
        self.verticalSlider_3.setMaximum(314)
        self.verticalSlider_3.setProperty("value", 0)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_4 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_4.setGeometry(QtCore.QRect(180, 80, 16, 160))
        self.verticalSlider_4.setMinimum(-314)
        self.verticalSlider_4.setMaximum(314)
        self.verticalSlider_4.setProperty("value", 0)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalSlider_5 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_5.setGeometry(QtCore.QRect(250, 10, 16, 160))
        self.verticalSlider_5.setMinimum(-314)
        self.verticalSlider_5.setMaximum(314)
        self.verticalSlider_5.setProperty("value", 0)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 350, 50, 25))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 400, 50, 25))
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 450, 50, 25))
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 330, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 380, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 430, 67, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 500, 50, 25))
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 550, 50, 25))
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 480, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 530, 67, 17))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 550, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 330, 181, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.get_sliderValue)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.lineEdit_2.setText(_translate("Dialog", "0"))
        self.lineEdit_3.setText(_translate("Dialog", "0"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.lineEdit_4.setText(_translate("Dialog", "0"))
        self.lineEdit_5.setText(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))

    def get_sliderValue(self, value):
        print(value)
        #return self.verticalSlider.value()

class ImageWidget(QtWidgets.QWidget):
    def __init__(self,scene,parent=None):
        super(ImageWidget,self).__init__(parent)
        self.scene = scene
        self.w=self.scene.get_width()
        self.h=self.scene.get_height()
        self.scene.draw()
        self.data= self.scene.get_surface().get_buffer().raw
        self.image=QtGui.QImage(self.data,self.w,self.h,QtGui.QImage.Format_RGB32)

    def updateDraw(self):

        self.scene.draw()
        self.data = self.scene.get_surface().get_buffer().raw
        self.image=QtGui.QImage(self.data,self.w,self.h,QtGui.QImage.Format_RGB32)

    def paintEvent(self,event):
        qp=QtGui.QPainter()
        qp.begin(self)
        self.updateDraw()
        qp.drawImage(0,0,self.image)
        qp.end()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,scene,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setCentralWidget(ImageWidget(scene))
        ui = Ui_Dialog()
        ui.setupUi(self)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    sc = scene()
    w=MainWindow(sc)
    w.show()
    app.exec_()
