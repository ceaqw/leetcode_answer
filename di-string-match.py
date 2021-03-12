# coding: utf8
# datetime: 2021-03-12
# 题目地址: https://leetcode-cn.com/problems/di-string-match/

from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        S_len = len(S)
        I_index = 0
        D_index = S_len
        arr = list(range(S_len+1))
        rest = list()
        index = 0
        while index < S_len:
            if S[index] == 'I':
                rest.append(arr[I_index])
                I_index += 1
            elif S[index] == 'D':
                rest.append(arr[D_index])
                D_index -= 1

            if index + 1 == S_len:
                if S[index] == "I":
                    rest.append(arr[I_index])
                else:
                    rest.append(arr[D_index])
                break
            index += 1

        return rest


a = Solution()
print(a.diStringMatch("DDI"))
