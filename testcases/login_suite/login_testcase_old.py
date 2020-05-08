import unittest
from common.browser import Browser
from common.base_page import Basepage
from common.config_utils import config
from actions.login_action import LoginAciton

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page = Basepage(Browser().get_chrome_dirver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(config.get_url_path)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_login_success(self):
        login_action = LoginAciton(self.base_page.driver)
        main_page = login_action.login_success('chenjuan', '1q2w3e4r,')
        self.assertEqual(main_page.get_username(), '陈娟', 'test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAciton(self.base_page.driver)
        actual_result = login_action.login_fail('chenjuan1', '1q2w3e4r')
        print('actual:%s'%actual_result)
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。')

if __name__=='__main__':
    unittest.main()