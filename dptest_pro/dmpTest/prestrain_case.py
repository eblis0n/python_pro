# coding=utf-8

import os
import openpyxl
import shutil
from utils.methods import file_name as file_name

# 当前脚本的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)

# 读取Excel内容
wbook=openpyxl.load_workbook(cur_path + "/testexcel/dmptest3.xlsx")
table2=wbook['Test_Case2']

# 用例文件夹
caseName = "case"
case_path = os.path.join(cur_path, caseName)

#########################加载用例#####################################
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

#########################比对需要执行的案例#####################################

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
    # print("casename:" + file_name(case_path)[i])
# print(ss)

#########################将可执行案例放到临时文件夹中#####################################
for i in range(0,len(ss)):
    if not os.path.exists(cur_path +"/test_case"):
        os.makedirs(cur_path +"/test_case")
    # for root, dirs, files in os.walk(aa):
    #     for file in  files:
    #         if os.path.join(file) == ss[i]:
    #             shutil.copy(os.path.join(file), 'test_case')
    shutil.copy(case_path + "/" + ss[i], cur_path +"/test_case")