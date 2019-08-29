# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: quick_sort.py
@time: 2019/8/29 23:37
"""
from typing import List


def partition(sort_list: List[int], start_index: int, end_index: int):
    """
    划分待排序数组为连个子数组
    :param sort_list:
    :param start_index:
    :param end_index:
    :return: 分割数组的小标
    """
    key = sort_list[end_index]
    i = start_index - 1
    for j in range(start_index, end_index):  # 这里需要注意 range 中end_index是开区间取值，即end_index - 1
        if sort_list[j] <= key:
            i = i + 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i + 1], sort_list[end_index] = sort_list[end_index], sort_list[i + 1]
    return i + 1


def hoare_partition(sort_list: List[int], start_index: int, end_index: int):
    """
    常见的方法，两个指针分别指向数组的第2个和最后一个，进行比较和交换，返回划分的index下标
    :param sort_list:
    :param start_index:
    :param end_index:
    :return:
    """
    key = sort_list[start_index]
    i = start_index + 1
    j = end_index

    while True:
        while sort_list[j] >= key and j > start_index:  # j 不能设置大于等于
            j = j - 1
        while sort_list[i] <= key and i < end_index:  # 其中i 不能设置小于等于，防止列表出现重复子串时候出现错误
            i = i + 1

        if j > i:
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
        else:
            sort_list[start_index], sort_list[j] = sort_list[j], sort_list[start_index]
            return j


def quick_sort(sort_list: List[int], start_index: int, end_index: int):
    """
    快速排序
    :param sort_list: 待排序的列表
    :param start_index: 列表数组的开始下标
    :param end_index: 列表数组的最后一个小标
    :return:
    """
    if start_index < end_index:
        # mid_index = partition(sort_list, start_index, end_index)
        mid_index = hoare_partition(sort_list, start_index, end_index)
        quick_sort(sort_list, start_index, mid_index - 1)
        quick_sort(sort_list, mid_index + 1, end_index)


if __name__ == "__main__":
    a = [2, 8, 7, 4, 3, 5, 6, 4]
    quick_sort(a, 0, len(a) - 1)
    print(a)
