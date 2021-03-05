# coding: utf8
# datetime: 2021-03-05
# 题目地址: https://leetcode-cn.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_list = []
        self.peek_index = -1


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_list.insert(0, x)
        self.peek_index += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        pop_element = None
        if self.peek_index > -1:
            pop_element = self.stack_list.pop(self.peek_index)
            self.peek_index -= 1
        return pop_element

    def peek(self) -> int:
        """
        Get the front element.
        """
        peek_element = None
        if self.peek_index > -1:
            peek_element = self.stack_list[self.peek_index]
        return peek_element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if self.peek_index == -1 else False
