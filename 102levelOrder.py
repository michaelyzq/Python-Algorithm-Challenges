"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""


class Solution(object):
    def levelOrder(self, root):
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
        self.items.append(valList)
        return self.appendNode(nextList)
