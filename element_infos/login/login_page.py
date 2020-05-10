from common.base_page import Basepage
from common.element_data_utils import ElementdataUtils
from common.browser import Browser


class LoginPage(Basepage):
    def __init__(self, driver):  # 属性==》页面的控件
        super().__init__(driver)
        elements = ElementdataUtils('login','login_page').get_element_info()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

    def input_username(self, username):   # 方法==》控件的操作
        self.input(self.username_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)

    def get_login_fail_alert(self, type, selector, value=''):
        value1 = self.alert(Type=type, Selector=selector, Value =value)
        return value1

if __name__=='__main__':
    driver = Browser().get_driver()
    loginPage = LoginPage(driver)
    loginPage.open_url('http://106.53.50.202:8999/zentao2/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    loginPage.input_username('chenjuan')
    loginPage.input_password('1q2w3e4r,')
    loginPage.click_login()
    loginPage.screenshot_as_file()