# coding: utf8
# 题目地址：https://leetcode-cn.com/problems/two-sum/

from typing import List


class Solution:
    count = 0
    sum_index = []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_1 = nums[0]
        for num_index in range(1,len(nums)):
            if num_1+nums[num_index] == target:
                self.sum_index = [self.count, self.count+num_index]
                return self.sum_index
        self.count += 1
        self.twoSum(nums[1:], target)
        return self.sum_index
