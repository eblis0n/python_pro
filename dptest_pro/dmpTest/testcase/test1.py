# encoding=utf-8

import pymysql

import openpyxl
from openpyxl.styles import colors
from openpyxl.styles import Font, Color

from constants.yunproInterface import interface_58 as  interface
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


#加载测试用例
#####################################使用openpyxl######################################
# 当前脚本的真实路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(cur_path)

# 读取Excel内容
wbook=openpyxl.load_workbook(cur_path + "/testexcel/dmptest3.xlsx")
table2=wbook['Test_Case2']



#测试结果输出的文件名

begtest=[]
endtest=[]

for i in range(1,int(table2.max_column)):
    if table2["A"+str(i)].value=="go":
        begtest.append(i)

    if table2["L"+str(i)].value=="end":
        endtest.append(i)
if len(begtest)==0:#检查是否有可用的用例
    print('没有可执行的用例')
    quit()
if len(begtest)!=len(endtest):
    print("用例有误,请检查各单元用例的开始和结束是否一致")
    quit()
print("测试用例加载完成")
print(len(begtest))

for j in range(0, len(begtest)):
    for k in range(1, int(begtest[i] + 1)):

        print("excel:"+table2["C"+str(k)].value)




# # 读取配置文件上的
# mysqlHost = conf.get("mysqlconf", "host")   # 读取配置文件上数据库主机号
# mysqlPort = conf.get("mysqlconf", "port")    # 读取配置文件数据库的端口号
# mysqlUser = conf.get("mysqlconf", "user")    # 读取配置文件数据库的账号
# mysqlPassword = conf.get("mysqlconf", "password")   # 读取配置文件数据库的密码
# mysqlName = conf.get("mysqlconf", "db_name")   # 读取配置文件数据库的名字
#
# # 定义字段来源
#
# queryentrySspStatisdaily = interfaceName.queryentrySspStatisdaily
# sspStatisdaily_data = parameter.sspStatisdaily_data
# set_dp_interface = utilsInterface.set_dp_interface
# get_media_validScreenCount = exploreSql.get_media_validScreenCount
# conn = exploreSql.conn
# queryentry_url = table2["D3"].value
#
# print(table2["D3"].value)
#
# ########################################开始测试#################################
# # 执行接口
# res_date = set_dp_interface(url=queryentry_url + queryentrySspStatisdaily,data = sspStatisdaily_data)
# datass =  res_date['data']
# print(datass)

# # 执行SQL查询
# pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
#                            charset="utf8",cursorclass = pymysql.cursors.DictCursor)
# pymysqlcursor = pymysqlconn.cursor()
# sql = "SELECT transaction_date,request_screens,play_times,play_duration FROM	ssp_play_summary WHERE (transaction_date BETWEEN '2019-02-14'	AND '2019-02-20') AND ssp_id = 2028;"
# pymysqlcursor.execute(sql)
# sql_datass=pymysqlcursor.fetchall()
# print(sql_datass)
# # sql_screenCount = sql_datass[0].get("SUM(screen_count)")
# # j = 0
# # for j in range(len(sql_datass)):
# #     # print(i)
# #     b = sql_datass[j]
# #     a = sql_datass[j].get("request_screens")
# #     print(a)
#
# if len(sql_datass) == len(datass):
#     i = 0
#     for i in range(len(datass)):
#      # print(i)
#      b = datass[i]
#      a = datass[i].get("validScreenCount")
#      c =  sql_datass[i].get("request_screens")
#      if  a == c:
#          print("成功了")
#      else:
#          print("失败")
# else:
#     print("数据不对等")