import MySQLdb, datetime, time
#code数字含义
code_mean = {10:"开始下载（10）",
                   11:"下载完成（11）",
                   12:"安装界面（12）",
                   13:"安装成功（13）",
                   14:"启动游戏（14）",
                   16:"更新开始（16）"}
#Networktype数字含义
network_type_mean = {1:"3G  网络",
                     2:"2G  网络",
                     3:"WIFI网络"}
#当前测试人员拥有手机
phonelist = {1:"0049990********", 2:"8689430********", 3:"3558680********"}
#当前系统时间
nowtime = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
print "当前时间：" + nowtime
today = str(nowtime).split()[0]
#去除日期
HMS = nowtime.split()[1]

print "目前测试人员拥有的手机如下："
print "HTC    ***  ：1"
print "HTC    ****  ：2"
print "HUAWEI ***** ：3"

phont_imei = raw_input("请选择你要查询的手机，输入上列手机对应的数字即可：")
time_start = raw_input("请输入需要查询的起始时间（格式如后：" + HMS + "，默认日期为今天）: ")
imei = phonelist[int(phont_imei)]
#查询开始时间
starttime = datetime.datetime.now()

print "开始连接数据库......"
try:
    db = MySQLdb.connect(host="***.***.***.***", port=****, user="****", passwd="****", db="****")
    cursor = db.cursor()
    print "数据库连接成功，开始进行查询......"
    cursor.execute('''SELECT
    ****,
    ****,
    ****,
    ****,
    ****
    from ****
    WHERE
    **** =  \'''' + imei + '''\' AND
    **** > \'''' + today + " " + time_start + '''' AND
    **** IN (10, 11, 12,13,14,16)
    ORDER BY
    **** DESC
    ''')
    result = cursor.fetchall()
    print "已获取查询结果，开始断开数据库连接....."
    cursor.close()
    db.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
else:
    print "断开数据库连接成功，开始展示查询结果......"
    if bool(result) != True:
        print "( ⊙ o ⊙ )啊哦，竟然没有查询到数据结果，请检查下查询时间"
    else:
        #对查询出的数据进行处理，方便查看
        print ""
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        i = 0
        for record in result:
            sqldata = result[i]
            time = sqldata[0]
            code = sqldata[1]
            name = sqldata[2]
            networktype = sqldata[4]
            print network_type_mean[int(networktype)] + \
                    " " + str(time).split()[1] + \
                    " " + code_mean[int(code)] + \
                    " " + name
            i += 1
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#结果展示时间
endtime = datetime.datetime.now()
wast_time = (endtime - starttime).seconds
print "本次查询总共耗时：" + str(wast_time) + " 秒 " + "查询手机IMEI：" +  phonelist[int(phont_imei)]__author__ = 'Administrator'
