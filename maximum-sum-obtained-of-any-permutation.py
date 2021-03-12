# coding: utf8
# datetime: 2021-03-09
# 题目地址: https://leetcode-cn.com/problems/maximum-sum-obtained-of-any-permutation/


from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums_len = len(nums)
        weights = [0]*nums_len
        change_num = 10**9+7
        for request in requests:
            for i in range(request[0], request[-1]+1):
                weights[i] += 1

        weights.sort()
        nums.sort()
        return sum(weight*num for weight, num in zip(weights, nums))%change_num

        # MODULO = 10**9 + 7
        # length = len(nums)
        # counts = [0] * length
        # for start, end in requests:
        #     counts[start] += 1
        #     if end + 1 < length:
        #         counts[end + 1] -= 1
        
        # for i in range(1, length):
        #     counts[i] += counts[i - 1]
        # counts.sort()
        # nums.sort()
        
        # total = sum(num * count for num, count in zip(nums, counts))
        # return total % MODULO



a = Solution()
print(a.maxSumRangeQuery(
    [757,900,712,753,367,2,845,904,340,274,812,466,342,405,128,780,451,675,980,180,89,516,178,236,44],
    [[85,1105],[975,1707],[161,1541],[908,2049],[404,1844],[212,2047]]
))
