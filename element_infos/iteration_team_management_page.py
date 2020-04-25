# 迭代团队管理
import time
from common.base_page import Basepage
from common.chrome_driver import chromedriver
from common.element_data_utils import ElementdataUtils
from element_infos.main_page import mainpage

class IterationTeamManagement(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        mainpage.goto_project()
        elements = ElementdataUtils('iteration_team_management').get_element_info()
        self.team = elements['team']
        self.click_iteration = elements['click_iteration']
        self.choose_iteration = elements['choose_iteration']
        self.team_management = elements['team_management']
        self.add_dev_member = elements['add_dev_member']
        self.choose_dev_member = elements['choose_dev_member']
        self.add_test_member = elements['add_test_member']
        self.choose_test_member = elements['choose_test_member']
        self.preservation = elements['preservation']

    def click_click_iteration(self):  # 点击迭代下拉框
        self.click(self.click_iteration)

    def click_choose_iteration(self):  # 选择一个迭代
        self.click(self.choose_iteration)

    def click_team(self):  # 点击团队
        self.click(self.team)

    def click_team_management(self):  # 点击团队管理
        self.click(self.team_management)

    def click_add_dev_member(self):  # 点击选人下拉框
        self.click(self.add_dev_member)

    def click_choose_dev_member(self):  # 选择一个开发
        self.click(self.choose_dev_member)

    def click_add_test_member(self):  # 点击选人下拉框
        self.click(self.add_test_member)

    def click_choose_test_member(self):  # 选择一个测试
        self.click(self.choose_test_member)

    def click_preservation(self):   # 点击保存
        self.click(self.preservation)

if __name__=='__main__':
    iterationteammanagement = IterationTeamManagement(chromedriver.get_driver)
    iterationteammanagement.click_click_iteration()
    iterationteammanagement.click_choose_iteration()
    time.sleep(2)
    iterationteammanagement.click_team()
    iterationteammanagement.click_team_management()
    iterationteammanagement.click_add_dev_member()
    iterationteammanagement.click_choose_dev_member()
    iterationteammanagement.click_add_test_member()
    iterationteammanagement.click_choose_test_member()
    iterationteammanagement.click_preservation()