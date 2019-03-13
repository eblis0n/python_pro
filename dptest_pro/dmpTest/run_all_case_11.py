# coding=utf-8
import unittest
from datetime import datetime
from commen import HTMLTestRunner_yo
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import openpyxl
import shutil
#下面三行代码python2报告出现乱码时候可以加上####
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）

# 当前脚本的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# 读取Excel内容
wbook=openpyxl.load_workbook(cur_path + "/testexcel/dmptest3.xlsx")
table2=wbook['Test_Case2']

# 提取case 名称
# 其中os.path.splitext()函数将路径拆分为文件名+扩展名
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.join(file)[0:4] == "test":
                if os.path.splitext(file)[1] == '.py':
                    L.append(os.path.join( file)[0:-3])
    return L


caseName = "case/test_case"
case_path = os.path.join(cur_path, caseName)  # 用例文件夹


begtest=[]
endtest=[]

for i in range(1,int(table2.max_column)):
    if table2["A"+str(i)].value=="go":
        begtest.append(i)

    if table2["L"+str(i)].value=="end":
        endtest.append(i)
if len(begtest)==0:#检查是否有可用的用例
    print('没有可执行的用例')
    quit()
if len(begtest)!=len(endtest):
    print("用例有误,请检查各单元用例的开始和结束是否一致")
    quit()
print("测试用例加载完成")

# print(len(begtest))

ss = []
for i in range(0,len(file_name(case_path))):
    # print("casename:" + file_name(aa)[i])
    print("第" + str(i) + "条用例")
    for j in range(1,len(begtest)):
        for k in range(2, int(begtest[i] + 1)):

            # print("excel:"+table2["C"+str(k)].value)
            if file_name(case_path)[i] == table2["C"+str(k)].value:
                # print(table2["A" + str(k)].value)
                # print(file_name(aa)[i])
                bb = str(file_name(case_path)[i] + '.py')
                ss.append(str(file_name(case_path)[i] + '.py'))
            k = k + 1


# print(ss)

for i in range(0,len(ss)):

    if not os.path.exists(case_path +"/test_case"):
        os.makedirs(case_path +"/test_case")
    # for root, dirs, files in os.walk(aa):
    #     for file in  files:
    #         if os.path.join(file) == ss[i]:
    #             shutil.copy(os.path.join(file), 'test_case')

    shutil.copy(case_path + "/" + ss[i], case_path +"/test_case")



def add_case(caseName, rule):
    '''第一步：加载所有的测试用例'''

    # 如果不存在这个case文件夹，就自动创建一个
    # if not os.path.exists(case_path): os.mkdir(case_path)
    # print("test case path:%s" % case_path)

    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    # report_abspath = os.path.join(report_path, "result.html")
    report_abspath = os.path.join(report_path, "sspresult" + datetime.now().date().isoformat() +  ".html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_yo.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

# def send_mail(sender, psw, receiver, smtpserver, report_file, port):
#     '''第四步：发送最新的测试报告内容'''
#     with open(report_file, "rb") as f:
#         mail_body = f.read()
#     # 定义邮件内容
#     msg = MIMEMultipart()
#     body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
#     msg['Subject'] = u"自动化测试报告"
#     msg["from"] = sender
#     msg["to"] = ",".join(receiver)     # 只能字符串
#     msg.attach(body)
#     # 添加附件
#     att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename= "report.html"'
#     msg.attach(att)
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)                      # 连服务器
#         smtp.login(sender, psw)
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#         smtp.login(sender, psw)                       # 登录
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
#     print('test report email has send out !')


if __name__ == "__main__":
    all_case = add_case(caseName, rule="test*.py")   # 1 加载用例
    # # 生成测试报告的路径
    run_case(all_case)        # 2 执行用例
    # # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")  # 测试报告路径
    report_file = get_report_file(report_path)  # 3 获取最新的测试报告
    # #邮箱配置
    # sender = "yoyo@qq.com"
    # psw = "xxx"
    # smtp_server = "smtp.qq.com"
    # port = 465
    # receiver = "yoyo@qq.com"
    # send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告
