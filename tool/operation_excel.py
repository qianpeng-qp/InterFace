import xlrd
from operaction_data.data_config import global_var
from xlutils.copy import copy
from tool.operation_file import filepath
from tool.operationjson import OperationJson
import json


class OperationExcel:
    def __init__(self, excelPath=filepath('dataconfig/case1.xlsx'), sheetName="Sheet1"):
        # 获取sheet内容
        self.excelPath = excelPath
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def get_case_lines(self):
        '''获取案例行数'''
        return self.rowNum

    def get_lines(self):
        '''获取单元格列数'''
        return self.colNum

    def get_cell_value(self, row, col):
        '''某单元格的值'''
        return self.table.cell_value(rowx=row, colx=col)

    def get_row_data(self, row=None):
        '''根据行号获取某一行内容'''
        if row != None:
            rows = self.table.row_values(row)
        else:
            rows = self.table.row_values(0)

        return rows

    def get_col_data(self, col=None):
        '''根据列号获取某一列内容'''
        if col != None:
            cols = self.table.col_values(col)
        else:
            cols = self.table.col_values(0)

        return cols

    def write_value(self, row, col, value):
        '''写入excel'''
        write_data = copy(self.data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.excelPath)

    def get_row_num(self, case_id):
        '''根据对应的caseid找到对应的行号'''
        num = 0
        cols_data = self.get_col_data()
        for cols_data in cols_data:
            if case_id == cols_data:
                return int(num)
            num = num + 1

    def is_run(self, row):
        '''是否运行'''
        flag = None
        col = int(global_var.run)
        run_model = self.table.cell_value(rowx=row, colx=col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        '''请求头'''
        col = int(global_var.header)
        header = self.table.cell_value(rowx=row, colx=col)
        if header != '':
            return header
        else:
            return None

    def get_request_method(self, row):
        '''请求方式'''
        col = int(global_var.request_way)
        request_method = self.table.cell_value(rowx=row, colx=col)
        return request_method

    def get_request_url(self, row):
        '''请求地址'''
        col = int(global_var.url)
        url = self.table.cell_value(rowx=row, colx=col)
        return url

    def get_request_data(self, row):
        '''获取请求数据'''
        col = int(global_var.data)
        data = self.table.cell_value(rowx=row, colx=col)
        if data == '':
            return None
        else:
            return json.loads(data)

    def get_data_for_json(self, row):
        '''通过关键字拿到data'''
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    def get_except_data(self, row):
        '''获取预期结果'''
        col = int(global_var.expect)
        expect = self.table.cell_value(rowx=row, colx=col)
        if expect == '':
            return None
        else:
            return expect

    def get_depend_key(self, row):
        '''获取依赖数据的key'''
        col = int(global_var.data_depend)
        depend_key = self.table.cell_value(rowx=row, colx=col)
        if depend_key == '':
            return None
        else:
            return depend_key

    def is_depend(self, row):
        '''case是否有依赖'''
        col = int(global_var.case_depend)
        depend_case_id = self.table.cell_value(rowx=row, colx=col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    def get_depend_field(self, row):
        '''获取数据依赖字段'''
        col = int(global_var.field_depend)
        data = self.table.cell_value(rowx=row, colx=col)
        if data == '':
            return None
        else:
            return data

    def write_result(self, row, value):
        col = int(global_var.result)
        self.write_value(row, col, value)

    # def dict_data(self):
    #     if self.rowNum <= 1:
    #
    #         print("------总行数小于1")
    #     else:
    #         r = []
    #         j = 1
    #         for i in range(self.rowNum - 1):
    #
    #             # 从第二行取对应values值
    #             values = self.table.row_values(j)
    #             if values:
    #                 s = {}
    #                 for x in range(self.colNum):
    #                     s[self.keys[x]] = values[x]
    #                 r.append(s)
    #                 j += 1
    #         return r


if __name__ == '__main__':
    str = '{"text":"垃圾","access_token":"24.49b459ea74af4b5736cdb6bc1f81954e.2592000.1617174696.282335-23724228"}'
    a = json.loads(str)
    print(a)
