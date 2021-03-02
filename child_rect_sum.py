# coding: utf8
# datetime: 2021-03-02

# 题目链接： https://leetcode-cn.com/problems/range-sum-query-2d-immutable/

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum([i for i in [sum(self.matrix[j][col1:col2+1]) for j in range(row1, row2+1)]])

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

a = NumMatrix(matrix)

print(a.sumRegion(2, 1, 4, 3))
print(a.sumRegion(1, 1, 2, 2))
print(a.sumRegion(1, 2, 2, 4))