# -*- coding: utf-8 -*-
import pymysql
import requests
import json
import os

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






