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

#参数化
#参数化
media_provider_id = parameter.quantity_data.get("media_provider_id")
create_time = parameter.quantity_data.get("create_time")
transaction_date = parameter.quantity_data.get("transaction_date")
startDate = parameter.quantity_data.get("startDate")
endDate = parameter.quantity_data.get("endDate")


# 定义字段来源
queryentrySspSummary = interfaceName.queryentrySspSummary
sspSummary_data = parameter.sspSummary_data
set_dp_interface = utilsInterface.set_dp_interface

class test_queryentry_ssp_summary (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        # 接口
        # cls.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)

        print("queryentry_ssp_summary接口测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        cls.pymysqlconn.close()


    def test_screenCount(self):
        print("开始测试test_screenCount")
        u'''比对screenCount字段与数据库是否一致'''
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_screencount =  self.res_date['data'].get("screenCount")
        # 执行SQL查询
        sql = "SELECT SUM(screen_count) FROM screen_summary WHERE media_provider_id = {0} AND create_time = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        screen_count=self.pymysqlcursor.fetchall()
        sql_screenCount = screen_count[0].get("SUM(screen_count)")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_screencount,sql_screenCount))
        self.assertEquals(inf_screencount, sql_screenCount,"test_screenCount数据对不上" )


    def test_validscreencount(self):
        print("开始测试test_validscreencount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_validscreencount =  self.res_date['data'].get("validScreenCount")

        # 执行SQL查询
        sql = "SELECT SUM(request_screens) FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_screens=self.pymysqlcursor.fetchall()
        slq_validScreenCount =  request_screens[0].get("SUM(request_screens)")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_validscreencount, slq_validScreenCount))
        self.assertEquals(inf_validscreencount, slq_validScreenCount, "test_validscreencount数据对不上" )

    def test_materialCount(self):
        print("开始测试test_materialCount")
        u'''比对validscreencount字段与数据库是否一致'''
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_materialCount =  self.res_date['data'].get("materialCount")
        # print(materialCount)

        # 执行SQL查询
        sql = "SELECT SUM(material_count) FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        material_count=self.pymysqlcursor.fetchall()
        slq_materialCount =  material_count[0].get("SUM(material_count)")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_materialCount, slq_materialCount))
        self.assertEquals(inf_materialCount, slq_materialCount, "test_materialCount数据对不上" )

    def test_materialPlayCount(self):
        print("开始测试test_materialPlayCount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_materialPlayCount =  self.res_date['data'].get("materialPlayCount")
        # print(materialPlayCount)

        # 执行SQL查询
        sql = "SELECT SUM(play_times) FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_times=self.pymysqlcursor.fetchall()
        sql_play_times = play_times[0].get("SUM(play_times)")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_materialPlayCount, sql_play_times))
        self.assertEquals(inf_materialPlayCount, sql_play_times, "test_materialPlayCount数据对不上" )

    def test_materialFailCount(self):
        print("开始测试test_materialFailCount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_materialFailCount =  self.res_date['data'].get("materialFailCount")
        # print(materialFailCount)

        # 执行SQL查询
        sql = "SELECT play_fail_times FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_fail_times=self.pymysqlcursor.fetchall()
        sql_play_fail_times = play_fail_times[0].get("play_fail_times")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：%s , 数据库查询结果：%d' %(inf_materialFailCount, sql_play_fail_times))
        self.assertEquals(inf_materialFailCount, sql_play_fail_times, "test_materialFailCount数据对不上" )

    def test_materialPlayDuration(self):
        print("开始测试test_materialPlayDuration")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_materialPlayDuration =  self.res_date['data'].get("materialPlayDuration")
        # print(materialFailCount)

        # 执行SQL查询
        sql = "SELECT play_duration FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_duration=self.pymysqlcursor.fetchall()
        sql_play_duration = play_duration[0].get("play_duration")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_materialPlayDuration, sql_play_duration))
        self.assertEquals(inf_materialPlayDuration, sql_play_duration, "test_materialPlayDuration数据对不上" )

    def test_errorScreenCount(self):
        print("测试开始test_errorScreenCount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_errorScreenCount =  self.res_date['data'].get("errorScreenCount")
        # print(materialFailCount)

        # 执行SQL查询
        sql = "SELECT (SUM(ssu.screen_count) - SUM(request_screens)) AS errorScreenCount FROM	screen_summary AS ssu LEFT JOIN ssp_play_summary AS spu ON ssu.create_time = spu.transaction_date WHERE	ssu.media_provider_id = {0} AND ssu.create_time = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        errorScreenCount=self.pymysqlcursor.fetchall()
        sql_errorScreenCount = errorScreenCount[0].get("errorScreenCount")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_errorScreenCount, sql_errorScreenCount))
        self.assertEquals(inf_errorScreenCount, sql_errorScreenCount, "test_errorScreenCount数据对不上" )

    def test_income(self):
        print("开始测试test_errorScreenCount")
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        inf_income =  self.res_date['data'].get("income")
        # print(materialFailCount)

        # 执行SQL查询
        sql = "SELECT amount FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}';".format(media_provider_id, transaction_date)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        amount=self.pymysqlcursor.fetchall()
        sql_amount = amount[0].get("amount")

        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(inf_income, sql_amount))
        self.assertEquals(str(sql_amount), str(inf_income), "test_income数据对不上" )



if __name__ == "__main__":
    unittest.main()