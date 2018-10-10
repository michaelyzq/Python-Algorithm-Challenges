"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root  :
            return []
        self.items = []
        self.appendNode([root])
        return self.items
    def appendNode(self, nodes):

        if len(nodes) == 0:
            return
        nextList = []
        valList = []
        for i in nodes:
            valList.append(i.val)
            if i.left != None:
                nextList.append(i.left)
            if i.right != None:
                nextList.append(i.right)
        self.items.insert(0,valList)
        return self.appendNode(nextList)