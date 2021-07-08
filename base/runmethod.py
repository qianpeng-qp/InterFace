import requests
import json


class Runmethod:
    def post_main(self, url, data, header=None):
        if header != None:
            result = requests.post(url=url, data=data)
        else:
            result = requests.post(url=url, data=data)
        return result

    def get_main(self, url, data, verify=False):
        result = requests.get(url=url, params=data, verify=verify)
        return result

    def run_main(self, method, url, data=None, header=None):
        if method == 'post':
            result = self.post_main(url=url, data=data, header=header)
        else:
            result = self.get_main(url=url, data=data)
        try:
            return json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        except:
            return result.text


if __name__ == '__main__':
    data = {"grant_type": "client_credentials", "client_id": "U7Z6NnsQNOLkdTWITItGgf1w",
            "client_secret": "9cRLl0ZMWQCEkFxQeb73zC4feFsCry4e"}

    result = Runmethod().get_main(url='https://aip.baidubce.com/oauth/2.0/token', data=data)
    print(result.text)
