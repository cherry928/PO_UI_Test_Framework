import os
import xlrd
from common.config_utils import config

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_data/element_infos.xlsx')

class ElementdataUtils:
    def __init__(self, module_name,  page_name, element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(self.element_path)
        self.sheet = self.workbook.sheet_by_name(module_name)
        self.row_count = self.sheet.nrows
        self.page_name = page_name


    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 5) == self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i ,1)
                element_info['locator_type'] = self.sheet.cell_value(i, 2)
                element_info['locator_value'] = self.sheet.cell_value(i, 3)
                timeout_value = self.sheet.cell_value(i, 4)
                element_info['timeout'] = timeout_value if isinstance(timeout_value, float) else config.time_out
                element_infos[self.sheet.cell_value(i ,0)] = element_info
        return element_infos

if __name__=='__main__':
    elements = ElementdataUtils('sheet1', 'login_page').get_element_info()
    print(elements)