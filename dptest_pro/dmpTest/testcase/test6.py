# encoding=utf-8
import operator
from constants.yunproInterface import interface_58 as  interface
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


# 定义字段来源
financeAnalysisDspList = interfaceName.financeAnalysisDspList
# dsplist_data = parameter.dsplist_data
set_dp_interface = utilsInterface.set_dp_interface
finance_url = interface.get("finance_url")

dsplist_data = {"startDate":"2019-03-26","endDate":"2019-03-26","groupBy":["areaCode","area"],"areaLevel":1,"pageIndex":1,"pageSize":1000,"createId":100046,"relationAccountlist":[100,101,102,103,104,105,106,1009,1016,1306,1310,1311,1312,1317,1318,2013,2028,2043,2056,2067,2092,2093,2094,2095,2096,2097,2098,2099,3000,3001,3017,3021,3022,3023,3024,3025,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3085]}

res_date = set_dp_interface(url=finance_url + financeAnalysisDspList,data=dsplist_data)