import unittest
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils

class LoginTest(SeleniumBaseCase):
    """
    用例层，登录测试用例
    """
    test_class_data = TestDataUtils('login_suite', 'login_test').convert_exceldata_to_testdata()  # 类属性 取出excel的数据

    def setUp(self) -> None:
        super().setUp()
        print('hello!')

    @unittest.skipIf(test_class_data['test_login_success']['is_not'], '')  # 判断测试用例是否被忽略
    def test_login_success(self):
        test_function_data = self.test_class_data['test_login_success']
        print(test_function_data)
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'), test_function_data['test_parameter'].get('password'))
        actual_reslut = main_page.get_username()
        self.assertEqual(actual_reslut, test_function_data['excepted_result'], 'test_login_success用例执行失败')

    @unittest.skipIf(test_class_data['test_login_fail']['is_not'], '')
    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        print(test_function_data)
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'), test_function_data['test_parameter'].get('password'))
        print('actual:%s' % actual_result)
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。')


if __name__ == '__main__':

    unittest.main()