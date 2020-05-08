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
    def get_url_path(self):
        value = self.read_ini('default', 'url')
        return value

    @property
    def get_log_path(self):
        value = self.read_ini('default','log_path')
        return value

    @property
    def get_log_level(self):
        value = int(self.read_ini('default', 'log_level'))
        return value

    @property
    def driver_path(self):
        driver_path_value = self.read_ini('default', 'driver_path')
        return driver_path_value

    @property
    def time_out(self):
        driver_time_value = float(self.read_ini('default', 'time_out'))
        return driver_time_value

    @property
    def screen_shot_path(self):
        screen_shot_path_value = self.read_ini('default', 'screen_shot_path')
        return screen_shot_path_value

    @property
    def user_name(self):
        user_name_value = self.read_ini('default', 'user_name')
        return user_name_value

    @property
    def pass_word(self):
        pass_word_value = self.read_ini('default', 'pass_word')
        return pass_word_value

    @property
    def driver_name(self):
        driver_name_value = self.read_ini('default', 'driver_name')
        return driver_name_value

config = Config_utils()

if __name__=='__main__':
    config_u = Config_utils()
    print((config_u.get_log_level))