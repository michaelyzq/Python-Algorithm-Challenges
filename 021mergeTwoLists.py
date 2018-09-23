"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """     
        l1next = l1
        l2next = l2
        new_node = ListNode(100)
        ret = new_node
        while l1 or  l2:
            if l1== None and l2 == None:
                return None
            elif l1 == None and l2 !=None:
                new_node.next = ListNode(l2.val)
                new_node = new_node.next
                l2 = l2.next
            elif l2 == None and l1 !=None:
                new_node.next = ListNode(l1.val)
                new_node = new_node.next
                l1 = l1.next
            else:
                if  l1.val > l2.val:
                    new_node.next =  ListNode(l2.val)
                    new_node = new_node.next
                    l2 = l2.next
                elif  l2.val >= l1.val:
                    new_node.next = ListNode(l1.val)
                    new_node = new_node.next
                    l1 = l1.next   
        return ret.next