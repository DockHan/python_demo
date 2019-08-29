# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: attr_methods.py
@time: 2019/8/28 23:20
"""


class A:
    _instance = 'class_variable'

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @staticmethod
    def class_method():
        return "class method"


if __name__ == "__main__":
    setattr(A, '_instance', [1, 2, 3, 4])
    print(getattr(A, "_instance"))
    setattr(A, 'not_exist_instance', "not_exist_instance")
    print(getattr(A, "not_exist_instance"))
