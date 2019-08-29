# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: python_excise
@file: new_init.py
@time: 20190828 22:48
"""


class NewInit(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ called...")
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        print("__init__ called....")


if __name__ == "__main__":
    new = NewInit()
