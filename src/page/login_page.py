from src.page.base_page import base_page
from selenium.webdriver.common.by import By


class Login_Page(base_page):
    url = '/login?code=public'
    submit_loc = (By.XPATH, '//div[@class="main-select"]//li[@class="text-tab border-right"][2]')
    username_loc = (By.XPATH, '//input[@placeholder="手机号/邮箱/用户名"]')
    password_loc = (By.XPATH, '//input[@placeholder="密码"]')
    login_loc1 = (By.XPATH, '//button[@disabled="disabled"]')
    login_loc2 = (By.XPATH, '//button[@class="btn btn-primary"]')
