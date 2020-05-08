import os
from common.config_utils import config
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
excel_path_value = os.path.join(current_path, '../element_info_data/element_infos.xlsx')

class ElementdataUtils:
    """
    调用ExcelUtils模块，转换输出的内容，根据所属页面，输出元素信息
    :param excel_path:excel路径；sheet_name:sheet名称；page_name:页面名称
    :return 返回格式是：{ x1:{}, x2:{},... }
    """
    def __init__(self, sheet_name=None, excel_path=excel_path_value):
        self.excelutils = ExcelUtils(excel_path, sheet_name)

    def get_element_info(self, page_name):
        element_infos = {}
        for i in range(1, self.excelutils.get_row_count):
            if self.excelutils.get_sheet_data_by_list()[i][5] == page_name:
                element_info = {}
                element_info['element_name'] = self.excelutils.get_sheet_data_by_list()[i][1]
                element_info['locator_type'] = self.excelutils.get_sheet_data_by_list()[i][2]
                element_info['locator_value'] = self.excelutils.get_sheet_data_by_list()[i][3]
                timeout_value = self.excelutils.get_sheet_data_by_list()[i][4]
                element_info['timeout'] = timeout_value if isinstance(timeout_value, float) else config.time_out
                element_infos[self.excelutils.get_sheet_data_by_list()[i][0]] = element_info
        return element_infos

if __name__ == '__main__':
    elements = ElementdataUtils().get_element_info('login_page')
    print(elements)