# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: add_two_sum.py
@time: 2019/9/18 7:56
"""

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 思路： 1. 先将链表进行逆置
    #        2. 对逆置后的链表进行位数相加，如果大于10，就递进一位；得到最后的结果
    #        3. 将得到的链表进行逆置，得到最终的结果

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_reverse = self.reverse_list(l1)
        l2_reverse = self.reverse_list(l2)
        pass


    @staticmethod
    def reverse_list(l: ListNode) -> ListNode:
        """
        使用两个指针对链表进行逆置, p2 用于指向当前链表的两个前后节点； p3用于保存逆置的结果
        缺点需要开辟新的空间来存储节点（空间复杂度会高）
        """
        # if listNode 只有一个元素，直接返回
        if l is None or l.next is None:
            return l
        p2 = l  # second node
        p3 = None  # reserve list node
        while p2 is not None:
            tmp_node = ListNode(p2.val)
            tmp_node.next = p3 if p3 is not None else None
            p2 = p2.next
            p3 = tmp_node
        return p3


if __name__ == "__main__":
    l1 = ListNode(3)
    l2 = ListNode(4)
    l3 = ListNode(7)
    l4 = ListNode(8)
    l5 = ListNode(9)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    s = Solution()
    result = s.reverse_list(l1)
    while result is not None:
        print(result.val)
        result = result.next



