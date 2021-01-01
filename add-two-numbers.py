# coding: utf8
# 题目地址：https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_sum = ListNode()
        l_add = 0
        while True:
            num_add = l1.val + l2.val + l_add
            l_sum.val = num_add%10
            l_sum.next = ListNode()
            l_add = num_add//10
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l1 is not None:
                while l2:
                    num_add = l2.val + l_add
                    l_sum.val = num_add%10
                    l_sum.next = ListNode()
                    l_add = num_add//10
                    l2 = l2.next
                break
            elif l2 is None and l1 is not None:
                while l1:
                    num_add = l1.val + l_add
                    l_sum.val = num_add%10
                    l_sum.next = ListNode()
                    l_add = num_add//10
                    l1 = l1.next
                break
        
        return l_sum


a = Solution()

print(a.addTwoNumbers())