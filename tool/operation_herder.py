import json

import requests
from requests import utils
from tool.operationjson import OperationJson


class Operation_herder:
    def __init__(self, response):
        self.response = json.loads(response)


    def get_response_url(self):
        '''
        :return: 获取登陆返回的token
        '''

        url = self.response['data']['url'][0]
        return url

    def get_cookie(self):
        '''
        获取cookie的jar
        :return:
        '''

        # url = self.get_response_url + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        # cookie = requests.get(url).cookies
        cookie = self.response.cookies
        print('*********'+cookie)
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie)

        op_json = OperationJson()
        op_json.write_json(cookie)

