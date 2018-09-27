'''
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
'''
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        while curr.next and curr.next.next:

            temp = ListNode(curr.next.val)
            temp2 = ListNode(curr.next.next.val)         
            temp2.next = temp
            if curr.next.next.next:
                temp.next = curr.next.next.next
            else:
                temp.next = None
            
            curr.next = temp2
            curr.next.next =temp 
            curr = temp 
        return dummy.next