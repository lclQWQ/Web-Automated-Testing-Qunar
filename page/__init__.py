from selenium.webdriver.common.by import By

"""
以下为服务器地址配置
"""
page_qunar_link = "https://www.qunar.com/"

"""
以下为页面元素定位信息
"""
####################登录操作相关元素#################
# 跳转到可供登录的页面
page_about_qunar = By.XPATH, "//div[contains(text(),'关于去哪儿')]"
# 主页面登录链接
page_login_link = By.PARTIAL_LINK_TEXT, "登录"
# 密码登录
page_pwd_login = By.CSS_SELECTOR, ".passwordTab"
# 电话输入框
page_input_phonenum = By.CSS_SELECTOR, "#username"
# 密码输入框
page_input_password = By.CSS_SELECTOR, "#password"
# 协议同意按钮
page_click_agree = By.CSS_SELECTOR, "#agreement"
# 登录按钮
page_login_button = By.XPATH, "//div[@class='button']/span[text()='登录']"
# 验证滑块
page_slider = By.CSS_SELECTOR, ".OQphwVk_QrhLuedI5-Jme"
# 验证轨迹
page_track = By.CSS_SELECTOR, ".NrgjHeg7YBdiFd3U9T_j_"
# 退出登录
page_logout_button = By.CSS_SELECTOR, ".q_header_logout"
# 所有信息填写后的警告信息
page_alert_info = By.XPATH, "//span[text()='用户名或密码错误']"
# 请输入手机/邮箱/用户名
page_alert_input_tele = By.XPATH, "//span[text()='请输入手机/邮箱/用户名']"
# 请输入密码
page_alert_input_pwd = By.XPATH, "//span[text()='请输入密码']"
#####################买票操作相关元素#################
# 火车票
page_train_ticket = By.CSS_SELECTOR, ".qhf_train"
# 出发站
page_from_station = By.XPATH, "//input[@name='fromStation']"
# 到达站
page_to_station = By.XPATH, "//input[@name='toStation']"
# 日期
page_date = By.XPATH, "//input[@name='date']"
# 立即搜索
page_search = By.XPATH, "//button[@name='stsSearch']"
# 购买
page_click_buy = By.XPATH, "//span[text()='购\u00A0\u00A0买']"
# 乘客姓名
page_passenger_name = By.XPATH, "//input[@name='pName_0']"
# 乘客证件号码
page_passenger_id = By.XPATH, "//input[@name='pCertNo_0']"
# 取票人姓名
page_contact_name = By.XPATH, "//input[@name='contact_name']"
# 取票人电话
page_contact_tele = By.XPATH, "//input[@name='contact_phone']"
# 提交订单
page_submit_order = By.XPATH,"/html/body/form/div[2]/div[2]/div[4]/div[2]/div[3]/button"
# 提交订单成功
page_pay = By.XPATH, "//div[text()='安全支付']"
# 提示信息
page_buy_alert = By.CSS_SELECTOR, ".retitle"
# 确认提示信息
page_confirm_alert = By.CSS_SELECTOR, ".btn_gray"
