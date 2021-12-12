from configparser import Error
import sys
import os

from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PyQt5.QtCore import QSize

from widgets.urlListWidget import UrlListWidget
from widgets.select_default_download_folder import SelectDefaultDownloadFolder

from utils.alerts import show_error_alert

iconSrc = (os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'src' + os.path.sep + 'img' + os.path.sep + 'logo.png'
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowIcon(QtGui.QIcon(iconSrc))
        self.setFixedSize(690, 435) 
        self.setWindowTitle("NSTK soundcloud downloader") 

        layout = QVBoxLayout()

        widgets = [
            UrlListWidget,
            SelectDefaultDownloadFolder
        ]

        for w in widgets:
            layout.addWidget(w())
        
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


stylesheet = """
    QMainWindow {
        background-image: url(""" + iconSrc + """); 
        background-repeat: no-repeat; 
        background-position: right;
        background-color: black;
    }
"""

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon((QtGui.QIcon(iconSrc)))
        app.setStyleSheet(stylesheet)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit( app.exec_() )
    except Error:
        show_error_alert(current_widget=mainWin,message="Ha ocurrido un error",submessage=Error.message )

