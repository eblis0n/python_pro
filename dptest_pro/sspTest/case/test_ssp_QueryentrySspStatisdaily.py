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
queryentrySspStatisdaily = interfaceName.queryentrySspStatisdaily
sspStatisdaily_data = parameter.sspStatisdaily_data
set_dp_interface = utilsInterface.set_dp_interface

class test_queryentry_ssp_statisdaily (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        print("queryentry_ssp_statisdaily接口测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        cls.pymysqlconn.close()

    def test_dataLen(self):
        print("开始测试test_dataLen")
        u'''比对screenCount字段与数据库是否一致'''
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspStatisdaily,data = sspStatisdaily_data)
        dataLen =  self.res_date['data']
        # print(len(dataLen))
        # 执行SQL查询
        # self.sql_screenCount = get_media_screenCount(2028, '2019-02-14',conn = self.pymysqlconn )
        sql = "SELECT transaction_date,request_screens,play_times,play_duration FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'	AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        sql_dataLen=self.pymysqlcursor.fetchall()
        # print(len(sql_dataLen))
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(len(dataLen),len(sql_dataLen)))
        self.assertEqual(len(dataLen), len(sql_dataLen),"test_dataLen,数据对不上" )

    @skip_dependon(depend="test_dataLen")
    def test_validScreenCount(self):
        print("开始测试test_validScreenCount")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspStatisdaily,data = sspStatisdaily_data)
        inf_validScreenCount =  self.res_date['data']

        # 执行SQL查询
        sql = "SELECT transaction_date,play_screens,play_times,play_duration FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'	AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_screens=self.pymysqlcursor.fetchall()
        i = 0
        print("屏数量比对")
        for i in range(len(inf_validScreenCount)):
            statisDate = inf_validScreenCount[i].get("statisDate")
            validScreenCount = inf_validScreenCount[i].get("validScreenCount")
            sql_play_screens = play_screens[i].get("play_screens")

            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisDate, validScreenCount,sql_play_screens))
        self.assertEqual(validScreenCount,sql_play_screens,"test_validScreenCount,数据对不上" )


    @skip_dependon(depend="test_dataLen")
    def test_playTimes(self):
        print("开始测试test_playTimes")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspStatisdaily,data = sspStatisdaily_data)
        inf_playTimes =  self.res_date['data']

        # 执行SQL查询
        sql = "SELECT transaction_date,request_screens,play_times,play_duration FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'	AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_times=self.pymysqlcursor.fetchall()
        i = 0
        print("播放次数比对")
        for i in range(len(inf_playTimes)):
            statisDate = inf_playTimes[i].get("statisDate")
            playTimes = inf_playTimes[i].get("playTimes")
            sql_play_times = play_times[i].get("play_times")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisDate, playTimes,sql_play_times))
        self.assertEqual(playTimes,sql_play_times,"test_playTimes,数据对不上" )

    @skip_dependon(depend="test_dataLen")
    def test_playDuration(self):
        print("开始测试test_playDuration")
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspStatisdaily,data = sspStatisdaily_data)
        inf_playDuration =  self.res_date['data']
        # print(len(inf_playDuration))

        # 执行SQL查询
        sql = "SELECT transaction_date,request_screens,play_times,play_duration FROM	ssp_play_summary WHERE (transaction_date BETWEEN '{0}'AND '{1}') AND ssp_id = {2};".format(startDate, endDate, media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_duration=self.pymysqlcursor.fetchall()
        # print(len(sql_playDuration))
        i = 0
        print("播放时长对比")
        for i in range(len(inf_playDuration)):
            statisDate = inf_playDuration[i].get("statisDate")
            playDuration = inf_playDuration[i].get("playDuration")
            sql_play_duration = play_duration[i].get("play_duration")
            print('日期: {0}, 接口返回结果：{1} , 数据库查询结果：{2}' .format(statisDate, playDuration,sql_play_duration))
        self.assertEqual(playDuration,sql_play_duration,"test_playDuration,数据对不上" )





if __name__ == "__main__":
    unittest.main()