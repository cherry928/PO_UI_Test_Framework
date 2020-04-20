from common.base_page import Basepage
from common.chrome_driver import chromedriver

class LoginPage(Basepage):
    def __init__(self, driver):  # 属性==》页面的控件
        super().__init__(driver)
        self.username_inputbox = {'element_name':'用户名输入框',
                                  'locator_type':'xpath',
                                  'locator_value':'//input[@name="account"]',
                                  'timeout': 5}
        self.password_inputbox = {'element_name': '密码输入框',
                                  'locator_type': 'xpath',
                                  'locator_value': '//input[@name="password"]',
                                  'timeout': 5}
        self.login_button = {'element_name': '登录按钮',
                                  'locator_type': 'xpath',
                                  'locator_value': '//button[@id="submit"]',
                                  'timeout': 5}

    def input_username(self, username):   # 方法==》控件的操作
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

if __name__=='__main__':
    loginPage = LoginPage(chromedriver.get_driver)
    loginPage.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    loginPage.input_username('test01')
    loginPage.input_password('newdream123')
    loginPage.click_login()