import json
import re
import urllib.parse

from tool.setup_logging import Log
log1 = Log()
from selenium import webdriver
from selenium.webdriver import ChromeOptions
class get_Web_Request:
    caps = {
        'browserName': 'chrome',
        'loggingPrefs': {
            'browser': 'ALL',
            'driver': 'ALL',
            'performance': 'ALL',
        },
        'goog:chromeOptions': {
            'perfLoggingPrefs': {
                'enableNetwork': True,
            },
            'w3c': False,
        },
    }

    # options = Options()
    options = ChromeOptions()
    options.add_argument('-headless')
    options.add_argument('--disable-gpu')  # 禁用GPU加速
    options.add_argument('--window-size=1280,800')  # 设置窗口大小
    # options.add_argument('--incognito')                     # 配置浏览器主题为黑色
    options.add_argument('--ignore-certificate-errors')  # 忽略连接警告信息
    options.add_experimental_option("detach", True)  # 不自动关闭浏览器
    options.add_argument("--disable-gpu")  # 禁用gpu
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 禁止加载图片
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用浏览器正在被自动化程序控制的提示
    options.add_experimental_option('useAutomationExtension', False)  # 禁用扩展插件
    options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=options, desired_capabilities=caps)
    driver.get('https://www.hao774.com/')
    #
    driver.implicitly_wait(10)
    i = 1
    for log in driver.get_log('performance'):
        request = json.loads(log['message'])['message']['params'].get('request')
        if request is None:
            continue
        regex = re.compile("ajax.*?")
        url = request['url']
        if not regex.findall(url):
            continue
        log1.debug('url:%s' % str(urllib.parse.urlsplit(url)))
        log1.debug('parms:%s' % str(dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))))
        i += 1
    driver.quit()