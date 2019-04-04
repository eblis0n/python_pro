# -*- coding: utf-8 -*-

from constants.yunproInterface import interface_58 as  interface
# from constants.interfaceName import queryentrySspSummary
# from constants.parameter import iflyImportscreen_data
import utils.interface as utilsInterface
import constants.interfaceName as interfaceName
import  constants.parameter as parameter
import utils.exploreSql as exploreSql
import unittest
# import pymysql
# import requests
# import json
import os
import configparser  as cparser
import openpyxl

# ===============读取配置文件============== #
base_dr = str(os.path.dirname(os.path.dirname(__file__)))
bae_idr = base_dr.replace('\\', '/')




# 读取配置文件上的
mysqlHost = conf.get("mysqlconf", "host")   # 读取配置文件上数据库主机号
mysqlPort = conf.get("mysqlconf", "port")    # 读取配置文件数据库的端口号
mysqlUser = conf.get("mysqlconf", "user")    # 读取配置文件数据库的账号
mysqlPassword = conf.get("mysqlconf", "password")   # 读取配置文件数据库的密码
mysqlName = conf.get("mysqlconf", "db_name")   # 读取配置文件数据库的名字

# 定义字段来源
queryentrySspSummary = table2["E2"].value
login_data = parameter.login_data
totalsummary_data = str(table2["F2"].value)
set_dp_interface = utilsInterface.set_dp_interface
get_media_screenCount = exploreSql.get_media_screenCount
conn = exploreSql.conn

planentry_url = table2["D2"].value

totalsummary_data1 = parameter.totalsummary_data1



# 读取配置文件 # 连接数据库
connect = conn(host=mysqlHost, port=mysqlPort, user=mysqlUser, passwd=mysqlPassword, dbName=mysqlName)

# 执行接口
res_date = set_dp_interface(url="http://192.168.1.58:3000/api/v2/dmp/v2/analysis/totalsummary",data = sspSummary_data)
screenCount = res_date['data'].get("screenCount")
# print(res_date['data'].get("screenCount"))
print(screenCount)

# 执行SQL查询
sql_screencount = get_media_screenCount(2028, '2019-02-14',conn = connect )
sCount = sql_screencount[0].get("SUM(screen_count)")
print(sCount)
# 判断 接口数据与数据库查询结果

if screenCount == sCount:
    print("成功了")
    print('接口返回结果：%s , 数据库查询结果：%d' %(screenCount,sCount))
else:
    print("失败了!!")
    print('接口返回结果：%s , 数据库查询结果：%d' %(screenCount,sCount))



