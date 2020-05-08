import os, time
import logging
from common.config_utils import config

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '..', config.get_log_path)

class LogUtils:
    def __init__(self, logger=None):
        self.log_name = os.path.join(log_path, 'UITest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(config.get_log_level)

        self.file_log = logging.FileHandler(self.log_name, 'w', encoding='utf-8')
        self.file_log.setLevel(config.get_log_level)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(config.get_log_level)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.file_log.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.file_log)
        self.logger.addHandler(self.ch)
        self.file_log.close()
        self.ch.close()

    def get_log(self):
        return self.logger

logger = LogUtils().get_log()

if __name__=='__main__':
    logger.info('newdream')