from src.page.login_page import Login_Page
from common.singdriver import Singdriver
from src.config.conf_read import ConfRead


class Login:
    def __init__(self):
        self.login = Login_Page(Singdriver())

    def go_in_login_page(self):
        self.login.open()
        self.login.find_element(self.login.submit_loc).click()

    def input_username(self):
        self.login.find_element(self.login.username_loc).send_keys(ConfRead().get_config('section', 'name'))


# if __name__ == '__main__':
#