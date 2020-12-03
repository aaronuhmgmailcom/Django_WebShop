import datetime
import base64
import json
import hashlib
# 通过代码发送http/https请求
import requests

from django.core.cache import cache


class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken, appId, templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId = appId
        self.templateId = templateId

    # 1.构造业务url
    def get_request_url(self, sig):
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid, sig)
        return self.url

    # 获取时间戳
    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

    # 计算sig
    def get_sig(self, timestamp):
        s = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(s.encode())
        return md5.hexdigest().upper()

    # 2.构造请求头
    def get_request_header(self, timestamp):
        s = self.accountSid + ':' + timestamp
        b_s = base64.b64encode(s.encode()).decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': b_s
        }

    # 3. 请求体
    def get_request_body(self, phone, code):
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, "3"]
        }
        return data

    # 4. 发送请求
    def do_request(self, url, header, body):
        res = requests.post(url, headers=header, data=json.dumps(body))
        return res.text

    # 5. 将以上所有封装一个完整的调用函数
    def run(self, phone, code):
        #  时间戳
        timestamp = self.get_timestamp()
        #  计算url中的参数
        sig = self.get_sig(timestamp)
        # 1. url
        url = self.get_request_url(sig)
        print(url)
        # 2. header
        header = self.get_request_header(timestamp)
        print(header)
        # 3. body
        body = self.get_request_body(phone, code)
        print(body)
        # 4. 发送请求
        res = self.do_request(url, header, body)
        return res


if __name__ == '__main__':
    aid = '8a216da87380115d017389546bb802f5'
    atoken = '12444d5592d247b2af0e5cc10bf666a0'
    appid = '8a216da87380115d017389546c9e02fb'
    tid = '1'
    x = YunTongXin(aid, atoken, appid, tid)
    res = x.run('15827654489', '123456')
    print(res)
