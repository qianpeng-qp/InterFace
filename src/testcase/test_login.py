import allure
import pytest

import sys
print(sys.path)
import os
os.chdir('/Users/pq/git/InterFace/')
for file in os.listdir(os.getcwd()):
     print(file)
sys.path.append('/Users/pq/git/InterFace/')
from src.business.login import Login


@allure.feature('登陆模块')
class test_Login:
    @allure.story('打开页面')
    def test_login1(self):
        Login().go_in_login_page()
        print('1')
        assert False

    @allure.story('输入账号')
    def test_login2(self):
        Login.go_in_login_page()

# if __name__ == '__main__':
#     pytest.main()
