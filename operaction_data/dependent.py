import json

from base.runmethod import Runmethod
from tool.operation_excel import OperationExcel
from jsonpath_rw import jsonpath, parse

from tool.setup_logging import Log

log = Log()


class DependentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()

    def get_case_line_data(self):
        '''通过case_id去获取该case_id的整行数据'''
        rows_data = self.opera_excel.get_row_data(self.case_id)
        return rows_data

    def run_dependent(self):
        '''执行依赖测试，获取结果'''
        run_method = Runmethod()
        row_num = int(self.opera_excel.get_row_num(self.case_id))
        request_data = self.opera_excel.get_request_data(row_num)
        header = self.opera_excel.is_header(row_num)
        method = self.opera_excel.get_request_method(row_num)
        url = self.opera_excel.get_request_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    def get_data_for_key(self, row):
        '''根据依赖的key去获取执行依赖测试case的响应,然后返回'''
        depend_data = self.opera_excel.get_depend_key(row=int(row))
        response_data = self.run_dependent()
        # print(response_data[depend_data])
        json_exe = parse(depend_data)  # 依赖格式   'student[*].female'
        male = json_exe.find(response_data)  # 返回值，依赖
        value = [match.value for match in male]
        return value
