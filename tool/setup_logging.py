import logging
import os
from tool import operation_file as tools


class Log:
    __logger = None  # 定义类的私有属性 默认值为 None

    def __new__(cls, *args, **kwargs):
        if cls.__logger == None:
            # 创建一下 日志类， 'cnodeApi' 为 logging name属性值
            cls.__logger = logging.getLogger('testcase')
            cls.__logger.setLevel(logging.DEBUG)  # 设置日志级别 DEBUG

            log_path = tools.filepath('logs')
            file_name = tools.filename('test.log')
            logfile_path = os.path.join(log_path, file_name)
            fh = logging.FileHandler(logfile_path, encoding='utf-8')  # 创建日志存储文件对象 app.log 日志存储文件名
            ch = logging.StreamHandler()  # 命令行输出流

            # log格式
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')

            fh.setFormatter(formatter)  # 文件存储赋给 __logger
            ch.setFormatter(formatter)  # 输出流 添加日志格式

            cls.__logger.addHandler(fh)  # 文件存储赋给 __logger
            cls.__logger.addHandler(ch)  # 输出流 赋给 __logger

        return cls.__logger
