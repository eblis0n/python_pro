# coding=utf-8

import unittest
from functools import wraps
import pymysql
import os


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

# #提取test头的案例，并且将其后缀名与文件名分离
# 其中os.path.splitext()函数将路径拆分为文件名+扩展名
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.join(file)[0:4] == "test":
                if os.path.splitext(file)[1] == '.py':
                    L.append(os.path.join( file)[0:-3])
    return L