# encoding=utf-8
import unittest
# import utils.interface as utilsInterface
from utils.methods import set_dp_interface as set_dp_interface
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
print(base_dr)
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

            # 接口参数
            planentry_url = table2["D" + str(k)].value
            totalsummary_address = table2["E" + str(k)].value
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

    # 请求屏数
    def test_requestScreenCount(self):
        print("开始测试test_requestScreenCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_requestScreenCount =  self.res_date['data'].get("requestScreenCount")
        # 执行SQL查询
        sql = "SELECT SUM(request_screens) AS request_screens FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(startDate,endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        request_screens=self.pymysqlcursor.fetchall()
        sql_request_screens = request_screens[0].get("request_screens")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(str(inf_requestScreenCount),str(sql_request_screens)))
        self.assertEquals(str(inf_requestScreenCount), str(sql_request_screens),"test_requestScreenCount数据对不上" )

    # 初始化屏数
    def test_initScreenCount(self):
        print("开始测试test_initScreenCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_initScreenCount =  self.res_date['data'].get("initScreenCount")
        # 执行SQL查询
        sql = "SELECT SUM(init_screens) AS init_screens FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(startDate,endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        init_screens=self.pymysqlcursor.fetchall()
        sql_init_screens = init_screens[0].get("init_screens")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(str(inf_initScreenCount),str(sql_init_screens)))
        self.assertEquals(str(inf_initScreenCount), str(sql_init_screens),"test_initScreenCount数据对不上" )

    # 播放屏数
    def test_validScreenCount(self):
        print("开始测试test_validScreenCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_validScreenCount = self.res_date['data'].get("validScreenCount")
        # 执行SQL查询
        sql = "SELECT SUM(play_screens) AS play_screens FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_screens = self.pymysqlcursor.fetchall()
        sql_play_screens = play_screens[0].get("play_screens")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_validScreenCount), str(sql_play_screens)))
        self.assertEquals(str(inf_validScreenCount), str(sql_play_screens), "test_validScreenCount数据对不上")
    # 有播放广告的媒体商数量
    def test_sspCount(self):
        print("开始测试test_sspCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_sspCount = self.res_date['data'].get("sspCount")
        # 执行SQL查询
        sql = "SELECT SUM(ssp_count) AS ssp_count FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        ssp_count = self.pymysqlcursor.fetchall()
        sql_ssp_count = ssp_count[0].get("ssp_count")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_sspCount), str(sql_ssp_count)))
        self.assertEquals(str(inf_sspCount), str(sql_ssp_count), "test_sspCount数据对不上")

    # 有播放广告的广告主数量
    def test_dspCount(self):
        print("开始测试test_dspCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_dspCount = self.res_date['data'].get("dspCount")
        # 执行SQL查询
        sql = "SELECT SUM(dsp_count) AS dsp_count FROM dsp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        dsp_count = self.pymysqlcursor.fetchall()
        sql_dsp_count = dsp_count[0].get("dsp_count")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_dspCount), str(sql_dsp_count)))
        self.assertEquals(str(inf_dspCount), str(sql_dsp_count), "test_dspCount数据对不上")

    # 素材总数
    def test_materialCount(self):
        print("开始测试test_materialCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_materialCount = self.res_date['data'].get("materialCount")
        # 执行SQL查询
        sql = "SELECT SUM(material_count)AS material_count FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        material_count = self.pymysqlcursor.fetchall()
        sql_material_count = material_count[0].get("material_count")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_materialCount), str(sql_material_count)))
        self.assertEquals(str(inf_materialCount), str(sql_material_count), "test_materialCoun数据对不上")

    # 有播放的素材数量
    def test_playMaterialCount(self):
        print("开始测试test_playMaterialCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_playMaterialCount = self.res_date['data'].get("playMaterialCount")
        # 执行SQL查询
        sql = "SELECT SUM(play_material_count)AS play_material_count FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        play_material_count = self.pymysqlcursor.fetchall()
        sql_play_material_count = play_material_count[0].get("play_material_count")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_playMaterialCount), str(sql_play_material_count)))
        self.assertEquals(str(inf_playMaterialCount), str(sql_play_material_count), "test_playMaterialCount数据对不上")

    # 有播放广告的广告数量
    def test_adCount(self):
        print("开始测试test_adCount")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_adCount = self.res_date['data'].get("adCount")
        # 执行SQL查询
        sql = "SELECT SUM(ad_count)AS ad_count FROM dsp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        ad_count = self.pymysqlcursor.fetchall()
        sql_ad_count = ad_count[0].get("ad_count")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_adCount), str(sql_ad_count)))
        self.assertEquals(str(inf_adCount), str(sql_ad_count), "test_adCount数据对不上")

    # 单屏平均播放次数
    def test_avgPlayTime(self):
        print("开始测试test_avgPlayTime")
        # 执行接口查询
        # self.res_date = set_dp_interface(url=interface.get("queryentry_url") + queryentrySspSummary,data = sspSummary_data)
        print("接口返回结果:" + str(self.res_date))
        inf_avgPlayTime = self.res_date['data'].get("avgPlayTime")
        # 执行SQL查询
        sql = "SELECT SUM(play_times) / SUM(play_screens) AS avg_Play_Time FROM ssp_play_summary_2_daily WHERE transaction_date BETWEEN '{0}' and '{1}';".format(
            startDate, endDate)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        avg_Play_Time = self.pymysqlcursor.fetchall()
        sql_avg_Play_Time = avg_Play_Time[0].get("avg_Play_Time")
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}'.format(str(inf_avgPlayTime), str(sql_avg_Play_Time)))
        self.assertEquals(str(inf_avgPlayTime), str(sql_avg_Play_Time), "test_avgPlayTime数据对不上")


if __name__ == "__main__":
    unittest.main()
