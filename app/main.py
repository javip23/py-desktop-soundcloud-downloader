from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('etc/config.ini')

downloader = cfg.get('BASECONFIG','baseDownloader')

print(downloader)