# coding: utf8
# datetime: 2021-03-13
# 题目地址: https://leetcode-cn.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = set()


    def add(self, key: int) -> None:
        self.key.add(key)

    def remove(self, key: int) -> None:
        if key in self.key:
            self.key.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return True if key in self.key else False