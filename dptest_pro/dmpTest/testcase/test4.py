# -*- coding: utf-8 -*-

import os
import openpyxl
import unittest
import shutil


# if not os.path.exists("test_case1"):
#     os.mkdir("test_case1")
#
# shutil.copy('test1.py', 'test_case1')


# 当前脚本的真实路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
caseName = "test_case"

path  = os.path.join(cur_path)
print(path)
dirs = os.listdir(path)
print(dirs)
for it in dirs:
    if it == 'test_case':
        # shutil.rmtree(os.path.join(cur_path,it))
        # print("删除成功！")
        print(it)
        break
    else:
        print("没有这个目录，请检查！！")
        # print(os.path.join(cur_path,it))


# shutil.rmtree(path)