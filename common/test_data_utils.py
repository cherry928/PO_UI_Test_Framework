#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_data_utils.py
# @time:2020/5/8 8:30 下午

import os
from common.config_utils import config
from common.excel_utils import ExcelUtils

current_path = os.path.abspath(os.path.dirname(__file__))
test_data_path = os.path.join( current_path , '..', config.testdata_path)

class TestDataUtils:

    def __init__(self, test_suite_name, test_class_name):
        self.test_class_name = test_class_name
        self.excel_data = ExcelUtils(test_data_path, test_suite_name).get_sheet_data_by_list()
        self.excel_rows = len(self.excel_data)

    def convert_exceldata_to_testdata(self):
        # {'test_login_success':{'test_name':'验证是否能成功进行登录',
        #                        'isnot':'是',
        #                        'test_parameter':{'username':'chenjuan','password':'1q2w3e4r,'}}
        #  'test_login_fail':{}
        #  }
        test_data_infos = {}
        for i in range(1, self.excel_rows):
            test_data_info = {}
            if self.excel_data[i][2].__eq__(self.test_class_name):
                test_data_info['test_name'] = self.excel_data[i][1]
                test_data_info['isnot'] = self.excel_data[i][3]
                test_data_info['excepted_result'] = self.excel_data[i][4]
                test_parameter = {}
                for j in range(5, len(self.excel_data[i])):  # 不定长参数 取值方式
                    if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j]) > 2:
                        parameter_info = self.excel_data[i][j].split('=')
                        test_parameter[parameter_info[0]] = parameter_info[1]
                test_data_info['test_parameter'] = test_parameter
            test_data_infos[self.excel_data[i][0]] = test_data_info
        return test_data_infos

if __name__ == '__main__':
    infos = TestDataUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()
    print(infos)