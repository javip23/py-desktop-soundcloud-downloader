
from os import name
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.Qt import QApplication, QTextCursor
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QCheckBox, QMessageBox
from PyQt5.QtCore import  Qt

from utils.config import get_user_settings, update_user_settings


class SelectDefaultDownloadFolder(QWidget):
      def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        
        self.setFixedWidth(500)
        
        self.layout = QGridLayout(self)

        # Shows the destination url if selected
        destination_url_textbox_label = QLabel(self)
        destination_url_textbox_label.setText("Carpeta de destino:")
        destination_url_textbox_label.setStyleSheet('color: white; font-size: 15px;')
        destination_url_textbox_label.move(10, 35)

        self.destination_url_textbox = QLineEdit(self)
        self.destination_url_textbox.setPlaceholderText("Por defecto es Descargas")
        self.destination_url_textbox.setReadOnly(True)
        self.destination_url_textbox.setFixedWidth(385)
        self.destination_path =  get_user_settings(namespace="DOWNLOADSETTINGS", key="base_download_folder")
        if self.destination_path:
          self.destination_url_textbox.setText(self.destination_path)

        # Add select button
        
        self.select_button = QPushButton()
        self.select_button.setText("Seleccionar")
        self.select_button.clicked.connect(self.select_destination_url)
        self.select_button.move(10,0)


        self.layout.addWidget(destination_url_textbox_label,0,0,1,0,Qt.AlignLeft)
        self.layout.addWidget(self.destination_url_textbox, 1,0, Qt.AlignCenter) 
        self.layout.addWidget(self.select_button,1,1, Qt.AlignCenter) 

      def select_destination_url(self):
        self.destination_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Selecciona una carpeta de destino')
        self.destination_url_textbox.setText(self.destination_path)
        update_user_settings(namespace='DOWNLOADSETTINGS',key="base_download_folder", value=self.destination_path.__str__())