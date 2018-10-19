"""
https://leetcode.com/problems/longest-univalue-path/description/

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
      
        """
        if not root:
            return 0
        self.none_root_parse = 0
        a = self.getlongestUnivaluePath(root)
        return max(a, self.none_root_parse)

    def getlongestUnivaluePath(self, root):
        def checkLongestVPath( root):
            leftl = 0
            rightl = 0
            if root.left is not None:
                if root.left.val == root.val:
                    leftl = 1 + checkLongestVPath(root.left)
                else:
                    leftl = 0 
            if root.right is not None :
                if root.right.val == root.val:
                    rightl =1+ checkLongestVPath(root.right)
                else:
                    rightl = 0 
            return max(leftl, rightl)
        def checkVShape(root):
            if root.left is not None and root.right is not None :
                if root.left.val ==root.val and  root.val == root.right.val:
                    linkv = 2 + checkLongestVPath(root.left) + checkLongestVPath(root.right)
                    if linkv >self.none_root_parse:
                        self.none_root_parse = linkv
            return
       
        checkVShape(root)
        leftl,right1 = 0,0
        if  root.left is not None :
            checkVShape(root.left)
            if root.left.val == root.val:
                leftl = max(1 + checkLongestVPath(root.left),self.getlongestUnivaluePath(root.left))
            else:
                leftl = self.getlongestUnivaluePath(root.left)
        if root.right is not None:
            checkVShape(root.right)
            if root.right.val == root.val:
                right1 =max(1+checkLongestVPath(root.right), self.getlongestUnivaluePath(root.right))
            else:
                right1 = self.getlongestUnivaluePath(root.right)
        return max(leftl, right1)
       