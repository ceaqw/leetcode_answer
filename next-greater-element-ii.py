# coding: utf8
# datetime: 2021-03-06
# 题目地址: https://leetcode-cn.com/problems/next-greater-element-ii/


from typing import List


# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         nums_len = len(nums)
#         result_list = [-1]*nums_len
#         if nums_len > 1:
#             for i in range(nums_len):
#                 current_index = 0 if (i+1) == nums_len else i+1
#                 while True:
#                     if nums[i] < nums[current_index]:
#                         result_list[i] = nums[current_index]
#                         break
#                     current_index += 1
#                     if current_index == nums_len:
#                         current_index = 0
#                     if current_index == i:
#                         break
#         return result_list[:nums_len]


# 单调栈应用
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res_list = [-1]*nums_len
        stack = []

        for i in range(nums_len*2-1):
            index = i%nums_len
            while stack and nums[index] > nums[stack[-1]]:
                res_list[stack.pop()] = nums[index]
            stack.append(index)
        
        return res_list


a = Solution()
print(a.nextGreaterElements([1,2,1]))
