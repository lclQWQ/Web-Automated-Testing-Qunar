import time
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger


class Base:
    # 初始化函数
    def __init__(self, driver, logging_filepath):
        self.driver = driver
        self.logger = GetLogger.get_logger(logging_filepath)
        self.action = ActionChains(self.driver)
        self.logger.info("Base函数初始化完毕")

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 元素信息
        :param timeout: 显式等待的最长时间，默认为30s
        :param poll: 查找频率，默认为每0.5s查找一次
        :return: 元素查找方法
        """
        self.logger.info("查找{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        self.logger.info("点击{}".format(loc))
        self.base_find_element(loc).click()

    # 填写信息
    def base_input_value(self, loc, value):
        # 寻找元素
        ele = self.base_find_element(loc)
        # 清除输入框中可能存在的信息
        self.logger.info("清理{}信息".format(loc))
        ele.clear()
        # 输入信息
        self.logger.info("向{}输入{}".format(loc, value))
        ele.send_keys(value)

    # 切换页面
    def base_switch_page(self):
        # 获取浏览器所有页面句柄
        handles = self.driver.window_handles
        # 获取最新打开的页面
        current_window = handles[-1]
        for handle in handles:
            # 关闭与登录页面无关的窗口
            if handle != current_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
        # 切换到打开的最新窗口
        self.driver.switch_to.window(current_window)

    # 获取文本信息
    def base_get_info(self, loc):
        return self.base_find_element(loc).text

    # 判断元素是否存在
    def base_if_element_exists(self, loc, timeout=5):
        try:
            self.base_find_element(loc, timeout)
            return True
        except Exception:
            return False

    # 拖动验证条
    def base_drag_verify_bar(self, slider_loc, track_loc):
        # 定位滑块元素
        slider = self.base_find_element(slider_loc)
        # 定位轨道元素
        track = self.base_find_element(track_loc)

        # 计算滑动距离
        distance = track.size['width'] - slider.size['width']

        # 执行滑动操作
        # 长按点击滑块
        self.action.click_and_hold(slider).perform()
        # 进行滑动 实际滑动距离需要稍微比计算滑动距离长一些
        self.action.move_by_offset(distance + 10, 0).perform()
        # 释放鼠标
        self.action.release().perform()
        sleep(1)

    # 截图
    def base_screenshot(self, filepath):
        self.driver.get_screenshot_as_file(
            filename=filepath + 'error_fig{}.png'.format(time.strftime('%Y%m%d_%H-%M-%S')))

    # 下拉滚动条
    def base_pull_down_scrollbar(self):
        js = "window.scrollTo(0,1000)"  # js脚本控制滚动条
        self.driver.execute_script(js)  # 执行js脚本

    # 回退页面
    def base_page_back(self, times=1):
        """

        :param times: 页面回退次数，默认回退一次
        :return: None
        """
        for _ in range(times):
            self.driver.back()
