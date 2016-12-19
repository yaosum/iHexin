#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function.get_excel_data import GetExcelData
from get_project_path import GetProjectPath
import os

"""
功能:从excel文件把关于pytest的配置信息读取出来,然后以运行pytest的命令形势的字符串保存在txt文件中。
"""
def get_pytest_configure():
    get_excel_data = GetExcelData()
    run_str = get_excel_data.pytestConfigure()
    file_path = GetProjectPath.getProjectPath() + '/temFile/pytestConfigure.txt'
    file = open(file_path, 'w')
    if os.path.isfile(file_path):
        file.write("{}\n".format(run_str))
        file.close()
    else:
        file.truncate()
        file.write("{}\n".format(run_str))
        file.close()