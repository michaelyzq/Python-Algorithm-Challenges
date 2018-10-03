"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        labels = []
        if not head:
            return head
        curr = head
        prev = None
        while curr.next:
            if curr.val in labels:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                labels.append(curr.val)
                curr = curr.next
        if prev != None and prev.val == curr.val:
            prev.next = None
        return head