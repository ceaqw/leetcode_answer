# coding: utf8
# datetime: 2021-03-12
# 题目地址: https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/



class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [1]
        preorder_list = preorder.split(',')
        for ch in preorder_list:
            if not stack:
                return False
            if ch == '#':
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
            else:
                stack[-1] -= 1
                if stack[-1] == 0:
                    stack.pop()
                stack.append(2)
            # print(stack)
        if stack:
            return False
        return True


a = Solution()
print(a.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))