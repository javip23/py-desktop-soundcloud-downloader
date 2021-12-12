
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import  QMessageBox



def show_info_alert(current_widget,message, submessage="" ):
    msg = QMessageBox(current_widget)
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setInformativeText(submessage)
    msg.setWindowTitle("Información")
    msg.exec_()

def show_warning_alert(current_widget,message, submessage="" ):
    msg = QMessageBox(current_widget)
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setInformativeText(submessage)
    msg.setWindowTitle("¡Atención!")
    msg.exec_()

def show_error_alert(current_widget,message, submessage="" ):
    msg = QMessageBox(current_widget)
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setInformativeText(submessage)
    msg.setWindowTitle("¡Error!")
    msg.exec_()