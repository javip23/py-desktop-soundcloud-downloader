
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.Qt import QApplication, QTextCursor
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QPlainTextEdit, QVBoxLayout, QCheckBox
from PyQt5.QtCore import  Qt

class UrlListWidget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        
        self.setFixedWidth(420)
        
        self.layout = QVBoxLayout(self)

        # Add fields to paste urls
        url_list_textbox_label = QLabel(self)
        url_list_textbox_label.setText("Lista de temas:")
        url_list_textbox_label.setStyleSheet('color: white; font-size: 20px;')
        url_list_textbox_label.move(10, 35)

        self.auto_paste_from_clipboard = QCheckBox("Obtener enlaces automáticamente del portapapeles", self)
        self.auto_paste_from_clipboard.setStyleSheet("QCheckBox:unchecked{ color: white; }QCheckBox:checked{ background: black ; color: white; }")

        self.url_list = QPlainTextEdit(self)
        self.url_list.setPlaceholderText("Enlace 1\nEnlace 2\nEnlace 3\n...")
        self.url_list.move(10,70)
        self.url_list.setFixedSize(400,200)
        QApplication.instance().clipboard().dataChanged.connect(self.clipboardChanged)


        # Add download button
        
        download_button = QPushButton(self)
        download_button.setText("Descargar")
        download_button.setFixedSize(120,35)
        download_button.setStyleSheet('')
        self.download_button = download_button


        self.layout.addWidget(url_list_textbox_label, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.auto_paste_from_clipboard, alignment=Qt.AlignRight)
        self.layout.addWidget(self.url_list, alignment=Qt.AlignLeft, ) 
        self.layout.addWidget(self.download_button, alignment=Qt.AlignCenter) 

    def clipboardChanged(self):
        text = QApplication.instance().clipboard().text()
        if self.auto_paste_from_clipboard.isChecked():
            if "soundcloud" in text and text not in self.url_list.toPlainText():
                self.url_list.insertPlainText(text + "\n")
        else:
            urls_text = self.url_list.toPlainText()
            cursor = self.url_list.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.url_list.setTextCursor(cursor)
            self.url_list.setTextCursor(cursor)
            self.url_list.ensureCursorVisible() 
            if urls_text and urls_text[len(urls_text) -1] != "\n":
                self.url_list.insertPlainText("\n")

    
