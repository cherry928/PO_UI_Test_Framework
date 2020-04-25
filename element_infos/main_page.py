from element_infos.login_page import LoginPage
from common.base_page import Basepage
from common.chrome_driver import chromedriver
from common.element_data_utils import ElementdataUtils

class MainPage(Basepage):
    def __init__(self, driver):  # 属性==》页面的控件
        super().__init__(driver)
        self.loginPage = LoginPage(driver)
        self.loginPage.open_url('http://106.53.50.202:8999/zentao2/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
        self.loginPage.input_username('chenjuan')
        self.loginPage.input_password('1q2w3e4r,')
        self.loginPage.click_login()
        elements = ElementdataUtils('main_page').get_element_info()
        self.companyname_showbox = elements['companyname_showbox']
        self.myzone_menu = elements['myzone_menu']
        self.product_menu = elements['product_menu']
        self.project_menu = elements['project_menu']
        self.username_showspan = elements['username_showspan']

    def get_companyname(self):   # 获取公司名称
        value = self.get_attribute_title(self.companyname_showbox)
        return value

    def goto_myzone(self): # 进入我的地盘菜单
        self.click(self.myzone_menu)

    def goto_product(self): # 进入产品菜单
        self.click(self.product_menu)

    def goto_project(self): # 进入迭代
        self.click(self.project_menu)

    def get_username(self): # 获取用户名
        value = self.get_text(self.username_showspan)
        return value

mainpage = MainPage(chromedriver.get_driver)

if __name__=='__main__':
    mainPageA = MainPage(chromedriver.get_driver)
    commanyname = mainPageA.get_companyname()
    mainPageA.goto_myzone()
    mainPageA.goto_product()
    mainPageA.goto_project()
    username = mainPageA.get_username()
    print(commanyname, username)