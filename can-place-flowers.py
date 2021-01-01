# coding: utf8

# 题目地址：https://leetcode-cn.com/problems/can-place-flowers/

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_index_list = []
        flowerbed_len = len(flowerbed)+1
        flower_index = 1
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        while flower_index<flowerbed_len:
            if flowerbed[flower_index-1] == flowerbed[flower_index] == flowerbed[flower_index+1] == 0:
                flower_index_list.append(flower_index)
                flower_index += 2
            else:
                flower_index += 1

        if len(flower_index_list) >= n:
            return True

        return False


test = Solution()

print(test.canPlaceFlowers([1,0,0,0,1], 1))