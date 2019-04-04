# coding=utf-8

import os
import shutil
from utils.methods import file_name as file_name
import constants.deploy as deploy




############################### 配置文件的地址######################
# 当前脚本的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# bae_idr = cur_path.replace('\\', '/')
#
# file_path = bae_idr + "/config.ini"
# conf = cparser.ConfigParser()
#
# conf.read(file_path)


# ######################读取配置文件上###################################
# wbook = openpyxl.load_workbook(conf.get("excel", "excel_path")) # 读取配置文件的Excel文档地址
# table2 = wbook[conf.get("excel", "table")] # 读取配置文件的Excel文档所使用的用例table

wbook = deploy.wbook
table2 = deploy.table2



# 读取Excel内容
# wbook=openpyxl.load_workbook(cur_path + "/testexcel/dmptest3.xlsx")
# table2=wbook['Test_Case2']

# 用例文件夹
caseName = "sspCase"
case_path = os.path.join(cur_path, caseName)
print(case_path)


#########################加载用例#####################################
begtest=[]
endtest=[]

for i in range(1,int(table2.max_column)):
    if table2["C"+str(i)].value=="go":
        begtest.append(i)

    if table2["L"+str(i)].value=="end":
        endtest.append(i)
if len(begtest)==0:#检查是否有可用的用例
    print('没有可执行的用例')
    quit()
if len(begtest)!=len(endtest):
    print("用例有误,请检查各单元用例的开始和结束是否一致")
    quit()
print("测试用例检查完成")

#########################比对需要执行的案例#####################################
caseitem = []
print("文件中的案例：" + str(len(file_name(case_path))), "Excel中需要测试的案例：" + str(len(begtest)))
for i in range(len(begtest)):  # 以Excel总数为基准循环
    # print("当前i" + str(i))
    for j in range(2,int(begtest[i]) + 1): # 循环Excel中的每一条用例
        # print("当前j" + str(j))
        # print("excel:"+table2["D"+str(j)].value)
        for k in range(len(file_name(case_path))): #循环case 目录下的每一条用例
            # print("当前k" + str(k))
            if file_name(case_path)[k] == table2["D"+str(j)].value: # 判断case目录中的案例与Excel中的是否一致，是写入ss list中
                # print(file_name(case_path)[k],table2["D"+str(j)].value)
                # bb = str(file_name(case_path)[i] + '.py')
                testcase = str(file_name(case_path)[i] + '.py')
                if testcase not in caseitem:
                    caseitem.append(testcase)

# print(ss)


#########################将可执行案例放到临时文件夹中#####################################
for i in range(0,len(caseitem)):
    if not os.path.exists(cur_path +"/test_case"):
        os.makedirs(cur_path +"/test_case")
    # for root, dirs, files in os.walk(aa):
    #     for file in  files:
    #         if os.path.join(file) == ss[i]:
    #             shutil.copy(os.path.join(file), 'test_case')
    shutil.copy(case_path + "/" + caseitem[i], cur_path +"/test_case")

print("案例加载完毕，待测试案例：" + str(caseitem))


