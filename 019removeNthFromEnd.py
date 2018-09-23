'''

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        next = head
        d = {}
        i = 1
        if next ==None:
            return head
        while next:
            d[i] = next
            next = next.next
            i = i+1       
        if i-n-1 == 0:
            head = d[2] if 2 in d else None
        elif n==1:
            d[i-n-1].next = None
        else:
            d[i-n-1].next = d[i-n+1]
        return head