# coding: utf8
# datetime: 2021-03-05
# 题目地址: https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points/


from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points_len = len(points)
        if points_len < 2:
            return
        area_width = []
        points = sorted(points, key=lambda x: x[0])
        for i in range(1, points_len):
            area_width.append(points[i][0]-points[i-1][0])

        return max(area_width)


a = Solution()
print(a.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
        