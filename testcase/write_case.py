import os
import shutil

from config.config_message import ConfigMessage
from testcase.write_yml import WriteYml
from tool import operation_file


class WriteCase:
    def writecase(self):
        yml_list = WriteYml.writeyml('${data_dir}$')
        src_path = operation_file.filepath(ConfigMessage().dir_manage('${data_dir}$'))
        temp_path = src_path + 'Template.py'
        for case in yml_list:
            yml_path = case.split('/')[0]
            yml_title = case.split('/')[1]
            case_name = 'test_' + yml_title + '.py'

            new_case_path = operation_file.filepath('testcase/' + yml_path) + '/' + case_name
            if not os.path.exists(new_case_path):
                shutil.copyfile(temp_path, new_case_path)
                n = 0
                with open(new_case_path, 'r', encoding='utf-8') as fw:
                    source = fw.readlines()
                with open(new_case_path, 'w', encoding='utf-8') as f:
                    for line in source:
                        if 'PATH = project_path' in line:
                            line = line.replace("offer", "%s" % yml_path)
                            f.write(line)
                            n = n + 1
                        elif 'case_dict = ini_case' in line:
                            line = line.replace("Template", yml_title)
                            f.write(line)
                            n = n + 1
                        elif 'class TestTemplate' in line:
                            line = line.replace("TestTemplate", "Test%s" % yml_title.title().replace("_", ""))
                            f.write(line)
                            n = n + 1
                        elif '@allure.story' in line:
                            line = line.replace("Template", yml_title)
                            f.write(line)
                            n = n + 1
                        elif 'def test_template' in line:
                            line = line.replace("template", yml_title.lower())
                            f.write(line)
                            n = n + 1
                        else:
                            f.write(line)
                            n += 1
                    for i in range(n, len(source)):
                        f.write(source[i])
            else:
                pass


if __name__ == '__main__':
    WriteCase().writecase()
