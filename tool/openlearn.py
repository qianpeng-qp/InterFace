from selenium import webdriver
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用浏览器正在被自动化程序控制的提示
    # options.add_experimental_option('useAutomationExtension', False)  # 禁用扩展插件
    options.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(options=options)
    driver.get('https://time.geekbang.org/')
    js = "document.cookie='GCID=d9540ef-ed89870-effbbda-0b1a076;domain=.geekbang.org;path=/';document.cookie='GRID=d9540ef-ed89870-effbbda-0b1a076;domain=.geekbang.org;path=/';document.cookie='GCESS=BQcEwoYtOAME1ZHlYAgBAwsCBQAEBAAvDQAJAQEBCJkLKQAAAAAAAgTVkeVgBgTlpzqvDAEBBQQAAAAACgQAAAAA;domain=.geekbang.org;path=/';document.cookie='GRID=f007e52-8b22e80-6a6cba8-812496b;domain=.geekbang.org;path=/';document.cookie='SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1625657813|1625657812;domain=.geekbang.org;path=/';"
    driver.execute_script(js)
    driver.refresh()