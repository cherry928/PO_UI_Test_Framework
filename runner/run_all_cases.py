#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:run_all_cases.py
# @time:2020/5/8 9:37 下午

import os
import unittest
from common import HTMLTestReportCN
from common.config_utils import config
from common.mail_utils import EmailUtils

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join( current_path , '..', config.case_path)
report_path = os.path.join( current_path , '..', config.report_path)

class RunAllCases:
    """
    执行case_path目录下所有以test.py结尾的文件
    输出的测试报告在report_path目录下
    """
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = '禅道自动化测试报告'
        self.description = 'UI-test'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        fp = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='cherry')
        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__ == '__main__':
    dir_path = RunAllCases().run()
    EmailUtils('Python自动化测试报告', dir_path).zip_send_mail()