# coding=utf-8

import unittest
from functools import wraps
import pymysql
import os
import requests
import json


############################# 接口###########################
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



############################# 装饰器类的方法###########################

# 装饰器
def skip_dependon(depend=""):
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)
        return inner_func
    return wraper_func


############################# 数据库类的方法###########################

def conn(host,port,user,passwd,dbName):
    """

    :param host:主机地址，如：192.168.1.51
    :param port: 端口号，如：8070
    :param user: 数据库账号，如：root
    :param passwd: 数据库密码，如：123
    :param db: 数据库名，如：ad_account
    :return: 返回文件描述符
    """
    conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, db=dbName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
    return conn

############################# 应用类的方法###########################

# 提取test头的案例，并且将其后缀名与文件名分离
# 其中os.path.splitext()函数将路径拆分为文件名+扩展名
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.join(file)[0:4] == "test":
                if os.path.splitext(file)[1] == '.py':
                    L.append(os.path.join( file)[0:-3])
    return L

# 判断
def comparison_1(self,inf_source,sql_source,statisDates,inf_data,sql_data):
    """

        :param self:unittest 断言需要使用
        :param inf_source: 接口data
        :param sql_source: 数据库data
        :param statisDates: 接口返回的日期
        :param inf_data: 接口需要比对的字段
        :param sql_data: 数据库需要比对的字段
        :return: 无
        """
    for i in range(len(inf_source)):
        statisDate = inf_source[i].get(statisDates)
        com_inf_data = inf_source[i].get(inf_data)
        com_sql_data = sql_source[i].get(sql_data)
        print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}'.format(statisDate, com_inf_data, com_sql_data))
    self.assertEqual(str(com_inf_data), str(com_sql_data), "这个字段,数据对不上")

# 判断report输出的名称
def repName(casename):
    if casename == "sspCase":
        reportname = "ssp平台测试报告"
    elif casename == "dmpCase":
        reportname = "dmp平台测试报告"
    else:
        reportname = "未知测试报告"

    return  reportname


# def ergodicReport():
#     if len(aa) == len(int_aa):
#         for i in range(0, len(aa)):
#             if str(res_date['data'][i].get('customerId')) == str(aa[i].get('dsp_id')):
#                 print("第一波通过"+ str(res_date['data'][i].get('customerId')),str(aa[i].get('dsp_id')))
#                 if str(res_date['data'][i].get('playTime')) == str(aa[i].get('confirm_num')):
#                     print("good,数据匹配"+ str(res_date['data'][i].get('playTime')), str(aa[i].get('confirm_num')))
#                 else:
#                     print("错了" + str(res_date['data'][i].get('playTime')), str(aa[i].get('confirm_num')))