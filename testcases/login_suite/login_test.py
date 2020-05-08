import unittest
from actions.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):
    """
    用例层，登录测试用例
    """
    def setUp(self) -> None:
        super().setUp()
        print('hello!')

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('chenjuan', '1q2w3e4r,')
        actual_reslut = main_page.get_username()
        self.assertEqual(actual_reslut, '陈娟', 'test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('chenjuan1', '1q2w3e4r')
        print('actual:%s' % actual_result)
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。')


if __name__ == '__main__':
    unittest.main()