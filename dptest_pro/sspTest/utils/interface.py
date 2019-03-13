# -*- coding: utf-8 -*-


import pymysql
import requests
import json
import os



def set_dp_interface (url,data):
    """
    :param url:接口地址，具体参考文档，如：http://192.168.1.50:8086/screenfeature/screen/update
    :param data:传参，如：{"mediaProviderId":2093}
    :return:res.text
    """

    headers = {'Content-Type': 'application/json;charset=utf-8', 'Connection': 'close'}
    url = url
    datas = json.dumps(data)
    res = requests.post(url, data = datas, headers = headers )
    res_date = res.json()
    print('请求地址：'+ url)
    print('请求参数：'+ str(data))
    # 返回信息
    print ('接口返回结果：'+ str(res.text))
    # print (res['errorCode'])
    # 返回响应头
    # print (res.status_code)
    return res_date








