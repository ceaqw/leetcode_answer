# coding: utf8
# datetime: 2021-03-08
# 题目地址: https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)


a = Solution()
print(a.removeDuplicates("abbaca"))
        