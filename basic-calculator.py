# coding: utf8
# datetime: 2021-03-09
# 题目地址: https://leetcode-cn.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        status_stack = [1]
        sign = 1
        ret = 0
        len_s = len(s)
        i = 0
        while i<len_s:
            if s[i] == " ":
                i += 1
            elif s[i] == '+':
                sign =  status_stack[-1]
                i += 1
            elif s[i] == '-':
                sign =  -status_stack[-1]
                i += 1
            elif s[i] == '(':
                status_stack.append(sign)
                i += 1
            elif s[i] == ')':
                status_stack.pop()
                i += 1
            else:
                num = 0
                while i < len_s and s[i] not in "+-() ":
                    print(i)
                    num = num*10 + int(s[i])
                    i += 1
                ret += num*sign

        return ret


a = Solution()
print(a.calculate("1 + 1"))