# 功能层
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import config
from common.browser import Browser

class LoginAction:
    """
    功能层，实现登录成功、登录失败、默认登录流程
    :param 传入浏览器驱动，用户名，密码
    """
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def login_action(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self, username, password):
        self.login_action(username, password)
        return MainPage(self.login_page.driver)

    def default_login(self):
        self.login_success(username=config.user_name, password=config.pass_word)

    def login_fail(self, username, password):
        self.login_action(username, password)
        value = self.login_page.get_login_fail_alert(type='yes', selector='alert')
        return value

    def login_by_cookie(self):
        pass

if __name__=='__main__':
    driver1 = Browser().get_driver()
    loginaction = LoginAction(driver1)
    driver1.get('http://106.53.50.202:8999/zentao2/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    loginaction.login_success('chenjuan', '1q2w3e4r,')