import os
from common.config_utils import config
from common.excel_utils import ExcelUtils

current_path = os.path.abspath(os.path.dirname(__file__))
excel_path_value = os.path.join( current_path, '..', config.element_info_path)
print(excel_path_value)

class ElementdataUtils:
    """
    调用ExcelUtils模块，转换输出的内容，根据模块，输出元素信息
    :param
    module_name 模块目录名称
    page_name 页面文件名称
    :return 返回格式是：{ x1:{}, x2:{},... }
    """
    def __init__(self, module_name, page_name, sheet_name=None, element_path=excel_path_value):
        self.element_path = element_path
        self.excel_path = os.path.join(self.element_path, module_name, page_name+'.xlsx')
        self.excelutils = ExcelUtils(self.excel_path, sheet_name)


    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.excelutils.get_row_count):
            element_info = {}
            element_info['element_name'] = self.excelutils.get_sheet_data_by_list()[i][1]
            element_info['locator_type'] = self.excelutils.get_sheet_data_by_list()[i][2]
            element_info['locator_value'] = self.excelutils.get_sheet_data_by_list()[i][3]
            timeout_value = self.excelutils.get_sheet_data_by_list()[i][4]
            element_info['timeout'] = timeout_value if isinstance(timeout_value, float) else config.time_out
            element_infos[self.excelutils.get_sheet_data_by_list()[i][0]] = element_info
        return element_infos

if __name__ == '__main__':
    elements = ElementdataUtils('main', 'main_page').get_element_info()
    print(elements)