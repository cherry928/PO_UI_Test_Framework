import os
from selenium import webdriver

class chrome_driver:
    def __init__(self):
        current_path = os.path.dirname(__file__)
        driver_path = os.path.join(current_path, '../webdriver/chromedriver')
        self.__driver = webdriver.Chrome(executable_path=driver_path)

    @property
    def get_driver(self):
        value = self.__driver
        return value

chromedriver = chrome_driver()
