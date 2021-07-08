from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from config.config_message import ConfigMessage


class base_page:
    """
    基础页面类
    """
    host = ConfigMessage().host_message('${host}$')
    baseurl = 'https://' + host

    def __init__(self, seleium_driver, base_url=baseurl):
        self.driver = seleium_driver
        self.base_url = base_url

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def get_url(self):
        return self.base_url + self.url

    def find_element(self, loc: object) -> object:
        '''重写find_element方法，显式等待'''
        try:
            # print(loc)
            # WebDriverWait(self.driver, 18, 0.5).until(EC.presence_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            print('-------基础页面元素未定位成功')

    def send_keys(self, value, *loc):
        try:
            # self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            print('------send_keys失败')