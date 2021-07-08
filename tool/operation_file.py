import os
import time
import re


def root_dir():
    root = os.path.dirname(__file__)
    while True:
        md_file = os.path.join(root, 'readme.txt')  # 以项目路径下的readme为依据，直到找找到
        if os.path.exists(md_file):  # 如果存在这个文件，root值已经是项目根目录
            break
        root = os.path.dirname(root)

    return root


def filepath(path):
    # r = os.path.join(root_dir(), 'src/')  path = path[1:]path = path[1:]
    r = root_dir()
    if re.match(r'/.*', path):
        path = path[1:]
    file_path = os.path.join(r, path)
    if not os.path.exists(file_path):

        os.mkdir(file_path)
    return file_path


def filename(name):
    file_time = time.strftime('%Y_%m_%d', time.localtime())

    return f'{file_time}-{name}'


if __name__ == '__main__':
    os.mkdir('/Users/pq/git/InterFace/testcase/page/2.0')
    # print(filepath('testcase/page/2.0'))
