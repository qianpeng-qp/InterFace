from base.runmethod import Runmethod
from operaction_data.dependent import DependentData
from tool.common_util import Common_util
from tool.operation_excel import OperationExcel
from tool.operation_herder import Operation_herder
from tool.operationjson import OperationJson
from tool.send_email import SendEmail
from tool.setup_logging import Log

log = Log()


class RunTest:
    def __init__(self):
        self.run_method = Runmethod()
        self.data = OperationExcel()
        self.com_util = Common_util()
        self.send_mail = SendEmail()

    def go_on_run(self):
        res = None
        pass_cont = []
        fail_cont = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_request_data(i)
                expect_data = self.data.get_except_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    '''获取依赖响应数据'''
                    depend_response_data = self.depend_data.get_data_for_key(row=i)
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                if header == 'write':
                    res = self.run_method.run_main(method, url, request_data)
                    op_header = Operation_herder(res)
                    op_header.write_cookie()
                elif header == 'yes':
                    op_json = OperationJson(file_path='dataconfig/cookie.json')
                    cookie = op_json.get_data('apsid')
                    cookies = {"apsid": cookie}
                    res = self.run_method.run_main(method, url, request_data, cookies)
                elif header == 'no' or header is None:
                    res = self.run_method.run_main(method, url, request_data)
                    log.debug('url:%s;method:%s; request_data:%s; result:%s;' % (url, method, request_data, res))
                else:
                    res = self.run_method.run_main(method, url, request_data, header)
                    log.debug('url:%s;method:%s; request_data:%s; result:%s;' % (url, method, request_data, res))
                if self.com_util.is_contain(expect_data, res) == True:
                    self.data.write_result(i, 'pass')
                    pass_cont.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_cont.append(i)
        log.debug('成功案例：%s;失败案例%s' % (pass_cont, fail_cont))
        # self.send_mail.send_main(pass_cont, fail_cont)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
