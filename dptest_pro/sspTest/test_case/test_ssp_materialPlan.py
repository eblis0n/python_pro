# encoding=utf-8

import unittest
from utils.methods import set_dp_interface as set_dp_interface
import constants.deploy as deploy
import pymysql
import os
import configparser  as cparser
import openpyxl



#######################从deploy里面读取配置文件内容#################################


mysqlHost = deploy.mysqlHost
mysqlPort = deploy.mysqlPort
mysqlUser = deploy.mysqlUser
mysqlPassword = deploy.mysqlPassword
mysqlName = deploy.mysqlName1
wbook = deploy.wbook
table2 = deploy.table2


############################### 配置文件的地址######################
#
# base_dr = str(os.path.dirname(os.path.dirname(__file__)))
# bae_idr = base_dr.replace('\\', '/')
#
# file_path = bae_idr + "/config.ini"
#
# conf = cparser.ConfigParser()
#
# conf.read(file_path)
#
#
# #######################读取配置文件上###################################
# mysqlHost = conf.get("mysqlconf", "host")   # 读取配置文件上数据库主机号
# mysqlPort = conf.get("mysqlconf", "port")    # 读取配置文件数据库的端口号
# mysqlUser = conf.get("mysqlconf", "user")    # 读取配置文件数据库的账号
# mysqlPassword = conf.get("mysqlconf", "password")   # 读取配置文件数据库的密码
# mysqlName = conf.get("mysqlconf", "db_name1")   # 读取配置文件数据库的名字
# wbook = openpyxl.load_workbook(conf.get("excel", "excel_path")) # 读取配置文件的Excel文档地址
# table2 = wbook[conf.get("excel", "table")] # 读取配置文件的Excel文档所使用的用例table



#######################根据Excel读取本接口对应的key#################################
begtest=[]
endtest=[]

for i in range(1,int(table2.max_column)):
    if table2["C"+str(i)].value=="go":
        begtest.append(i)

    if table2["L"+str(i)].value=="end":
        endtest.append(i)

for j in range(1, len(begtest)):
    for k in range(2, int(begtest[j] + 1)):
        # print("excel:" + table2["C" + str(k)].value)
        if os.path.basename(__file__)[0:-3] == table2["D" + str(k)].value:

            # 接口参数
            admanage_url = table2["E" + str(k)].value # 接口路径
            admanageMaterialV2QueryPlan = table2["F" + str(k)].value # 接口地址
            sspPlan_data = table2["G" + str(k)].value # 请求参数

            # 数据库条件
            media_provider_id = table2["H" + str(k)].value
            # create_time = table2["I" + str(k)].value
            # transaction_date = table2["H" + str(k)].value
            startDate = table2["I" + str(k)].value
            endDate = table2["J" + str(k)].value
            limits = table2["k" + str(k)].value
            break
########################################################

# 对应的接口：/admanage/material/v2/query/plan
class test_material_plan (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pymysqlconn = pymysql.connect(host=mysqlHost, port=int(mysqlPort), user=mysqlUser, passwd=mysqlPassword, db=mysqlName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
        cls.pymysqlcursor = cls.pymysqlconn.cursor()

        # 接口
        # cls.res_date = set_dp_interface(url=admanage_url + admanageMaterialV2QueryPlan, data=sspPlan_data)

        print("test_material_plan接口测试开始\n")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
        cls.pymysqlconn.close()

    def test_planLen(self):
        print("开始测试test_planLen")
        # 执行接口查询
        self.res_date = set_dp_interface(url=admanage_url + admanageMaterialV2QueryPlan, data=sspPlan_data)
        # print("接口返回结果:" + str(self.res_date))
        planLen =  self.res_date['data']

        # 执行SQL查询
        sql = "	SELECT * FROM material m LEFT JOIN material_review mr ON m.id = mr.id WHERE mr.media_provider_id = {0} GROUP BY order_id;".format( media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        sql_planLen=self.pymysqlcursor.fetchall()
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(len(planLen),len(sql_planLen)))
        self.assertEqual(len(planLen), len(sql_planLen),"test_planLen,数据对不上" )






if __name__ == "__main__":
    unittest.main()