import unittest
from time import sleep

from parameterized import parameterized

from base.get_driver import SetDriver
from base.get_logger import GetLogger
from page.page_login import PageLogin
from tools.read_json import read_json

"""
以下为相关文件保存地址
"""
# 日志文件保存地址
logger_filepath = "../logs/"
# 错误截图保存地址
error_screenshot_filepath = "../screen_shots/"
# 测试报告保存地址
testing_report_filepath = "../reports/"
# 测试文件地址
test_data_filepath = "../datas/"


def get_login_data(filename):
    file = test_data_filepath + filename
    json_data = read_json(file)
    res = []

    for data in json_data.values():
        res.append((data["tele"], data["pwd"], data["expect"], data["true_case"]))

    return res


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = SetDriver.get_driver()
        cls.login = PageLogin(cls.driver, logging_filepath=logger_filepath)
        cls.logger = GetLogger.get_logger(filepath=logger_filepath)
        cls.login.page_prepare_login()

    @classmethod
    def tearDownClass(cls):
        SetDriver.quit_driver()

    @parameterized.expand(get_login_data("telephone_login.json"))
    def test_login_by_telephone(self, telephone, pwd, expect, true_case):
        self.login.page_login_by_pwd(telephone, pwd)
        if true_case:
            try:
                self.assertTrue(self.login.page_if_login_success())
                self.login.page_click_logout()

                try:
                    self.assertTrue(self.login.page_if_logout_success())
                    self.login.page_click_login_link()
                    self.login.page_click_pwd_login()

                except Exception as e:
                    self.logger.error(e)
                    self.login.page_screenshot(screenshot_filepath=error_screenshot_filepath)

            except Exception as e:
                self.logger.error(e)
                self.login.page_screenshot(screenshot_filepath=error_screenshot_filepath)

        else:

            sleep(1)
            alert_info = self.login.page_get_alert_info()

            try:
                self.assertEqual(expect, alert_info)

            except Exception as e:
                self.logger.error(e)
                self.login.page_screenshot(screenshot_filepath=error_screenshot_filepath)
            # 刷新页面，重置同意协议按钮以及警告信息
            self.driver.refresh()
            self.login.page_click_pwd_login()
