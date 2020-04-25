from common.read_yaml_utils import ReadYaml
from common.chrome_driver import chromedriver
from common.base_page import Basepage

class LoginPage(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        loginyaml = ReadYaml()
        elements =loginyaml.read_yaml()
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

    def input_username(self, username):
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