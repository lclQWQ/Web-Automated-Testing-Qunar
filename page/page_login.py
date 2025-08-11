import page
from base.base import Base


class PageLogin(Base):
    # 点击关于去哪儿
    def page_click_about_qunar(self):
        self.base_click(page.page_about_qunar)

    # 关闭无用页面
    def page_close_another_window(self):
        self.base_switch_page()

    # 进入登录页面
    def page_click_login_link(self):
        self.base_click(page.page_login_link)

    """默认密码登录"""

    # 点击密码登录
    def page_click_pwd_login(self):
        self.base_click(page.page_pwd_login)

    # 输入手机号
    def page_input_telephone(self, tele):
        self.base_input_value(page.page_input_phonenum, tele)

    # 输入密码
    def page_input_password(self, pwd):
        self.base_input_value(page.page_input_password, pwd)

    # 拖动验证条
    def page_drag_verify_bar(self):
        self.base_drag_verify_bar(page.page_slider, page.page_track)

    # 点击同意协议
    def page_click_agree_button(self):
        self.base_click(page.page_click_agree)

    # 点击登录按钮
    def page_click_login_button(self):
        self.base_click(page.page_login_button)

    # 点击退出登录
    def page_click_logout(self):
        self.base_click(page.page_logout_button)

    # 获取警告信息：警告信息出现位置多样，需逐层分析
    def page_get_alert_info(self):
        alert_locs = [
            page.page_alert_input_tele,  # 未输入手机号的警告
            page.page_alert_input_pwd,  # 未输入密码的警告
            page.page_alert_info  # 最底部的警告信息
        ]

        visible_alerts = []
        # 收集所有可见警告
        for loc in alert_locs:
            if self.base_if_element_exists(loc, 2):
                text = self.base_get_info(loc)
                if text:  # 忽略空文本
                    visible_alerts.append(text)
        return visible_alerts[0] if visible_alerts else False

    # 失败截图
    def page_screenshot(self, screenshot_filepath):
        self.base_screenshot(screenshot_filepath)

    # 判断是否登录成功
    def page_if_login_success(self):
        return self.base_if_element_exists(page.page_logout_button)

    # 判断是否退出成功
    def page_if_logout_success(self):
        return self.base_if_element_exists(page.page_login_link)

    #进入登录页面的前置操作
    def page_prepare_login(self):
        self.page_click_about_qunar()
        self.page_close_another_window()
        self.page_click_login_link()
        self.page_click_pwd_login()

    # 手机号登录功能组装
    def page_login_by_pwd(self, telephone, password):
        self.page_input_telephone(telephone)
        self.page_input_password(password)
        self.page_click_agree_button()
        print("-----运行到这里了---------")
        self.page_click_login_button()
        print("-----运行到这里了---------")
        # 若不填写用户名或者密码，点击登录不会出现验证条，同时会出现警告信息
        alert = self.page_get_alert_info()
        print("-----运行到这里了---------")
        if alert:
            print(alert)
        else:
            self.page_drag_verify_bar()

    def page_login_entirely(self, tele, pwd):
        self.page_click_about_qunar()
        self.page_close_another_window()
        self.page_click_login_link()
        self.page_click_pwd_login()
        self.page_input_telephone(tele)
        self.page_input_password(pwd)
        self.page_click_agree_button()
        self.page_click_login_button()
        self.page_drag_verify_bar()
