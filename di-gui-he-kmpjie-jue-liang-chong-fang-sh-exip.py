# coding: utf8
# datetime: 2021-03-14
# 题目地址：https://leetcode-cn.com/problems/check-subtree-lcci/solution/di-gui-he-kmpjie-jue-liang-chong-fang-sh-exip/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None:
            return not t2
        if t2 == None:
            return True
        # find the root of t2 in t1
        return self.dfs(t1, t2) or self.checkSubTree(t1.left , t2) or self.checkSubTree(t1.right, t2)
    
    def dfs(self, t1, t2):
        # t2 is over
        if t2 == None:
            return True
        # t2 is not over and t1 is over
        elif t2 != None and t1 == None:
            return False
        # not equal
        elif t2.val != t1.val:
            return False
        # equal, then search left and right
        else:
            return self.dfs(t1.right, t2.right)

