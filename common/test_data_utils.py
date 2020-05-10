#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:test_data_utils.py
# @time:2020/5/8 8:30 下午

import os
from common.config_utils import config
from common.excel_utils import ExcelUtils

current_path = os.path.abspath(os.path.dirname(__file__))
test_data_path = os.path.join(current_path, '..', config.testdata_path)

class TestDataUtils:
    """
    调用ExcelUtils模块，转换输出的内容，根据所属测试类、sheet，输出元素信息
    :param
    第一个参数：test_suite_name  test_data_path目录下，目录名称
    第二个参数：test_file_name  test_suite_name目录下，文件名称
    :return
    {'test_login_success':{'test_name':'验证是否能成功进行登录',
                           'isnot':False,
                           'excepted_result': '陈娟',
                           'test_parameter': {'username': 'chenjuan', 'password': '1q2w3e4r,'}}
     'test_login_fail':{}
    }
    """
    def __init__(self, test_suite_name, test_file_name, test_class_name=None, test_data_path=test_data_path):
        test_data_path = os.path.join(test_data_path, test_suite_name,  test_file_name+'.xlsx')
        self.excel_data = ExcelUtils(test_data_path, test_class_name).get_sheet_data_by_list()
        self.excel_rows = len(self.excel_data)

    def convert_exceldata_to_testdata(self):
        test_data_infos = {}
        for i in range(1, self.excel_rows):
            test_data_info = {}
            test_data_info['test_name'] = self.excel_data[i][1]
            test_data_info['is_not'] = False if self.excel_data[i][2].__eq__('是') else True  # 把excel的'是'转换为False 代表用例执行
            test_data_info['excepted_result'] = self.excel_data[i][3]
            test_parameter = {}
            for j in range(4, len(self.excel_data[i])):  # 不定长参数 取值方式
                if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j]) > 2:  # 判断表格中含有 '=' 并且长度大于2
                    parameter_info = self.excel_data[i][j].split('=')  # 取出 = 左右两边的值
                    test_parameter[parameter_info[0]] = parameter_info[1]
            test_data_info['test_parameter'] = test_parameter
            test_data_infos[self.excel_data[i][0]] = test_data_info
        return test_data_infos

if __name__ == '__main__':

    infos = TestDataUtils('login_suite', 'login_test').convert_exceldata_to_testdata()
    print(infos)