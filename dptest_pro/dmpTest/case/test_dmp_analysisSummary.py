# encoding=utf-8
import unittest
# import utils.interface as utilsInterface
from utils.interface import set_dp_interface as set_dp_interface
import constants.interfaceName as interfaceName
import  constants.parameter as parameter
from constants.yunproInterface import interface_58 as  interface
import pymysql
import os
import configparser  as cparser
import openpyxl
from  utils.methods import skip_dependon as skip_dependon




# ===============读取配置文件============== #
base_dr = str(os.path.dirname(os.path.dirname(__file__)))
bae_idr = base_dr.replace('\\', '/')

# 配置文件的地址
file_path = bae_idr + "/config.ini"

conf = cparser.ConfigParser()

conf.read(file_path)

# print(file_path)

# 读取配置文件上的
mysqlHost = conf.get("mysqlconf", "host")   # 读取配置文件上数据库主机号
mysqlPort = conf.get("mysqlconf", "port")    # 读取配置文件数据库的端口号
mysqlUser = conf.get("mysqlconf", "user")    # 读取配置文件数据库的账号
mysqlPassword = conf.get("mysqlconf", "password")   # 读取配置文件数据库的密码
mysqlName = conf.get("mysqlconf", "db_name")   # 读取配置文件数据库的名字

## 读取Excel的用例

wbook=openpyxl.load_workbook(bae_idr + "/testexcel/dmptest3.xlsx")
table2=wbook['Test_Case2']
# print(table2.title)
#######################根据Excel读取本接口对应的key#################################
begtest=[]
endtest=[]

for i in range(1,int(table2.max_column)):
    if table2["A"+str(i)].value=="go":
        begtest.append(i)

    if table2["L"+str(i)].value=="end":
        endtest.append(i)

for j in range(1, len(begtest)):
    for k in range(2, int(begtest[j] + 1)):
        # print("excel:" + table2["C" + str(k)].value)
        if os.path.basename(__file__)[0:-3] == table2["C" + str(k)].value:
            # print(str(k))
            # vv = str(k)

            # 接口参数
            planentry_url = table2["D" + str(k)].value
            totalsummary_address = table2["E" + str(k)].value
            # totalsummary_address = table2["E2"].value
            totalsummary_data = table2["F" + str(k)].value

            # 数据库条件
            create_time = table2["I" + str(k)].value
            startDate = table2["J" + str(k)].value
            endDate = table2["K" + str(k)].value
            break
########################################################


class test_analysis_summary (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        # 接口查询
        cls.res_date = set_dp_interface(url=planentry_url + totalsummary_address,data = totalsummary_data)

        print("dmp_analysis_summary接口测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        cls.pymysqlconn.close()

    def test_totalScreen(self):
        print("开始测试test_totalScreen")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_totalScreen =  self.res_date['data'].get("totalScreen")
        # 执行SQL查询
        sql = "SELECT SUM(screen_count) AS totalScreen FROM screen_summary WHERE  create_time = '{0}';".format(create_time)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        screen_count=self.pymysqlcursor.fetchall()
        sql_screenCount = screen_count[0].get("totalScreen")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_totalScreen,sql_screenCount))
        self.assertEquals(inf_totalScreen, sql_screenCount,"test_screenCount数据对不上" )




if __name__ == "__main__":
    unittest.main()
