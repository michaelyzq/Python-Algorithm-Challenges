"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/description/
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        curr = head
        dummy = ListNode(0)
        dummy.next=head
        curr = dummy
        prev = None
        while curr.next:  
            if curr.val == val:
                if prev !=None:
                    prev.next = curr.next            
                else:
                    prev = dummy
                curr = curr.next    
            else:
                prev = curr
                curr = curr.next
        if prev != None and curr.val == val:
            prev.next = None
        elif prev ==None and curr.val == val:
            return None
        return dummy.next