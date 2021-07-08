from config.conf_read import ConfRead
import re


class ConfigMessage:

    def host_message(self, hos):
        """
        host关联配置
        :param hos:
        :return:
        """
        try:
            relevance_list = re.findall(r"\${(.*?)}\$", hos)
            for n in relevance_list:
                pattern = re.compile(r'\${' + n + r'}\$')
                host_cf = ConfRead()
                host_relevance = host_cf.read_title('host')
                hos = re.sub(pattern, host_relevance[n], hos, count=1)
        except TypeError:
            pass
        return hos

    def mail_manage(self, ml):
        """
        email关联配置
        :param ml:
        :return:
        """
        if not re.match(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[cn,com]{1,3}$', ml):
            raise TypeError
        return ml

    def dir_manage(self, directory):
        """
        directory关联配置
        :param directory:
        :return:
        """
        try:
            relevance_list = re.findall(r"\${(.*?)}\$", directory)
            for n in relevance_list:
                pattern = re.compile(r'\${' + n + r'}\$')
                dir_cf = ConfRead()
                dir_relevance = dir_cf.read_title('directory')
                directory = re.sub(pattern, dir_relevance[n], directory, count=1)
        except TypeError:
            pass
        return directory


if __name__ == '__main__':
    re = ConfigMessage().dir_manage('${data_dir}$')
    print(re)
