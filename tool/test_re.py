# from tool import operation_file
#
# a = 'i/a'
# # b = re.match(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[cn,com]{1,3}$', a)
# # b = re.match(r'/.*', a)
# # if re.match(r'/.*', a):
# #     print(1)
#
#
# operation_file.filepath(a)
# # ml = re.sub(pattern, a, count=1)
# # b = pattern.findall(a)
# # print(b)
# [{"status": "COMPLETE", "method": "POST", "protocolVersion": "HTTP/2.0", "scheme": "https",
#   "host": "beacon.tingyun.com", "actualPort": 443, "path": "/xhr1",
#   "query": "pvid=aed77b15-06ed-4b09-b7ba-e0988522afbd&ref=https%3A%2F%2Fblog.csdn.net%2Fralrk%2Farticle%2Fdetails%2F104394766&referrer=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DtKlJ5IGW5imMRrjrNRLbnnK2myFJki2k2EVgN-Oh6d-7LaeNmXgdug7kfvSOio4TaJdzOVzwUwBWO0qdbXaRBa%26wd%3D%26eqid%3Dbe8fd74900063f630000000460657bdf&key=QG29kA_pBzU&v=1.8.3&av=1.8.3&did=f68d41ee-e301-4457-9039-85c9d1a2b921&sid=d505051a-df7d-433e-b8e3-123c1b0b1a5e&__r=1617264586191",
#   "tunnel": false, "keptAlive": true, "webSocket": false, "remoteAddress": "beacon.tingyun.com/140.143.52.226",
#   "clientAddress": "/127.0.0.1", "clientPort": 49947,
#   "times": {"start": "2021-04-01T16:09:46.194+08:00", "requestBegin": "2021-04-01T16:09:46.194+08:00",
#             "requestComplete": "2021-04-01T16:09:46.195+08:00", "responseBegin": "2021-04-01T16:09:46.321+08:00",
#             "end": "2021-04-01T16:09:46.330+08:00"},
#   "durations": {"total": 136, "dns": null, "connect": null, "ssl": null, "request": 1, "response": 9, "latency": 126},
#   "speeds": {"overall": 25507, "request": 3261000, "response": 23111}, "totalSize": 3469,
#   "ssl": {"protocol": "TLSv1.2", "cipherSuite": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"}, "alpn": {"protocol": "h2"},
#   "request": {"sizes": {"headers": 352, "body": 2909}, "mimeType": "text/plain", "charset": "UTF-8",
#               "contentEncoding": null, "header": {
#           "headers": [{"name": ":method", "value": "POST"}, {"name": ":authority", "value": "beacon.tingyun.com"},
#                       {"name": ":scheme", "value": "https"}, {"name": ":path",
#                                                               "value": "/xhr1?pvid=aed77b15-06ed-4b09-b7ba-e0988522afbd&ref=https%3A%2F%2Fblog.csdn.net%2Fralrk%2Farticle%2Fdetails%2F104394766&referrer=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DtKlJ5IGW5imMRrjrNRLbnnK2myFJki2k2EVgN-Oh6d-7LaeNmXgdug7kfvSOio4TaJdzOVzwUwBWO0qdbXaRBa%26wd%3D%26eqid%3Dbe8fd74900063f630000000460657bdf&key=QG29kA_pBzU&v=1.8.3&av=1.8.3&did=f68d41ee-e301-4457-9039-85c9d1a2b921&sid=d505051a-df7d-433e-b8e3-123c1b0b1a5e&__r=1617264586191"},
#                       {"name": "content-length", "value": "2909"}, {"name": "sec-ch-ua",
#                                                                     "value": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\""},
#                       {"name": "sec-ch-ua-mobile", "value": "?0"}, {"name": "user-agent",
#                                                                     "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},
#                       {"name": "content-type", "value": "text/plain;charset=UTF-8"}, {"name": "accept", "value": "*/*"},
#                       {"name": "origin", "value": "https://blog.csdn.net"},
#                       {"name": "sec-fetch-site", "value": "cross-site"}, {"name": "sec-fetch-mode", "value": "no-cors"},
#                       {"name": "sec-fetch-dest", "value": "empty"},
#                       {"name": "referer", "value": "https://blog.csdn.net/ralrk/article/details/104394766"},
#                       {"name": "accept-encoding", "value": "gzip, deflate, br"},
#                       {"name": "accept-language", "value": "zh-CN,zh;q=0.9"}]}, "body": {
#           "text": "{\"xhr\":[{\"id\":1,\"req\":\"GET https://img-home.csdnimg.cn/data_json/toolbar/toolbar1217.json\",\"start\":1617264581508,\"du\":40,\"cb\":8,\"status\":200,\"err\":0,\"rec\":3332,\"send\":0,\"type\":\"XHR\"},{\"id\":0,\"req\":\"GET https://event.csdn.net/logstores/csdn-pc-tracking-pageview/track_ua.gif?APIVersion=0.6.0&cid=10_17096318260-1611653073534-330210&sid=10_1617264581211.689611&pid=blog&uid=&did=10_17096318260-1611653073534-330210&dc_sid=737ec7a12e1e0088d522b6b72e2ad6a4&ref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DtKlJ5IGW5imMRrjrNRLbnnK2myFJki2k2EVgN-Oh6d-7LaeNmXgdug7kfvSOio4TaJdzOVzwUwBWO0qdbXaRBa%26wd%3D%26eqid%3Dbe8fd74900063f630000000460657bdf&curl=https%3A%2F%2Fblog.csdn.net%2Fralrk%2Farticle%2Fdetails%2F104394766&utm=&spm=1001.2101&tos=3358&adb=0&cCookie=c_first_ref%3Dwww.baidu.com%3Bc_segment%3D2%3Bc_sid%3D737ec7a12e1e0088d522b6b72e2ad6a4%3Bc_ref%3Dhttps%253A%2F%2Fwww.baidu.com%2Flink%3Bc_pref%3Dhttps%253A%2F%2Fwww.baidu.com%2Flink%3Bc_session_id%3D10_1617264581211.689611%3Bc_first_page%3Dhttps%253A%2F%2Fblog.csdn.net%2Fralrk%2Farticle%2Fdetails%2F104394766%3Bc_page_id%3Ddefault%3B&t=1617264581&screen=1792*1120&un=&urn=1617264581470-ab3ed1a3-fff5-4180-b754-9de9b8ab2293&vType=&log_id=294\",\"start\":1617264581473,\"du\":365,\"cb\":1,\"status\":200,\"err\":0,\"rec\":43,\"send\":0,\"type\":\"XHR\"},{\"id\":3,\"req\":\"GET https://kunpeng.csdn.net/ad/json/536\",\"start\":1617264581555,\"du\":415,\"cb\":0,\"status\":200,\"err\":0,\"rec\":51,\"send\":0,\"type\":\"XHR\"},{\"id\":5,\"req\":\"POST https://blog.csdn.net/phoenix/web/v1/comment/list/104394766?page=1&size=10&commentId=\",\"start\":1617264581695,\"du\":296,\"cb\":10,\"status\":200,\"err\":0,\"rec\":588,\"send\":0,\"type\":\"XHR\"},{\"id\":6,\"req\":\"GET https://img-home.csdnimg.cn/data_json/jsconfig/shop-window-new.json\",\"start\":1617264581799,\"du\":204,\"cb\":1,\"status\":200,\"err\":0,\"rec\":721,\"send\":0,\"type\":\"XHR\"},{\"id\":2,\"req\":\"GET https://silkroad.csdn.net/api/v2/assemble/list/channel/search_hot_word?channel_name=pc_hot_word&size=10&platform=pc&imei=10_17096318260-1611653073534-330210&toolbarSearchExt=%7B%22landingWord%22%3A%5B%5D%2C%22queryWord%22%3A%22%22%2C%22tag%22%3A%5B%5D%2C%22title%22%3A%22%E7%88%AC%E5%8F%9612306%E4%BD%99%E7%A5%A8%E4%BF%A1%E6%81%AF%E6%8A%A5%E9%94%99%EF%BC%9Ajson.decoder.JSONDecodeError%3A+Expecting+value%3A+line+1+column+1+(char+0)%22%7D\",\"start\":1617264581553,\"du\":725,\"cb\":0,\"status\":200,\"err\":0,\"rec\":7063,\"send\":0,\"type\":\"XHR\"},{\"id\":7,\"req\":\"GET https://blog.csdn.net/phoenix/web/v1/get-shop-window-goods-list?username=ralrk\",\"start\":1617264582004,\"du\":721,\"cb\":1,\"status\":200,\"err\":0,\"rec\":42,\"send\":0,\"type\":\"XHR\"},{\"id\":4,\"req\":\"POST https://msg.csdn.net/v1/web/message/view/announcement\",\"start\":1617264581556,\"du\":1226,\"cb\":1,\"status\":200,\"err\":0,\"rec\":197,\"send\":0,\"type\":\"XHR\"},{\"id\":8,\"req\":\"POST https://event.csdn.net/logstores/csdn-pc-tracking-page-exposure/track\",\"start\":1617264582489,\"du\":607,\"cb\":1,\"status\":200,\"err\":0,\"rec\":0,\"send\":5429,\"type\":\"XHR\"}]}",
#           "charset": "UTF-8"}},
#   "response": {"status": 200, "sizes": {"headers": 188, "body": 20}, "mimeType": "text/plain", "charset": null,
#                "contentEncoding": "gzip", "header": {
#           "headers": [{"name": ":status", "value": "200"}, {"name": "date", "value": "Thu, 01 Apr 2021 08:09:46 GMT"},
#                       {"name": "content-type", "value": "text/plain"}, {"name": "server", "value": "nginx"},
#                       {"name": "vary", "value": "Accept-Encoding"},
#                       {"name": "access-control-allow-origin", "value": "*"},
#                       {"name": "access-control-allow-headers", "value": "accept, content-type, classname"},
#                       {"name": "access-control-allow-methods", "value": "POST, GET, OPTIONS"},
#                       {"name": "content-encoding", "value": "gzip"}]},
#                "body": {"text": "", "charset": null, "decoded": true}}
