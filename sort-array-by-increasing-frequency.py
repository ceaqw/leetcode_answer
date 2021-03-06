# coding: utf8
# datetime: 2021-03-05
# 题目地址: https://leetcode-cn.com/problems/sort-array-by-increasing-frequency/


from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: (nums.count(x), x))


a = Solution()
print(a.frequencySort([1,1,2,2,2,3]))
