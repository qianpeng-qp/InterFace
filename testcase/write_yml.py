import json
import urllib.parse
from config.config_message import ConfigMessage
from tool import operation_file
import os
from ruamel import yaml
from tool.setup_logging import Log

log = Log()


class WriteYml:
    def writeyml(datapath):
        har_path = operation_file.filepath(ConfigMessage().dir_manage(datapath))
        print(har_path)
        har_list = os.listdir(har_path)
        case_file_list = []
        for i in har_list:
            # if 'chlsj' in i:
            if 'test1.chlsj' in i:
                with open(har_path + i, 'r', encoding='utf-8') as f:
                    log.debug("从%s目录下，读取文件%s" % (har_path, i))
                    har_ct = json.loads(f.read())[0]
                    path = har_ct['path']
                    method = har_ct['method']
                    scheme = har_ct['scheme']
                    title = path.split('/')[-1]
                    info_id = "test_" + title + "_01"
                    parameter_type = har_ct["request"]["mimeType"]
                    parameter = dict()
                try:
                    if method in 'POST':
                        parameter_list = urllib.parse.unquote(har_ct["request"]["body"]["text"])
                    elif method in 'PUT':
                        parameter_list = har_ct["request"]["body"]["text"]
                    elif method in 'DELETE':
                        parameter_list = urllib.parse.unquote(har_ct["request"]["body"]["text"])
                    else:
                        parameter_list = har_ct["query"]
                    if "&" in parameter_list:

                        for key in parameter_list.split("&"):
                            val = key.split("=")
                            parameter[val[0]] = val[1]
                    else:
                        try:
                            parameter = json.loads(parameter_list)
                        except:
                            parameter = parameter_list
                except Exception as e:
                    log.error("未找到parameter: %s" % e)
                    raise e
                case_path = operation_file.filepath(ConfigMessage().dir_manage('${page_dir}$') + path.split("/")[-2])
                response_code = har_ct["response"]["status"]
                response_body = har_ct["response"]["body"]["text"]
                test_info = dict()
                test_info["id"] = info_id
                test_info["title"] = path.split("/")[-2]
                test_info["host"] = '${host}$'
                test_info["address"] = path
                # 定义checkout(),输出 结果json
                case_list = dict()
                check = dict()
                check["check_type"] = 'json'
                check["expected_code"] = response_code
                expected_request = json.loads(response_body)
                result_file = 'result_' + title + '.json'
                # 大于4行写入json文件
                if len(expected_request) >= 2:
                    if not os.path.exists(case_path + '/' + result_file):
                        result_dicts = dict()
                        result_dicts['test_name'] = title
                        result_dicts['json'] = expected_request
                        with open(case_path + '/' + result_file, 'w', encoding='utf-8')as ff:
                            json.dump(result_dicts, ff, ensure_ascii=False, indent=4)
                else:
                    check['expected_request'] = expected_request
                test_case_list = []
                test_case = dict()
                test_case_list.append(test_case)
                param_file = title + '.json'
                # 大于2行写入json文件
                if len(parameter) >= 2:
                    if not os.path.exists(case_path + '/' + param_file):
                        with open(case_path + '/' + param_file, 'w', encoding='utf-8')as ff:
                            json.dump(parameter, ff, ensure_ascii=False, indent=4)
                        test_case["parameter"] = title + '.json'
                else:
                    test_case["parameter"] = parameter
                test_case['test_name'] = title
                test_case['info'] = title
                test_case['http_type'] = scheme
                test_case['request_type'] = method
                test_case['parameter_type'] = parameter_type
                test_case['address'] = path
                test_case["headers"] = {"X-Requested-With": "XMLHttpRequest"}
                test_case["cookies"] = True
                test_case["timeout"] = 20
                test_case["file"] = False
                test_case["check"] = check
                test_case["relevance"] = None

                case_list["test_info"] = test_info
                case_list["premise"] = None
                case_list["test_case"] = test_case_list
                case_file = case_path + '/' + title + '.yml'
                if not os.path.exists(case_file):
                    with open(case_file, 'w', encoding='utf-8') as fd:
                        case_file_list.append(path.split("/")[-2] + '/' + title)
                        log.debug("从%s目录下，写入测试文件%s" % (case_path, case_file))
                        yaml.dump(case_list, fd, Dumper=yaml.RoundTripDumper)
        return case_file_list

if __name__ == '__main__':
    print(WriteYml.writeyml('${data_dir}$'))