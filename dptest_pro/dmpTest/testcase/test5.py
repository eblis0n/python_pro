# encoding=utf-8
import operator
from constants.yunproInterface import interface_online as  interface
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
mysqlHost = conf.get("onlinemysqlconf", "host")   # 读取配置文件上数据库主机号
mysqlPort = conf.get("onlinemysqlconf", "port")    # 读取配置文件数据库的端口号
mysqlUser = conf.get("onlinemysqlconf", "user")    # 读取配置文件数据库的账号
mysqlPassword = conf.get("onlinemysqlconf", "password")   # 读取配置文件数据库的密码
mysqlName = conf.get("onlinemysqlconf", "db_name")   # 读取配置文件数据库的名字

# 定义字段来源
financeAnalysisDspList = interfaceName.financeAnalysisDspList
dsplist_data = parameter.dsplist_data
set_dp_interface = utilsInterface.set_dp_interface
finance_url = interface.get("finance_url")


res_date = set_dp_interface(url=finance_url + financeAnalysisDspList,data = dsplist_data)

int_aa = res_date['data']
# inf_totalRegistScreen =  res_date['data'].get("totalRegistScreen")

# bb = json.dumps(res_date)
# inp_dict = json.loads(bb) # 根据字符串书写格式，将字符串自动转换成 字典类型
# print(inp_dict)

# 读取配置文件 # 连接数据库




pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
pymysqlcursor = pymysqlconn.cursor()
# 执行SQL查询
sql = "SELECT dsp_id,SUM(confirm_num) as confirm_num FROM dsp_play_summary WHERE  transaction_date BETWEEN '2019-03-28' and '2019-03-28' GROUP BY dsp_id"
pymysqlcursor.execute(sql)
aa = pymysqlcursor.fetchall()
# sql_play_time_len = play_time_len[0].get("play_time_len")
print(str(aa))
# print(aa[0])
ss = sorted(aa[0])
# print(ss[1])
rr = aa[0].get(ss[0])
# print(rr)
# vv = 'customerId'
# bbb = 'playTime'
#
# if len(aa) == len(int_aa):
#     # print(len(aa),len(int_aa))
#     for i in range(0,len(aa)):
#         # print(aa[i])
#         # print(int_aa[i].get(vv))
#         ss = sorted(aa[i])
#         for j in range (0,len(ss)):
#             # print(aa[i].get(ss[j]))
#             if int_aa[i].get(vv) == aa[i].get(ss[j]):
#                 print(aa[i].get(ss[j]))
#                 if int_aa[i].get(bbb) == aa[i].get(ss[j]):
#                     print("数据对了")


if len(aa) == len(int_aa):
    for i in range(0, len(aa)):
        if str(res_date['data'][i].get('customerId')) == str(aa[i].get('dsp_id')):
            print("第一波通过"+ str(res_date['data'][i].get('customerId')),str(aa[i].get('dsp_id')))
            if str(res_date['data'][i].get('playTime')) == str(aa[i].get('confirm_num')):
                print("good,数据匹配"+ str(res_date['data'][i].get('playTime')), str(aa[i].get('confirm_num')))
            else:
                print("错了" + str(res_date['data'][i].get('playTime')), str(aa[i].get('confirm_num')))

# print(rr)
# str1 = 'hello'
# str2 = None
# print(operator.eq(str1, str2))
# print(str1.__eq__(str2))


