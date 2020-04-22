from common.base_page import Basepage
from common.chrome_driver import chromedriver
from common.element_data_utils import ElementdataUtils

class LoginPage(Basepage):
    def __init__(self, driver):  # 属性==》页面的控件
        super().__init__(driver)
        # self.username_inputbox = {'element_name':'用户名输入框',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@name="account"]',
        #                           'timeout': 5}
        # self.password_inputbox = {'element_name': '密码输入框',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 5}
        # self.login_button = {'element_name': '登录按钮',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 5}
        elements = ElementdataUtils('login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

    def input_username(self, username):   # 方法==》控件的操作
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

if __name__=='__main__':
    loginPage = LoginPage(chromedriver.get_driver)
    loginPage.open_url('http://106.53.50.202:8999/zentao2/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    loginPage.input_username('chenjuan')
    loginPage.input_password('1q2w3e4r,')
    loginPage.click_login()