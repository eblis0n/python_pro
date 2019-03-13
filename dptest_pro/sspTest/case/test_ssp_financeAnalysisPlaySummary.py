# encoding=utf-8
import unittest
import utils.interface as utilsInterface
import constants.interfaceName as interfaceName
import  constants.parameter as parameter
from constants.yunproInterface import interface_58 as  interface
import pymysql
import os
import configparser  as cparser


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

doc_path = conf.get("excel", "doc_path")   # 读取配置文件上的Excel表的路径


#参数化
media_provider_id = parameter.quantity_data.get("media_provider_id")
create_time = parameter.quantity_data.get("create_time")
transaction = parameter.quantity_data.get("transaction")
startDate = parameter.quantity_data.get("startDate")
endDate = parameter.quantity_data.get("endDate")

# 定义字段来源
sspFinanceAnalysisPlaySummary = interfaceName.sspFinanceAnalysisPlaySummary
analysisPlaySummary_data = parameter.analysisPlaySummary_data
set_dp_interface = utilsInterface.set_dp_interface


class test_analysis_play_summary (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        # 接口查询
        # cls.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlaySummary,data = analysisPlaySummary_data)

        print("queryentry_ssp_statisdaily接口测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        cls.pymysqlconn.close()

    def test_requestScreenCount(self):
        print("开始测试test_screenCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlaySummary,data = analysisPlaySummary_data)
        inf_requestScreenCount =  self.res_date['data'].get("requestScreenCount")
        # 执行SQL查询
        # self.sql_screenCount = get_media_screenCount(2028, '2019-02-14',conn = self.pymysqlconn )
        sql = "SELECT sum(DISTINCT request_screens) AS requestScreens FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date BETWEEN '{1}' AND '{2}' ;".format(media_provider_id, startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_screens=self.pymysqlcursor.fetchall()
        sql_requestScreenCount = request_screens[0].get("requestScreens")
        # print(sql_requestScreenCount)
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_requestScreenCount,sql_requestScreenCount))
        self.assertEquals(inf_requestScreenCount, sql_requestScreenCount,"test_requestScreenCount数据对不上" )


    def test_validScreenCount(self):
        print("开始测试test_validscreencount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlaySummary,data = analysisPlaySummary_data)
        inf_validscreencount =  self.res_date['data'].get("validScreenCount")

        # 执行SQL查询

        sql = "SELECT  play_screens  FROM ssp_play_summary WHERE ssp_id = '{0}' AND transaction_date ='{1}' ".format(media_provider_id, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_screens=self.pymysqlcursor.fetchall()
        slq_validScreenCount =  play_screens[0].get("play_screens")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_validscreencount, slq_validScreenCount))
        self.assertEquals(inf_validscreencount, slq_validScreenCount, "数据对不上" )

    def test_requestCount(self):
        print("开始测试test_requestCount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlaySummary,data = analysisPlaySummary_data)
        inf_requestCount =  self.res_date['data'].get("requestCount")

        # 执行SQL查询
        sql = "SELECT request_times FROM ssp_play_summary WHERE ssp_id = '{0}' AND transaction_date ='{1}' ;".format(media_provider_id, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_times=self.pymysqlcursor.fetchall()
        slq_request_times =  request_times[0].get("request_times")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_requestCount, slq_request_times))
        self.assertEquals(inf_requestCount, slq_request_times, "数据对不上" )

    def test_materialPlayCount(self):
        print("开始测试test_materialPlayCount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlaySummary,data = analysisPlaySummary_data)
        inf_materialPlayCount =  self.res_date['data'].get("materialPlayCount")

        # 执行SQL查询
        sql = "SELECT sum(play_times) AS playTimes FROM ssp_play_summary WHERE ssp_id = '{0}' AND transaction_date BETWEEN '{1}'AND '{2}' ".format(media_provider_id, startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_times=self.pymysqlcursor.fetchall()
        slq_play_times =  play_times[0].get("playTimes")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_materialPlayCount, slq_play_times))
        self.assertEquals(inf_materialPlayCount, slq_play_times, "test_materialPlayCount数据对不上" )





if __name__ == "__main__":
    unittest.main()