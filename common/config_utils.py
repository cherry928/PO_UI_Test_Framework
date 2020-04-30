import os
import configparser

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, '../conf/config.ini')

class Config_utils:
    def __init__(self, config_path=cfgpath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding="utf-8")
    def read_ini(self, sec, option):
        value = self.__conf.get(sec, option)
        return value
    @property
    def get_excel_path(self):
        value = self.read_ini('default','excel_path')
        return value
    @property
    def get_log_path(self):
        value = self.read_ini('default','log_path')
        return value
    @property
    def driver_path(self):
        driver_path_value = self.read_ini('default', 'driver_path')
        return driver_path_value

config = Config_utils()

if __name__=='__main__':
    config_u = Config_utils()
    print(config_u.get_excel_path)