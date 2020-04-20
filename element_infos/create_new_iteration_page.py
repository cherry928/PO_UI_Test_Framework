# 添加新迭代页面
from common.base_page import Basepage
from common.chrome_driver import chromedriver
from element_infos.main_page import mainpage

class CreateNewIterationPage(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        mainpage.goto_project()
        self.create_iteration = {'element_name': '添加迭代',
                                 'locator_type': 'xpath',
                                 'locator_value': '//div[@id="pageActions"]',
                                 'timeout': 5}
        self.iteration_name = {'element_name': '迭代名称',
                               'locator_type': 'xpath',
                               'locator_value': '//input[@id="name"]',
                               'timeout': 5}
        self.iteration_code = {'element_name': '迭代代号',
                               'locator_type': 'xpath',
                               'locator_value': '//input[@id="code"]',
                               'timeout': 5}
        self.start_date = {'element_name': '起始日期',
                           'locator_type': 'xpath',
                           'locator_value': '//input[@id="begin"]',
                           'timeout': 5}
        self.close_date = {'element_name': '截止日期',
                           'locator_type': 'xpath',
                           'locator_value': '//input[@id="end"]',
                           'timeout': 5}
        self.team_name = {'element_name': '团队名称',
                          'locator_type': 'xpath',
                          'locator_value': '//input[@id="team"]',
                          'timeout': 5}
        self.iteration_type = {'element_name': '迭代类型',
                               'locator_type': 'xpath',
                               'locator_value': '//select[@id="type"]',
                               'timeout': 5}
        self.chose_iteration_type = {'element_name': '选择迭代类型',
                                     'locator_type': 'xpath',
                                     'locator_value': '//option[@title="长期迭代"]',
                                     'timeout': 5}
        self.related_items = {'element_name': '关联项目',
                              'locator_type': 'xpath',
                              'locator_value': '//div[@id="products0_chosen"]',
                              'timeout': 5}
        self.chose_related_items = {'element_name': '选择关联项目',
                                    'locator_type': 'xpath',
                                    'locator_value': '//li[@title="新梦想"]',
                                    'timeout': 5}
        self.switch_to_content_frame = {'element_name': 'content_frame',
                                        'locator_type': 'xpath',
                                        'locator_value': '//iframe[@class="ke-edit-iframe"]',
                                        'timeout': 5}
        self.iterative_description = {'element_name': '迭代描述',
                                      'locator_type': 'xpath',
                                      'locator_value': '//body[@class="article-content"]',
                                      'timeout': 5}
        self.preservation = {'element_name': '保存',
                             'locator_type': 'xpath',
                             'locator_value': '//button[@id="submit"]',
                             'timeout': 5}
        self.close_button = {'element_name': '关闭',
                             'locator_type': 'xpath',
                             'locator_value': '//a[@class="close"]',
                             'timeout': 5}

    def click_create_iteration(self):    # 点击添加迭代按钮
        self.click(self.create_iteration)

    def input_iteration_name(self, name):   # 输入迭代名称
        self.input(self.iteration_name, name)

    def input_iteration_code(self, code):  # 输入迭代代码
        self.input(self.iteration_code, code)

    def clear_data_content(self):  # 清除日期输入框的日期
        self.clear(self.start_date)

    def input_start_date(self, begin):  # 输入开始日期
        self.input(self.start_date, begin)

    def click_start_date(self):  # 再点击日期输入框
        self.click(self.start_date)

    def input_close_date(self, close):  # 输入截止日期
        self.input(self.close_date, close)

    def click_close_date(self):  # 再点击日期输入框
        self.click(self.close_date)

    def input_team_name(self, team):  # 输入团队名称
        self.input(self.team_name, team)

    def click_iteration_type(self):  # 点击迭代类型
        self.click(self.iteration_type)

    def click_chose_iteration_type(self):  # 选择一个迭代类型
        self.click(self.chose_iteration_type)

    def click_related_items(self):  # 点击关联项目
        self.click(self.related_items)

    def click_chose_related_items(self):  # 选择关联项目
        self.click(self.chose_related_items)

    def switchto_frame(self):  # 切换frame
        self.switch_to_frame(self.switch_to_content_frame)

    def input_iterative_description(self, description):  # 输入迭代描述
        self.input(self.iterative_description,description)

    def switchto_default_content(self):  # 切换到默认frame
        self.switch_to_default_content()

    def slide_element(self):  # 滑到保存按钮
        self.slide_specified_element(self.preservation)

    def click_preservation(self):  # 点击保存按钮
        self.click(self.preservation)

    def click_close_button(self):  # 点击关闭按钮
        self.click(self.close_button)

if  __name__ == '__main__':
    createnewiterationpage = CreateNewIterationPage(chromedriver.get_driver)
    createnewiterationpage.click_create_iteration()
    createnewiterationpage.input_iteration_name('公共研发组sprint1')
    createnewiterationpage.input_iteration_code('sprint1')
    createnewiterationpage.clear_data_content()
    createnewiterationpage.input_start_date('2020-04-19')
    createnewiterationpage.click_start_date()
    createnewiterationpage.input_close_date('2020-08-20')
    createnewiterationpage.click_close_date()
    createnewiterationpage.input_team_name('公共研发组sprint1')
    createnewiterationpage.click_iteration_type()
    createnewiterationpage.click_chose_iteration_type()
    # createnewiterationpage.click_related_items()
    # createnewiterationpage.click_chose_related_items()
    createnewiterationpage.switchto_frame()
    createnewiterationpage.input_iterative_description('公共研发组sprint1迭代')
    createnewiterationpage.switchto_default_content()
    createnewiterationpage.slide_element()
    createnewiterationpage.click_preservation()
    createnewiterationpage.click_close_button()