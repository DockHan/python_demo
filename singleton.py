# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: singleton.py
@time: 2019/8/28 23:09
"""

import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


if __name__ == "__main__":
    o1 = Singleton()
    o2 = Singleton()

    print(o1)
    print(o2)
