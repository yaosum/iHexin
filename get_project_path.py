#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class GetProjectPath(object):
    """
        功能:获取工程根目录路径
    """
    @classmethod
    def getProjectPath(cls):
        return os.path.dirname(os.path.abspath(__file__))