# coding: utf8
# datetime: 2021-03-05
# 题目地址: https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        is_positive = True
        num_list = []
        if x < 0:
            is_positive = False
            x = 0-x
        while x:
            num_list.insert(0, x%10)
            x //= 10
        
        reverse_num = 0
        for i in range(len(num_list)):
            reverse_num += num_list[i]*10**i
        reverse_num = reverse_num if is_positive else 0-reverse_num
        if reverse_num > 2**31-1 or reverse_num < -2**31:
            reverse_num = 0
        return reverse_num


a = Solution()
print(a.reverse(0))
