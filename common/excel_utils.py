#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:excel_utils.py
# @time:2020/5/5 4:37 下午
import os
import xlrd
from common.config_utils import config


current_path = os.path.abspath(os.path.dirname(__file__))
excel_path = os.path.join( current_path , '..', config.testdata_path)
# print(excel_path)

class ExcelUtils:
    """
    根据提供的excel路径和sheet名称读取对应sheet内容
    :param excel_path:excel路径；sheet_name:sheet名称
    :return 返回格式是：[ [],[],[]... ]
    """
    def __init__(self, excel_path, sheet_name=None):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):  # sheet_name没有带参数时，默认取第一个
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        row_count = self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count = self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self):
        all_excel_data = []
        for rownum in range(self.get_row_count):
            row_excel_data = []
            for colnum in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(rownum, colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data

if __name__ == '__main__':
    excelutils = ExcelUtils(excel_path)
    print(excelutils.get_sheet_data_by_list())