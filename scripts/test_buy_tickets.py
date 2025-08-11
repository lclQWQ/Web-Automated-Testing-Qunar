import unittest
from time import sleep

from parameterized import parameterized

from base.get_driver import SetDriver
from base.get_logger import GetLogger
from page.page_buy_tickets import PageBuyTickets
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


def get_buy_data(filename):
    file = test_data_filepath + filename
    json_data = read_json(file)
    res = []

    for data in json_data.values():
        res.append((data["from_station"], data["to_station"], data["date"], data["name"], data["id_card"], data["tele"],
                    data["true_case"], data["expect"]))

    return res


class TestBuyTickets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = SetDriver.get_driver()
        cls.logger = GetLogger.get_logger(logger_filepath)
        cls.login = PageLogin(cls.driver, logger_filepath)
        cls.buy = PageBuyTickets(cls.driver, logger_filepath)
        cls.login.page_login_entirely(tele="17340220730", pwd="li123456789")
        cls.buy.page_click_train()

    @classmethod
    def tearDownClass(cls):
        SetDriver.quit_driver()

    @parameterized.expand(get_buy_data("buy_tickets.json"))
    def test_buy_tickets(self, from_station, to_station, date, name, id_card, tele, true_case, expect):
        """

        :param from_station: 出发站
        :param to_station: 到达站
        :param date: 购票日期
        :param name: 乘客姓名
        :param id_card: 乘客证件号
        :param tele: 乘客手机号
        :param true_case: 正逆案例
        :param expect: 预期结果
        :return: None
        """
        self.buy.page_buy_tickets(from_station, to_station, date, name, id_card, tele)
        if true_case:
            try:
                self.assertTrue(self.buy.page_submit_success())
                self.buy.page_back(3)
                try:
                    self.assertTrue(self.buy.page_back_success())
                except Exception as e:
                    self.login.page_screenshot(error_screenshot_filepath)
                    self.logger.error("{},回退初始页面失败".format(e))
            except Exception as e:
                self.login.page_screenshot(error_screenshot_filepath)
                self.logger.error("{},提交订单失败".format(e))
        else:
            sleep(1)
            alert_info = self.buy.page_get_alert_info()
            try:
                self.assertEqual(alert_info, expect)
            except Exception as e:
                self.login.page_screenshot(error_screenshot_filepath)
                self.logger.error("{},测试结果与预期不符".format(e))

            self.buy.page_confirm_alert()
            self.buy.page_back(2)
            try:
                self.assertTrue(self.buy.page_back_success())
            except Exception as e:
                self.login.page_screenshot(error_screenshot_filepath)
                self.logger.error("{},回退初始页面失败".format(e))
