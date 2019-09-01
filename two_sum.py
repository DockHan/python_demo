# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: two_sum.py
@time: 2019/9/1 22:13
"""
from typing import List


class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # construct the dictionary
        value_index_map = {}
        for i in range(len(nums)):
            value_index_map[nums[i]] = i
        # find the index
        for j in range(len(nums)):
            other_value = target - nums[j]
            if other_value in value_index_map.keys() and j != value_index_map[other_value]:
                other_index = value_index_map[other_value]
                if j < other_index:
                    return [j, other_index]
                else:
                    return [other_index, j]

    def two_sum_opt(self, nums: List[int], target: int) -> List[int]:
        value_index_map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in value_index_map:
                return [value_index_map[another_num], index]
            value_index_map[num] = index


if __name__ == "__main__":
    a = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.two_sum_opt(a, target))

    b = [3, 3]
    target_b = 6
    print(s.two_sum_opt(b, target_b))
