# coding: utf8
# datetime: 2021-03-13
# 题目地址: https://leetcode-cn.com/problems/longest-word-in-dictionary/


from typing import List


class Solution(object):
    def longestWord(self, words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""

