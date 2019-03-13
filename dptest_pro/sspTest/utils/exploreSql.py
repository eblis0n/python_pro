# -*- coding: utf-8 -*-
import pymysql
import requests
import json
import os

def conn(host,port,user,passwd,dbName):
    """

    :param host:主机地址，如：192.168.1.51
    :param port: 端口号，如：8070
    :param user: 数据库账号，如：root
    :param passwd: 数据库密码，如：123
    :param db: 数据库名，如：ad_account
    :return: 返回文件描述符
    """
    conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, db=dbName,
                           charset="utf8",cursorclass = pymysql.cursors.DictCursor)
    return conn


def get_media_validScreenCount(ssp_id, transaction_date, conn):
    """

    :param mediaProviderid:填写需要筛选的媒体商编号 ,如;2013
    :param status: 需要筛选的屏状态  ,如：1
    :param conn: 数据库连接后的描述符，如：conn
    :return:获取数据库中所有的screenId，并存放到列表中
    """

    db = conn.cursor()
    # sql = "select screen_id from screen where media_provider_id = {0} and status = {1}".format(mediaProviderid, status)
    sql = "SELECT SUM(request_screens) FROM ssp_play_summary WHERE ssp_id = {0} AND transaction_date = '{1}'".format(ssp_id, transaction_date)
    print(sql)
    # 执行sql语句
    db.execute(sql)
    requestscreens = db.fetchall()
    print(requestscreens)
    conn.close()
    db.close()
    return requestscreens

def get_media_screenCount(media_provider_id, create_time, conn):
    """

    :param mediaProviderid:填写需要筛选的媒体商编号 ,如;2013
    :param status: 需要筛选的屏状态  ,如：1
    :param conn: 数据库连接后的描述符，如：conn
    :return:获取数据库中所有的screenId，并存放到列表中
    """

    db = conn.cursor()
    # sql = "select screen_id from screen where media_provider_id = {0} and status = {1}".format(mediaProviderid, status)
    sql = "SELECT SUM(screen_count) FROM screen_summary WHERE media_provider_id = {0} AND create_time = '{1}'".format(media_provider_id, create_time)
    # print(sql)
    # 执行sql语句
    db.execute(sql)
    screencount = db.fetchall()
    # print(screencount)
    conn.close()
    db.close()
    return screencount


connect = conn(host='192.168.1.58', port=3306, user='root', passwd='dianping123', dbName='trans_db')  # 连接数据库
# connect = conn(host=mysqlHost, port=mysqlPort, user=mysqlUser, passwd=mysqlPassword, dbName=mysqlName)
get_media_screenCount(2028, '2019-02-14',conn = connect )



