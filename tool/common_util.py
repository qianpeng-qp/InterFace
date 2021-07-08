import json
import operator


class Common_util:

    def is_contain(self, str_one, str_two):
        '''
           判断字符串是否在另一个字符串中
           str_one:查找的字符串
           str_two:被查找的字符串
           '''
        flag = None
        # if isinstance(str_one, str) == False:
        #     str_one = str_one.encode('unicode-escape').decode('string_escape')
        #     return operator.eq(str_one, str_two)
        try:
            if str_one in str_two:
                flag = True
            else:
                flag = False
            return flag
        except:
            return flag

    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        :param dict_one:
        :param dict_two:
        :return:
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
            # print(dict_one)

        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
            # print(dict_two)
        return operator.eq(dict_one, dict_two)


