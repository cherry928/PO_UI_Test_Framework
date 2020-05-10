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
    def testdata_path(self):
        testdata_path_value = self.read_ini('default', 'testdata_path')
        return testdata_path_value

    @property
    def report_path(self):
        report_path_value = self.read_ini('default', 'report_path')
        return report_path_value

    @property
    def case_path(self):
        case_path_value = self.read_ini('default', 'case_path')
        return case_path_value

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

    @property
    def element_info_path(self):
        element_info_path_value = self.read_ini('default', 'element_info_path')
        return element_info_path_value

    @property
    def smtp_server(self):
        smtp_server_value = self.read_ini('email', 'smtp_server')
        return smtp_server_value

    @property
    def smtp_sender(self):
        smtp_sender_value = self.read_ini('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def smtp_senderpassword(self):
        smtp_senderpassword_value = self.read_ini('email', 'smtp_senderpassword')
        return smtp_senderpassword_value

    @property
    def smtp_receiver(self):
        smtp_receiver_value = self.read_ini('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def smtp_cc(self):
        smtp_cc_value = self.read_ini('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def smtp_subject(self):
        smtp_subject_value = self.read_ini('email', 'smtp_subject')
        return smtp_subject_value

config = Config_utils()

if __name__=='__main__':
    config_u = Config_utils()
    print((config_u.testdata_path))