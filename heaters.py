# coding: utf8
# datetime: 2021-03-12
# 题目地址: https://leetcode-cn.com/problems/heaters/

from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heater_len = len(heaters)
        if heater_len == 1:
            return max(houses[-1]-heaters[0], heaters[0]-houses[0])
        min_ret = 0
        for house in houses:
            tmp_min = abs(heaters[0]-house)
            for heater in heaters[1:]:
                tmp_min = min(abs(heater-house), tmp_min)
            min_ret = max(tmp_min, min_ret)
        return min_ret


a = Solution()
print(a.findRadius([1,2,3,4], [1,4]))