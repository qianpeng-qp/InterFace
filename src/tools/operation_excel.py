import xlrd

from tool.operation_file import filepath


class Operation_excel:
    def __init__(self, excelPath=filepath('dataconfig/case1.xlsx'), sheetName="Sheet1"):
        self.path = excelPath
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

    def get_value(self, row, col):
        return self.table.cell(row, col)
