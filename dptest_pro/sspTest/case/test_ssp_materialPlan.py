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
mysqlName = conf.get("mysqlconf", "db_name1")   # 读取配置文件数据库的名字

doc_path = conf.get("excel", "doc_path")   # 读取配置文件上的Excel表的路径

#参数化
media_provider_id = parameter.quantity_data.get("media_provider_id")


# 定义字段来源
admanageMaterialV2QueryPlan = interfaceName.admanageMaterialV2QueryPlan
sspPlan_data = parameter.sspPlan_data
set_dp_interface = utilsInterface.set_dp_interface


class test_material_plan (unittest.TestCase):
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

    def test_planLen(self):
        print("开始测试test_dataLen")
        u'''比对screenCount字段与数据库是否一致'''
        # 执行接口查询
        self.res_date = set_dp_interface(url=interface.get("admanage_url") + admanageMaterialV2QueryPlan,data = sspPlan_data)
        planLen =  self.res_date['data']
        # print(len(dataLen))

        # 执行SQL查询
        sql = "	SELECT * FROM material m LEFT JOIN material_review mr ON m.id = mr.id WHERE mr.media_provider_id = {0};".format( media_provider_id)
        print("数据库查询使用语句：" + sql)
        self.pymysqlcursor.execute(sql)
        sql_planLen=self.pymysqlcursor.fetchall()
        # print(len(sql_dataLen))
        # 判断 接口数据与数据库查询结果
        print('接口返回结果：{0} , 数据库查询结果：{1}' .format(len(planLen),len(sql_planLen)))
        self.assertEqual(len(planLen), len(sql_planLen),"test_dataLen,数据对不上" )






if __name__ == "__main__":
    unittest.main()