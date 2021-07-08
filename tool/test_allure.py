import os

import allure
import pytest

from tool import operation_file

@allure.feature('登陆模块')
class TestLogin():
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    @allure.story('登陆成功场景')
    def test_login_succes (self):
        with allure.step('登陆1'):
            print('登陆成功')
            allure.attach("这是一个纯文本", name="登陆成功1", attachment_type=allure.attachment_type.TEXT)  # 添加文本
        assert False

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('登陆01')
    def test_login_1(self):
        pass

    @allure.story("用户名错误，登录失败")
    @allure.issue("10086", "这是一个bug，需要修复")
    @allure.severity(allure.severity_level.NORMAL)  # 正常问题
    def test_loginc(self):
        allure.attach.file("WechatIMG62.jpeg", name="这是一个图片", attachment_type=allure.attachment_type.JPG)  # 添加图片
        print("这是登录，用户名错误，登录失败")
        pass

if __name__ == '__main__':

    args = ['-s', '-q', '--alluredir', operation_file.filepath('tool/report_xml_dir')]
    pytest.main(args)
    cmd = 'allure generate %s -o %s -c' % (operation_file.filepath('tool/report_xml_dir'),
                                           operation_file.filepath('tool/report_html_dir'))
    # print(cmd)
    os.system(cmd)


