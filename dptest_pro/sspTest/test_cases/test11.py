import MySQLdb, datetime, time
#code���ֺ���
code_mean = {10:"��ʼ���أ�10��",
                   11:"������ɣ�11��",
                   12:"��װ���棨12��",
                   13:"��װ�ɹ���13��",
                   14:"������Ϸ��14��",
                   16:"���¿�ʼ��16��"}
#Networktype���ֺ���
network_type_mean = {1:"3G  ����",
                     2:"2G  ����",
                     3:"WIFI����"}
#��ǰ������Աӵ���ֻ�
phonelist = {1:"0049990********", 2:"8689430********", 3:"3558680********"}
#��ǰϵͳʱ��
nowtime = (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
print "��ǰʱ�䣺" + nowtime
today = str(nowtime).split()[0]
#ȥ������
HMS = nowtime.split()[1]

print "Ŀǰ������Աӵ�е��ֻ����£�"
print "HTC    ***  ��1"
print "HTC    ****  ��2"
print "HUAWEI ***** ��3"

phont_imei = raw_input("��ѡ����Ҫ��ѯ���ֻ������������ֻ���Ӧ�����ּ��ɣ�")
time_start = raw_input("��������Ҫ��ѯ����ʼʱ�䣨��ʽ���" + HMS + "��Ĭ������Ϊ���죩: ")
imei = phonelist[int(phont_imei)]
#��ѯ��ʼʱ��
starttime = datetime.datetime.now()

print "��ʼ�������ݿ�......"
try:
    db = MySQLdb.connect(host="***.***.***.***", port=****, user="****", passwd="****", db="****")
    cursor = db.cursor()
    print "���ݿ����ӳɹ�����ʼ���в�ѯ......"
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
    print "�ѻ�ȡ��ѯ�������ʼ�Ͽ����ݿ�����....."
    cursor.close()
    db.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
else:
    print "�Ͽ����ݿ����ӳɹ�����ʼչʾ��ѯ���......"
    if bool(result) != True:
        print "( �� o �� )��Ŷ����Ȼû�в�ѯ�����ݽ���������²�ѯʱ��"
    else:
        #�Բ�ѯ�������ݽ��д�������鿴
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
#���չʾʱ��
endtime = datetime.datetime.now()
wast_time = (endtime - starttime).seconds
print "���β�ѯ�ܹ���ʱ��" + str(wast_time) + " �� " + "��ѯ�ֻ�IMEI��" +  phonelist[int(phont_imei)]__author__ = 'Administrator'
