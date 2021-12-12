
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QPlainTextEdit, QVBoxLayout, QCheckBox, QMessageBox
from PyQt5.QtCore import  Qt, QUrl
from PyQt5.QtMultimedia import *

class AnnoyingMusicPlayer(QWidget):
    """
    Un guiño a los miticos keygen (que todos alguna vez hemos usado)
    con la musica que no se podía quitar (pero esta sí)
    """
    def __init__(self,*args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setFixedWidth(100)
        self.layout = QVBoxLayout(self)

        self.player = None

        self.play_button_label = QLabel(self)
        self.play_button_label.setText("Música")
        self.play_button_label.setStyleSheet('color: white; font-size: 15px;')

        self.play_button = QPushButton(self)
        self.play_button.setStyleSheet('font-size: 20px;')
        self.play_button.setFixedSize(30,30)
        self.play_button.clicked.connect(self.start_or_stop_music)

        self.layout.addWidget(self.play_button_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.play_button, alignment=Qt.AlignCenter)
        
        self.generate_music_player()

    def show_play_button(self):
        self.play_button.setText(u"\u23F5")
        self.play_button.setStyleSheet('font-size: 25px;')

    def show_pause_button(self):
        self.play_button.setText(u"\u23F8")
        self.play_button.setStyleSheet('font-size: 15px;')
        
    
    def start_or_stop_music(self):          
        if self.music_playing:
            self.player.stop()
            self.show_play_button()   
        else:
            self.player.play()
            self.show_pause_button()
        self.music_playing = not self.music_playing
            
    def generate_music_player(self):
        playlist = QMediaPlaylist(self)
        url = QUrl.fromLocalFile('/home/javi/git/py-desktop-soundcloud-downloader/app/src/sound/annoying_music_keygen_like.mp3')
        playlist.addMedia(QMediaContent(url))
        playlist.setPlaybackMode(QMediaPlaylist.Loop)
        playlist.setCurrentIndex(0)

        self.player = QMediaPlayer(self)
        self.player.setPlaylist(playlist)
        self.player.setVolume(25)
        self.player.play()
        self.show_pause_button()
        self.music_playing = True

