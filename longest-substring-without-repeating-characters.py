# coding: utf8
# datetime: 2021-03-05
# 题目地址: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        if str_len == 0:
            return 0
        max_len_list = [1]*str_len
        for i in range(1, str_len):
            tmp_str = s[i]
            for j in range(i-1, -1, -1):
                if s[j] in tmp_str:
                    break
                max_len_list[i] += 1
                tmp_str += s[j]
        return max(max_len_list)



a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))
