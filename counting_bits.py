# coding: utf8
# datetime: 2021-03-03
# 题目地址： https://leetcode-cn.com/problems/counting-bits/

from typing import List


# 解法一
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         return [bin(i).count('1') for i in range(num+1)]


# 解法二
class Solution:
    def __init__(self):
        self.res = [0]

    def countBits(self, num: int) -> List[int]:
        for i in range(1, num+1):
            self.res.append(self.res[i&(i-1)]+1)
        return self.res


a = Solution()
print(a.countBits(5))
