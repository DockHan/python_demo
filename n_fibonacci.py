# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: n_fibonacci.py
@time: 2019/9/4 23:33
"""

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

class Solution:
    def __init__(self):
        self.n_value_map = {}
        self.n_value_map[0] = 1
        self.n_value_map[1] = 1
        self.n_value_map[2] = 1

    def Fibonacci(self, n):
        """

        :param n:
        :return:
        """
        # write code here
        if n in self.n_value_map:
            # print(self.n_value_map)
            # print("=" * 10)
            return self.n_value_map[n]
        else:
            result = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
            self.n_value_map[n] = result
            return result

    def fibinacci_good(self, n):
        res = [0, 1, 1, 2]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]

    def Fibonacci_new(self, n):
        fibi_list = [0, 1, 1, 2]  # 0: 1, 1 : 1, 2: 1 对应Fib的值
        index = 4
        if n in [0, 1, 2]:
            return 1
        while index <= n:
            fibi_list.append(fibi_list[-1] + fibi_list[-2])
            index = index + 1
        return fibi_list[n]


if __name__ == "__main__":
    s = Solution()
    # print(s.Fibonacci(39))
    print(s.fibinacci_good(-1))
    print(s.Fibonacci_new(-1))
    print(s.fibinacci_good(2))
    print(s.Fibonacci_new(2))
    print(s.fibinacci_good(3))
    print(s.Fibonacci_new(3))
    print(s.fibinacci_good(4))
    print(s.Fibonacci_new(4))
    print(s.fibinacci_good(5))
    print(s.Fibonacci_new(5))
    print(s.fibinacci_good(11))
    print(s.Fibonacci_new(11))
    print(s.fibinacci_good(22))
    print(s.Fibonacci_new(22))
    print(s.fibinacci_good(39))
    print(s.Fibonacci_new(39))
    print(s.fibinacci_good(40))
    print(s.Fibonacci_new(40))
