from time import sleep

import page
from base.base import Base


class PageBuyTickets(Base):

    # 点击火车票
    def page_click_train(self):
        self.base_click(page.page_train_ticket)

    # 输入出发站
    def page_input_from_station(self, from_station):
        self.base_input_value(page.page_from_station, from_station)

    # 输入到达站
    def page_input_to_station(self, to_station):
        self.base_input_value(page.page_to_station, to_station)

    # 输入日期
    def page_input_date(self, date):

        input_date = self.base_find_element(page.page_date)
        self.driver.execute_script("arguments[0].value = arguments[1];", input_date, date)

    # 点击立即搜索
    def page_click_search(self):
        self.base_click(page.page_search)

    # 点击购买
    def page_click_buy(self):
        self.base_click(page.page_click_buy)

    # 填写乘客姓名
    def page_input_passenger_name(self, name):
        self.base_input_value(page.page_passenger_name, name)

    # 填写乘客身份证
    def page_input_passenger_id(self, id):
        self.base_input_value(page.page_passenger_id, id)

    # 填写取票人姓名
    def page_input_contact_name(self, name):
        self.base_input_value(page.page_contact_name, name)

    # 填写取票人手机号
    def page_input_contact_tele(self, tele):
        self.base_input_value(page.page_contact_tele, tele)

    # 点击提交订单
    def page_click_submit(self):
        self.base_click(page.page_submit_order)

    # 下拉滚动条
    def page_pull_down_scrollbar(self):
        self.base_pull_down_scrollbar()

    # 判断创建订单是否成功
    def page_submit_success(self):
        return self.base_if_element_exists(page.page_pay)

    # 回退至测试初始页面
    def page_back(self,times):
        self.base_page_back(times)

    # 判断是否回退成功
    def page_back_success(self):
        return self.base_if_element_exists(page.page_search, 2)

    def page_get_alert_info(self):
        return self.base_get_info(page.page_buy_alert)

    def page_confirm_alert(self):
        self.base_click(page.page_confirm_alert)

    # 购票功能组装
    def page_buy_tickets(self, from_station, to_station, date, name, id, tele):
        """

        :param from_station: 出发站
        :param to_station: 到达站
        :param date: 购票日期
        :param name: 乘客姓名
        :param id: 乘客证件号
        :param tele: 乘客电话
        :return: None
        """
        sleep(2)
        self.page_input_from_station(from_station)
        sleep(2)
        self.page_input_to_station(to_station)
        sleep(2)
        self.page_input_date(date)
        sleep(2)
        self.page_click_search()
        self.page_click_buy()
        self.page_input_passenger_name(name)
        self.page_input_passenger_id(id)
        self.page_pull_down_scrollbar()
        self.page_input_contact_name(name)
        self.page_input_contact_tele(tele)
        self.page_click_submit()
