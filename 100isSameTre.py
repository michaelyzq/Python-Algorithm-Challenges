"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
https://leetcode.com/problems/same-tree/description/
"""
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p or q) and not (p and q):
            return False
        elif not (p or q):
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
    