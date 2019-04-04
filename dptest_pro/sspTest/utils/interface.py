# -*- coding: utf-8 -*-

import requests
import json

def set_dp_interface (url,data):
    """
    :param url:接口地址，具体参考文档，如：http://192.168.1.50:8086/screenfeature/screen/update
    :param data:传参，如：{"mediaProviderId":2093}
    :return:res.text
    """

    headers = {'Content-Type': 'application/json;charset=utf-8', 'Connection': 'close'}
    # headers = headers
    url = url
    # 虽然不知道是什么原理，如果是通过Excel读取json格式数据，就用先dumps 后再 loads一下服务器才能识别
    datas = json.dumps(data)  # 输入的是str类型
    datas1 = json.loads(datas) # 输出的是dict类型
    # datas = data
    res = requests.post(url, data = datas1, headers = headers )
    res_date = res.json()
    print('请求地址：'+ url)
    print('请求参数：'+ str(datas1))
    # 返回信息
    print ('接口返回结果：'+ str(res.text))
    # print('响应头：'+ str(res.headers))
    # print (res['errorCode'])
    # 返回响应头
    # print (res.status_code)
    return res_date









