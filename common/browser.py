import os
from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options

current_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join( current_path , '..', config.driver_path)

class Browser(object):
    def __init__(self, driver_path = dri_path):
        self.__driver_path = driver_path

    def get_chrome_dirver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        chrome_driver_path = os.path.join(self.__driver_path, 'chromedriver')
        __driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
        return __driver
