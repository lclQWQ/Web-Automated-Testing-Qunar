from selenium import webdriver

import page


class SetDriver:
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取浏览器驱动
            cls.driver = webdriver.Edge()
            # 最大化浏览器页面
            cls.driver.maximize_window()
            # 输入测试地址
            cls.driver.get(page.page_qunar_link)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            # 关闭浏览器驱动
            cls.driver.quit()
            cls.driver = None
