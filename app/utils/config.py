from configparser import ConfigParser

def get_configuration(namespace, key):
    cfg = ConfigParser()
    cfg.read('etc/config.ini')
    return cfg.get(namespace,key)

def get_user_settings(namespace, key):
    cfg = ConfigParser()
    cfg.read('etc/usersettings.ini')
    return cfg.get(namespace,key)

def update_user_settings(namespace, key, value):
    cfg = ConfigParser()
    with open('etc/usersettings.ini') as f:
        cfg.read_file(f)
    cfg[namespace][key] = value 
    with open('etc/usersettings.ini', 'r+') as f:
        cfg.write(f)