# encoding=utf-8

import unittest
import utils.interface as utilsInterface
from  utils.methods import skip_dependon as skip_dependon
import constants.interfaceName as interfaceName
import  constants.parameter as parameter
from constants.yunproInterface import interface_58 as  interface
import pymysql
import os
import configparser  as cparser
from functools import wraps

# ===============读取配置文件============== #
base_dr = str(os.path.dirname(os.path.dirname(__file__)))
bae_idr = base_dr.replace('\\', '/')


# 配置文件的地址
file_path = bae_idr + "/config.ini"

conf = cparser.ConfigParser()

conf.read(file_path)



# 读取配置文件上的
mysqlHost = conf.get("mysqlconf", "host")   # 读取配置文件上数据库主机号
mysqlPort = conf.get("mysqlconf", "port")    # 读取配置文件数据库的端口号
mysqlUser = conf.get("mysqlconf", "user")    # 读取配置文件数据库的账号
mysqlPassword = conf.get("mysqlconf", "password")   # 读取配置文件数据库的密码
mysqlName = conf.get("mysqlconf", "db_name")   # 读取配置文件数据库的名字


#参数化
media_provider_id = parameter.quantity_data.get("media_provider_id")
create_time = parameter.quantity_data.get("create_time")
transaction = parameter.quantity_data.get("transaction")
startDate = parameter.quantity_data.get("startDate")
endDate = parameter.quantity_data.get("endDate")

# 定义字段来源
sspFinanceAnalysisPlayList = interfaceName.sspFinanceAnalysisPlayList
FinanceAnalysisPlayList_data = parameter.FinanceAnalysisPlayList_data
set_dp_interface = utilsInterface.set_dp_interface

class test_queryentry_ssp_analysisPlayList_curvegraph (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        print("queryentry_ssp_analysisPlayList(播放趋势图)接口测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        cls.pymysqlconn.close()

    def test_analysisPlayListLen(self):
        print("开始测试test_analysisPlayListLen")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        inf_analysisplaylistlen = self.res_date['data']
        # print(len(inf_analysisplaylistlen))
        # 执行SQL查询
        sql = "SELECT * FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        sql_dataLen=self.pymysqlcursor.fetchall()
        # print(len(sql_dataLen))
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(len(inf_analysisplaylistlen),len(sql_dataLen)))
        self.assertEqual(len(inf_analysisplaylistlen), len(sql_dataLen),"test_dataLen,数据对不上" )

    @skip_dependon(depend="test_analysisPlayListLen")
    def test_playListValidScreenCount(self):
        print("开始测试test_playListValidScreenCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        validScreenCount =  self.res_date['data']

        # 执行SQL查询
        sql = "SELECT transaction_date,play_screens FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_screens=self.pymysqlcursor.fetchall()
        i = 0
        print("展现广告屏数比对")
        for i in range(len(validScreenCount)):
            statisGroup = validScreenCount[i].get("statisGroup")
            inf_validScreenCount = validScreenCount[i].get("validScreenCount")
            sql_play_screens = play_screens[i].get("play_screens")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisGroup, inf_validScreenCount,sql_play_screens))
        self.assertEqual(inf_validScreenCount,sql_play_screens,"test_validScreenCount,数据对不上" )


    @skip_dependon(depend="test_analysisPlayListLen")
    def test_playListplayTimes(self):
        print("开始测试test_playListplayTimes")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        materialPlayCount =  self.res_date['data']

        # 执行SQL查询
        sql = "SELECT transaction_date,play_times FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_times=self.pymysqlcursor.fetchall()
        i = 0
        print("有效播放次数比对")
        for i in range(len(materialPlayCount)):
            statisGroup = materialPlayCount[i].get("statisGroup")
            inf_materialPlayCount = materialPlayCount[i].get("materialPlayCount")
            sql_play_times = play_times[i].get("play_times")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisGroup, inf_materialPlayCount,sql_play_times))
        self.assertEqual(inf_materialPlayCount,sql_play_times,"test_playListplayTimes,数据对不上" )

    @skip_dependon(depend="test_analysisPlayListLen")
    def test_playListrequestScreenCount(self):
        print("开始测试test_playListrequestScreenCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        requestScreenCount =  self.res_date['data']
        # print(len(inf_playDuration))

        # 执行SQL查询
        sql = "SELECT transaction_date,request_screens FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_screens=self.pymysqlcursor.fetchall()
        # print(len(sql_playDuration))
        i = 0
        print("请求屏数对比")
        for i in range(len(requestScreenCount)):
            statisGroup = requestScreenCount[i].get("statisGroup")
            inf_requestScreenCount = requestScreenCount[i].get("requestScreenCount")
            sql_request_screens = request_screens[i].get("request_screens")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisGroup, inf_requestScreenCount,sql_request_screens))
        self.assertEqual(inf_requestScreenCount,sql_request_screens,"test_playListrequestScreenCount,数据对不上" )

    @skip_dependon(depend="test_analysisPlayListLen")
    def test_playListerrorScreenCount(self):
        print("开始测试test_playListerrorScreenCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        errorScreenCount =  self.res_date['data']
        # print(len(inf_playDuration))

        # 执行SQL查询
        sql = "SELECT ssu.create_time, (SUM(DISTINCT ssu.screen_count) - SUM(DISTINCT spu.request_screens)) AS errorScreenCounts FROM screen_summary AS ssu LEFT JOIN ssp_play_summary AS spu ON ssu.create_time = spu.transaction_date WHERE	ssu.media_provider_id = {2} AND (ssu.create_time BETWEEN '{0}' AND  '{1}') GROUP BY create_time;".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        sql_errorScreenCounts=self.pymysqlcursor.fetchall()
        # print(sql_errorScreenCounts)
        i = 0
        print("异常屏对比")
        for i in range(len(errorScreenCount)):
            statisGroup = errorScreenCount[i].get("statisGroup")
            inf_errorScreenCount = errorScreenCount[i].get("errorScreenCount")
            sql_errorScreenCount = sql_errorScreenCounts[i].get("errorScreenCounts")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisGroup, inf_errorScreenCount,sql_errorScreenCount))
        self.assertEqual(inf_errorScreenCount,sql_errorScreenCount,"test_playListerrorScreenCount,数据对不上" )

    @skip_dependon(depend="test_analysisPlayListLen")
    def test_playListmaterialFailCount(self):
        print("开始测试test_playListmaterialFailCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        materialFailCount =  self.res_date['data']
        # print(len(inf_playDuration))

        # 执行SQL查询
        sql = "SELECT transaction_date,play_fail_times FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_fail_times=self.pymysqlcursor.fetchall()
        # print(sql_errorScreenCounts)
        i = 0
        print("播放异常对比")
        for i in range(len(materialFailCount)):
            statisGroup = materialFailCount[i].get("statisGroup")
            inf_materialFailCount = materialFailCount[i].get("materialFailCount")
            sql_play_fail_times = play_fail_times[i].get("play_fail_times")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisGroup, inf_materialFailCount,sql_play_fail_times))
        self.assertEqual(inf_materialFailCount,sql_play_fail_times,"test_playListmaterialFailCount,数据对不上" )

    @skip_dependon(depend="test_analysisPlayListLen")
    def test_playListrequestCount(self):
        print("开始测试test_playListrequestCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + sspFinanceAnalysisPlayList,data = FinanceAnalysisPlayList_data)
        requestCount =  self.res_date['data']
        # print(len(inf_playDuration))

        # 执行SQL查询
        sql = "SELECT transaction_date,request_times FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_times=self.pymysqlcursor.fetchall()
        # print(sql_errorScreenCounts)
        i = 0
        print("播放异常对比")
        for i in range(len(requestCount)):
            statisGroup = requestCount[i].get("statisGroup")
            inf_requestCount = requestCount[i].get("requestCount")
            sql_request_times = request_times[i].get("request_times")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisGroup, inf_requestCount,sql_request_times))
        self.assertEqual(inf_requestCount,sql_request_times,"test_playListrequestCount,数据对不上" )







if __name__ == "__main__":
    unittest.main()