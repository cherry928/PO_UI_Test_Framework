from element_infos.login_page import LoginPage
from common.base_page import Basepage
from common.chrome_driver import chromedriver

class MainPage(Basepage):
    def __init__(self, driver):  # 属性==》页面的控件
        super().__init__(driver)
        loginPage = LoginPage(chromedriver.get_driver)
        loginPage.open_url('http://127.0.0.1/zentaopms/www/index.php?m=user&f=login')
        loginPage.input_username('admin')
        loginPage.input_password('123456aA')
        loginPage.click_login()
        self.companyname_showbox = {'element_name':'公司名字',
                                  'locator_type':'xpath',
                                  'locator_value':'//h1[@id="companyname"]',
                                  'timeout': 5}
        self.myzone_menu = {'element_name':'我的地盘',
                            'locator_type':'xpath',
                            'locator_value':'//li[@data-id="my"]',
                            'timeout': 5}
        self.product_menu = {'element_name':'产品',
                            'locator_type':'xpath',
                            'locator_value':'//li[@data-id="product"]',
                            'timeout': 5}
        self.project_menu = {'element_name':'迭代',
                            'locator_type':'xpath',
                            'locator_value':'//li[@data-id="project"]',
                            'timeout': 5}
        self.username_showspan = {'element_name':'用户名字',
                                  'locator_type':'xpath',
                                  'locator_value':'//span[@class="user-name"]',
                                  'timeout': 5}


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
    mainPage = MainPage(chromedriver.get_driver)
    commanyname = mainPage.get_companyname()
    mainPage.goto_myzone()
    mainPage.goto_product()
    mainPage.goto_project()
    username = mainPage.get_username()
    print(commanyname, username)