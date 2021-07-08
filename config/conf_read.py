from configparser import ConfigParser
import os


class ConfRead:
    def __init__(self):
        self.conf = ConfigParser()
        self.path = os.path.join(os.path.dirname(__file__), 'config.ini')
        if not os.path.exists(self.path):
            raise FileNotFoundError("请确保配置文件存在！")

    def get_mail_address(self):
        """
        读取配置文件中email地址
        :return:
        """
        self.conf.read(self.path, encoding='utf-8')
        return self.conf.get('section', 'mail')

    def get_config(self, title, text):
        self.conf.read(self.path, encoding='utf-8')
        return self.conf.get(title, text)

    def set_config(self, title, value, text):
        self.conf.read(self.path)
        self.conf.set(title, value, text)
        with open(self.path, 'w')as f:
            self.conf.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.conf.add_section(title)
        with open(self.path, "a", encoding='utf-8') as f:
            self.conf.write(f)

    def read_title(self, title):
        """
        配置文件读取directory
        :return:
        """
        self.conf.read(self.path)
        return self.conf[title]


if __name__ == '__main__':
    # ConfRead().add_conf('test')
    # ConfRead().set_config(title='host', value='host', text='1.1.1.1')
    print(ConfRead().get_config('section', 'name'))
