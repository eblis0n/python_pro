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

# print(os.path.basename(__file__)) # 读取当前文件名称

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

class test_analysis_totalsummary (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        # 接口查询
        cls.res_date = set_dp_interface(url=planentry_url + totalsummary_address,data = totalsummary_data)

        print("DMP_analysis_totalsummary接口测试开始")

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
        self.assertEquals(inf_totalScreen, sql_screenCount,"test_totalScreen数据对不上" )

    def test_totalRegistScreen(self):
        print("开始测试test_totalRegistScreen")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_totalRegistScreen =  self.res_date['data'].get("totalRegistScreen")
        # 执行SQL查询
        sql = "SELECT SUM(regist_screen_Count) AS totalRegistScreen FROM screen_summary WHERE  create_time = '{0}';".format(create_time)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        regist_screen_Count=self.pymysqlcursor.fetchall()
        sql_registscreenCount = regist_screen_Count[0].get("totalScreen")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_totalRegistScreen,sql_registscreenCount))
        self.assertEquals(inf_totalRegistScreen, sql_registscreenCount,"test_totalRegistScreen数据对不上" )

    def test_totalRequest(self):
        print("开始测试test_totalRequest")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_totalRequest =  self.res_date['data'].get("totalRequest")
        # 执行SQL查询
        sql = "SELECT sum(request_times) AS totalRequest from ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' AND '{1}';".format(startDate,endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_times=self.pymysqlcursor.fetchall()
        sql_requesttimes = request_times[0].get("totalRequest")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(str(inf_totalRequest),str(sql_requesttimes)))
        self.assertEquals(str(inf_totalRequest), str(sql_requesttimes),"test_totalRequest数据对不上" )

    def test_totalMaxPlayDate(self):
        print("开始测试test_totalMaxPlayDate")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_totalMaxPlayDate = self.res_date['data'].get("totalMaxPlayDate")
        # 执行SQL查询
        sql = "SELECT confirm_num,transaction_date FROM dsp_play_summary_2_daily ORDER BY confirm_num DESC;"
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        transaction_date=self.pymysqlcursor.fetchall()
        sql_transaction_date = transaction_date[0].get("transaction_date")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(str(inf_totalMaxPlayDate),str(sql_transaction_date)))
        self.assertEquals(str(inf_totalMaxPlayDate), str(sql_transaction_date),"test_totalMaxPlayDate数据对不上" )

    @skip_dependon(depend="test_totalMaxPlayDate")
    def test_totalMaxPlayTime(self):
        print("开始测试test_totalMaxPlayTime")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_totalMaxPlayTime = self.res_date['data'].get("totalMaxPlayTime")
        # 执行SQL查询
        sql = "SELECT confirm_num,transaction_date FROM dsp_play_summary_2_daily ORDER BY confirm_num DESC;"
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        confirm_num=self.pymysqlcursor.fetchall()
        sql_confirm_num = confirm_num[0].get("confirm_num")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(str(inf_totalMaxPlayTime),str(sql_confirm_num)))
        self.assertEquals(str(inf_totalMaxPlayTime), str(sql_confirm_num),"test_totalMaxPlayTime数据对不上" )




if __name__ == "__main__":
    unittest.main()
