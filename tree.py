# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: Zhiyuan Han
@license: Personal
@contact: hange_8735@163.com
@site: https://github.com/DockHan
@software: PyCharm
@file: tree.py
@time: 2019/9/6 21:56
"""
from typing import List, Any
from queue import Queue


class Stack:
    """
    实现栈数据结果，用于树的非递归遍历
    """

    def __init__(self):
        self._stack_list = []

    def push(self, node: Any):
        """
        存放数据到栈中
        :param node:
        :return:
        """
        self._stack_list.append(node)

    def pop(self):
        if self._stack_list:
            # last_item = self._stack_list[-1]
            # del self._stack_list[-1]  # 需要check del列表中的一个元素，对应去除的元素是否还存在
            return self._stack_list.pop(-1)
        else:
            return None

    def is_empty(self):
        """
        栈是否为空
        :return:
        """
        if not self._stack_list:
            return True
        else:
            return False

    def get_top(self):
        """
        获取栈顶的value
        :return:
        """
        if self._stack_list:
            return self._stack_list[-1]
        else:
            return None

    def __str__(self):
        print(self._stack_list)

    def print_stack(self):
        print(self._stack_list)


class Node:
    """
    树的节点定义
    """

    def __init__(self, value):
        self.value = value
        self.left_tree = None
        self.right_tree = None


class BinaryTree:
    '''
    二叉树的各种遍历操作： 递归的方法
    '''

    def __init__(self):
        self.result_list = None

    def init_result(self):
        self.result_list = []

    def print_result_list(self, message: str = None) -> None:
        print(message)
        print(self.result_list)

    def in_order(self, node: Node) -> List[int]:
        '''
        中序遍历, 需要保存到数组里，使用前请调用self.init_result() function
        '''
        if node is None:  # None，直接return
            return []
        self.in_order(node.left_tree)
        self.result_list.append(node.value)
        self.in_order(node.right_tree)
        return self.result_list

    def pre_order(self, node: Node) -> List[int]:
        '''
        前序遍历， 需要保存到数组里，使用前请调用self.init_result() function
        :param node: 要前序遍历的node
        :return:
        '''
        if node is None:  # None，直接return
            return []
        self.result_list.append(node.value)
        self.pre_order(node.left_tree)
        self.pre_order(node.right_tree)
        return self.result_list

    def post_order(self, node: Node) -> List[int]:
        '''
        后续遍历， 需要保存到数组里，使用前请调用self.init_result() function
        '''
        if node is None:  # None，直接return
            return []
        self.post_order(node.left_tree)
        self.post_order(node.right_tree)
        self.result_list.append(node.value)
        return self.result_list

    def level_order(self, node: Node) -> List[int]:
        '''
        层次遍历，需要保存到数组里，该方法内部已经调用self.init_result()， 无需外部调用
        使用队列的数据结构，将节点放到队列中，先进先出
        '''
        self.init_result()
        if node is None:  # None，直接return
            return []
        q = Queue()  # 使用队列对树进行层次遍历
        q.put(node)  # first add root node
        while q.qsize() != 0:
            get_node = q.get()  # type: Node
            self.result_list.append(get_node.value)
            if get_node.left_tree:
                q.put(get_node.left_tree)
            if get_node.right_tree:
                q.put(get_node.right_tree)
        return self.result_list


class BinaryTreeOptimization:
    """
    基于堆栈的方法对二叉树进行遍历，算法进一步会优化
    """
    @staticmethod
    def in_order(node: Node) -> List[int]:
        """
        借助队列和队列，对二叉树进行中序遍历
        :param node:
        :return:
        """
        if node is None:  # None，直接return
            return []

        result = []
        stack = []
        pos = node
        while pos is not None or len(stack) > 0:
            if pos is not None:
                stack.append(pos)
                pos = pos.left_tree
            else:
                pos = stack.pop()
                result.append(pos.value)
                pos = pos.right_tree

        return result

    @staticmethod
    def pre_order(node: Node) -> List[int]:
        """
        借助队列和队列，对二叉树进行中序遍历,前序遍历
        :param node:
        :return:
        """
        if not node:  # 节点为None，直接return
            return []

        result = []
        s = Stack()
        s.push(node)
        while s.is_empty() is not True:
            get_node = s.pop()  # type: Node
            result.append(get_node.value)
            if get_node.right_tree:  # 先将右子树压栈
                s.push(get_node.right_tree)
            if get_node.left_tree:
                s.push(get_node.left_tree)
        return result

    def post_order(self, node: Node) -> List[int]:
        """
        # 后序打印二叉树（非递归）
        # 使用两个栈结构
        # 第一个栈进栈顺序：左节点->右节点->跟节点
        # 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
        # 第二个栈存储为第一个栈的每个弹出依次进栈
        # 最后第二个栈依次出栈
        :param node:
        :return:
        """
        if not node:
            return []
        result = []
        stack = [node]
        stack2 = []
        while len(stack) > 0:
            node = stack.pop()
            stack2.append(node)
            if node.left_tree is not None:
                stack.append(node.left_tree)
            if node.right_tree is not None:
                stack.append(node.right_tree)
        while len(stack2) > 0:
            result.append(stack2.pop().value)
        return result


class BuildBinaryTree:
    """
    重建二叉树
    """
    def __init__(self, pre_order: List[int], in_order: List[int]) -> None:
        self.node = None  # type: Node
        self.pre_order = pre_order  # type: list
        self.in_order = in_order  # type: list

    def build_binary_tree(self, pre_start_index: int, pre_end_index: int,
                          in_start_index: int, in_end_index: int) -> Node:
        """
        重建二叉树
        :param pre_start_index: 前序遍历的列表起始下标
        :param pre_end_index: 前序遍历的列表结束下标
        :param in_start_index: 中序遍历的列表起始下标
        :param in_end_index: 中序遍历的列表结束下标
        :return: 二叉树
        """
        if self.pre_order is None and self.in_order is None \
                and len(self.pre_order) == 0 and len(self.in_order) == 0:
            return None

        # 前序遍历的第一个是根节点
        root_value = self.pre_order[pre_start_index]
        self.node = Node(root_value)
        if pre_end_index == pre_start_index:
            if in_start_index == in_end_index:
                return self.node
            else:
                raise Exception("Your input list is invalidate")

        # 在中序遍历中找到根节点
        in_index = in_start_index
        while in_index <= in_end_index:
            if self.in_order[in_index] == root_value:





if __name__ == "__main__":
    a = []
    b = None
    print(len(a) == 0)
    print(b is None)
    # node_leaf_4 = Node(4)
    # node_leaf_8 = Node(8)
    # node_leaf_12 = Node(12)
    # node_leaf_16 = Node(16)
    #
    # node_6 = Node(6)
    # node_6.left_tree = node_leaf_4
    # # node_6.left_tree = None
    # node_6.right_tree = node_leaf_8
    #
    # node_14 = Node(14)
    # node_14.left_tree = node_leaf_12
    # node_14.right_tree = node_leaf_16
    #
    # node_root = Node(10)
    # node_root.left_tree = node_6
    # node_root.right_tree = node_14
    #
    # bt = BinaryTree()
    # bt.init_result()
    # pre_order_list = bt.pre_order(node_root)
    # print("pre_order_list:", pre_order_list)
    # bt.init_result()
    # in_order_list = bt.in_order(node_root)
    # print("in_order_list:", in_order_list)
    # bt.init_result()
    # post_order_list = bt.post_order(node_root)
    # print("post_order_list:", post_order_list)
    # level_order_list = bt.level_order(node_root)
    # print("level_order_list:", level_order_list)
    #
    # bto = BinaryTreeOptimization()
    # bto_pre_order_list = bto.pre_order(node_root)
    # print("bto_pre_order_list:", bto_pre_order_list)
    # bto_in_order_list = bto.in_order(node_root)
    # print("bto_in_order_list:", bto_in_order_list)
    # bto_post_order_list = bto.post_order(node_root)
    # print("bto_post_order_list:", bto_post_order_list)
    # print("end")
