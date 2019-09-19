# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    两个解法差不多，都不是最优的
    """
    __MIN = pow(-2, 31)
    __MAX = pow(2, 31) - 1

    def reverse(self, x: int) -> int:
        # print(self.__MAX, self.__MIN)
        # 数字转换成字符串
        x_str = str(x)
        if x_str[0] == '-':
            unsigned_x_reverse_str = "-"
        signed_x_reverse_str = unsigned_x_reverse_str + x_str[::-1].lstrip("0").rstrip("-")
        result = int(signed_x_reverse_str)
        return 0 if result < self.__MIN or result > self.__MAX else result

    def reverse1(self, x: int) -> int:
        """
        first commit
        :param x:
        :return:
        """
        # print(self.__MAX, self.__MIN)
        # 数字转换成字符串
        x_str = str(x)
        start_index = 0 if x_str[0] is not '-' else 1
        # unsigned_x_reverse_str = reversed(x_str[start_index:]).
        unsigned_x_reverse_str = x_str[::-1]
        if start_index:
            unsigned_x_reverse_str = "-" + unsigned_x_reverse_str.replace('-', '')
            # print("---", unsigned_x_reverse_str)
        result = int(unsigned_x_reverse_str)
        return 0 if result < self.__MIN or result > self.__MAX else result


if __name__ == "__main__":
    s = Solution()
    # print(s.reverse(123))
    # print(s.reverse(120))
    print(s.reverse(-123))
    print(s.reverse(-59700000006))
    # print(s._MAX)
    # print(s._MAX)
