from configparser import Error
import sys
import os

from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout
from PyQt5.QtCore import QSize
from PyQt5.QtCore import  Qt

from widgets.urlListWidget import UrlListWidget
from widgets.select_default_download_folder import SelectDefaultDownloadFolder
from widgets.annoying_music_player import AnnoyingMusicPlayer

from utils.alerts import show_error_alert

iconSrc = (os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'src' + os.path.sep + 'img' + os.path.sep + 'logo.png'
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        try:
            self.setWindowIcon(QtGui.QIcon(iconSrc))
            self.setFixedSize(690, 435) 
            self.setWindowTitle("NSTK soundcloud downloader") 

            layout = QGridLayout()

            widgets = [
                UrlListWidget,
                SelectDefaultDownloadFolder,
                AnnoyingMusicPlayer
            ]

            
            layout.addWidget(UrlListWidget(),0,0,Qt.AlignLeft)
            layout.addWidget(AnnoyingMusicPlayer(),1,1, Qt.AlignCenter)
            layout.addWidget(SelectDefaultDownloadFolder(),1,0, Qt.AlignCenter)

            
            widget = QWidget()
            widget.setLayout(layout)

            # Set the central widget of the Window. Widget will expand
            # to take up all the space in the window by default.
            self.setCentralWidget(widget)
        except Error:
            show_error_alert(current_widget=self,message="Ha ocurrido un error",submessage=Error.message )



stylesheet = """
    QMainWindow {
        background-image: url(""" + iconSrc + """); 
        background-repeat: no-repeat; 
        background-position: right;
        background-color: black;
    }
"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon((QtGui.QIcon(iconSrc)))
    app.setStyleSheet(stylesheet)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
    
