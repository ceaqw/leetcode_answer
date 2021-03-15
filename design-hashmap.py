# coding: utf8
# datetime: 2021-03-14
# 题目地址：https://leetcode-cn.com/problems/design-hashmap/


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key%100 in self.hash_map:
            self.hash_map[key%100][key] = value
        elif:
            self.hash_map[key%100] = {key: value}

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key%100 in self.hash_map:
            return self.hash_map[key%100][key]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key%100 in self.hash_map:
            if key in self.hash_map[key%100]:
                self.hash_map[key%100].pop(key)
 