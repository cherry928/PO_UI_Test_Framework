import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, '../webdriver/chromedriver')

class LoginPage:
    def __init__(self):  # 属性==》页面的控件
        self.dirver = webdriver.Chrome(executable_path=driver_path)
        self.dirver.implicitly_wait(10)
        self.dirver.maximize_window()
        self.dirver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.username_inputbox = self.dirver.find_element(By.XPATH, '//input[@id="account"]')
        self.password_inputbox = self.dirver.find_element(By.XPATH, '//input[@name="password"]')
        self.login_button = self.dirver.find_element(By.XPATH, '//button[@id="submit"]')
        self.keeplogin_checkbox = self.dirver.find_element(By.XPATH, '//input[@name="keepLogin[]"]')

    def input_username(self, username): # 方法==》控件的操作
        self.username_inputbox.send_keys(username)
        logger.info('用户名输入框输入：' + str(username))

    def input_password(self, password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入框输入：' + str(password))

    def click_login(self):
        self.login_button.click()
        logger.info('点击登录按钮')

if __name__=='__main__':
    loginPage = LoginPage()
    loginPage.input_username('test01')
    loginPage.input_password('newdream123')
    loginPage.click_login()