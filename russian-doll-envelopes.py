# coding: utf8
# datetime: 2021-03-04
# 题目地址: https://leetcode-cn.com/problems/russian-doll-envelopes


from typing import List



class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        len_envelopes = len(envelopes)
        if not len_envelopes:
            return len_envelopes

        # 排序w
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)

        max_child_list = [1]*len_envelopes

        # 求最长子串
        for i in range(len_envelopes):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    max_child_list[i] = max(max_child_list[i], max_child_list[j] + 1)

        print(max_child_list)
        return max(max_child_list)


a = Solution()
print(a.maxEnvelopes([[1,3],[3,5],[6,7],[6,3],[8,4],[9,5]]))
