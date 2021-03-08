# coding: utf8
# datetime: 2021-03-08
# 题目地址: https://leetcode-cn.com/problems/palindrome-partitioning-ii/


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        f = [[True]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        m = [float("inf")] * n
        for i in range(n):
            if f[0][i]:
                m[i] = 0
            else:
                for j in range(i):
                    if f[j + 1][i]:
                        m[i] = min(m[i], m[j] + 1)
        
        return m[n - 1]



a = Solution()
print(a.minCut("cdd"))
