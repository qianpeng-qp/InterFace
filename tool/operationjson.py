import json
from tool.operation_file import filepath

class OperationJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = filepath('dataconfig/user.json')
        else:
            self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        '''读取json文件'''
        with open(self.file_path) as fp:
            data = json.load(fp)
        return data

    def get_data(self, id):
        '''根据关键字进行获取数据'''
        # print(self.data)
        return self.data[id]

    def write_json(self, data):
        with open(filepath('dataconfig/cookie.json'), 'w') as fp:
            fp.write(json.dumps(data))

#
if __name__ == '__main__':
    open1 = OperationJson()
    print(open1.get_data('url'))
#     open1.write_json({'id':'5555'})
#     # print(open1.data)
