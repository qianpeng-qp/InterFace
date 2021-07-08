# import pymysql
#
# db = pymysql.connect(***)
# cursor = db.cursor()
# cursor.execute()
# db.commit()
# db.close()

#
# import xlrd
# data = xlrd.open_workbook(filepath)
# table = data.sheet_by_name(sheet_name='')
# table.cell_value()


import pytest


@pytest.mark.parametrize("id", [1, 2, 3, 4, 5])
def test_fun1(id):
    print(id)


@pytest.fixture()
def test_fun2():
    print(2)
