# -*- coding: utf-8 -*-

from constants.yunproInterface import interface_58 as  interface
# from constants.interfaceName import queryentrySspSummary
# from constants.parameter import iflyImportscreen_data
import utils.interface as utilsInterface
import constants.interfaceName as interfaceName
import  constants.parameter as parameter
import utils.exploreSql as exploreSql

import pymysql
import requests
import json
import os
import configparser  as cparser

# ===============读取配置文件============== #
base_dr = str(os.path.dirname(os.path.dirname(__file__)))
bae_idr = base_dr.replace('\\', '/')


# 配置文件的地址
file_path = bae_idr + "/config.ini"

conf = cparser.ConfigParser()

conf.read(file_path)

print(file_path)


# 读取配置文件上的
mysqlHost = conf.get("mysqlconf", "host")   # 读取配置文件上数据库主机号
mysqlPort = conf.get("mysqlconf", "port")    # 读取配置文件数据库的端口号
mysqlUser = conf.get("mysqlconf", "user")    # 读取配置文件数据库的账号
mysqlPassword = conf.get("mysqlconf", "password")   # 读取配置文件数据库的密码
mysqlName = conf.get("mysqlconf", "db_name")   # 读取配置文件数据库的名字

# 定义字段来源

queryentrySspStatisdaily = interfaceName.queryentrySspStatisdaily
sspStatisdaily_data = parameter.sspStatisdaily_data
set_dp_interface = utilsInterface.set_dp_interface
get_media_validScreenCount = exploreSql.get_media_validScreenCount
conn = exploreSql.conn

# 读取配置文件 # 连接数据库
# connect = conn(host=mysqlHost, port=mysqlPort, user=mysqlUser, passwd=mysqlPassword, dbName=mysqlName)

# 执行接口
res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspStatisdaily,data = sspStatisdaily_data)
datass =  res_date['data']
# print(len(datass))
# i = 0
# for i in range(len(datass)):
#     # print(i)
#     b = datass[i]
#     a = datass[i].get("validScreenCount")
#     print(b)


# 执行SQL查询
pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
pymysqlcursor = pymysqlconn.cursor()
sql = "SELECT transaction_date,request_screens,play_times,play_duration FROM	ssp_play_summary WHERE (transaction_date BETWEEN '2019-02-14'	AND '2019-02-20') AND ssp_id = 2028;"
pymysqlcursor.execute(sql)
sql_datass=pymysqlcursor.fetchall()
print(sql_datass)
# sql_screenCount = sql_datass[0].get("SUM(screen_count)")
# j = 0
# for j in range(len(sql_datass)):
#     # print(i)
#     b = sql_datass[j]
#     a = sql_datass[j].get("request_screens")
#     print(a)

if len(sql_datass) == len(datass):
    i = 0
    for i in range(len(datass)):
     # print(i)
     b = datass[i]
     a = datass[i].get("validScreenCount")
     c =  sql_datass[i].get("request_screens")
     if  a == c:
         print("成功了")
     else:
         print("失败")
else:
    print("数据不对等")