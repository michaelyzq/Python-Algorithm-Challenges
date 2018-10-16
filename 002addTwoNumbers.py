"""
https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1nums = 0
        l1n =0
        while l1:
            l1nums = l1nums + l1.val*(10**l1n)
            l1= l1.next
            l1n = l1n+1
        l2nums = 0
        l2n =0
        while l2:
            l2nums = l2nums + l2.val*(10**l2n)
            l2 = l2.next
            l2n = l2n+1
        num_val = l1nums + l2nums
        ret = ListNode(0)
        curr = ListNode(0)
        ret.next = curr
        while num_val:
            yu = num_val % 10
            curr.val =yu
            
            num_val = num_val //10
            if num_val >0:
                curr.next = ListNode(0)
                curr = curr.next

        return ret.next
