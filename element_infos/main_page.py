from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log_utils import logger

class MainPage:
    def __init__(self):  # 属性==》页面的控件
        loginPage = LoginPage()
        loginPage.input_username('test01')
        loginPage.input_password('newdream123')
        loginPage.click_login()
        self.driver =loginPage.dirver
        self.companyname_showbox = self.driver.find_element(By.XPATH, '//h1[@id="companyname"]')
        self.myzone_menu = self.driver.find_element(By.XPATH, '//li[@data-id="my"]')
        self.product_menu = self.driver.find_element(By.XPATH, '//li[@data-id="product"]')
        self.username_showspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')

    def get_companyname(self): # 获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        logger.info('获取公司名成功，公司名是：' + str(value))
        return value

    def goto_myzone(self): # 进入我的地盘菜单
        self.myzone_menu.click()

    def goto_product(self): # 进入产品菜单
        self.product_menu.click()

    def get_username(self): # 获取用户名
        value = self.username_showspan.text
        logger.info('获取用户名成功，用户名是：'+ str(value))
        return value

if __name__=='__main__':
    mainPage = MainPage()
    commanyname = mainPage.get_companyname()

    mainPage.goto_myzone()

    username = mainPage.get_username()
    print(commanyname, username)