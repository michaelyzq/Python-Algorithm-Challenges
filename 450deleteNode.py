
https://leetcode.com/problems/delete-node-in-a-bst/description/
"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node = self.getNode(root, key)
        if not node:
            return root
        parent = self.getParent(node, root)
        root = self.removeNode(node, parent, root)
        return root
    def getNode(self, currentNode, key):
        if not currentNode:
            return None
        elif currentNode.val == key:
            return currentNode
        elif key < currentNode.val:
            return self.getNode(currentNode.left, key)
        else:
            return self.getNode(currentNode.right, key)
    def getParent(self, currentNode, start):        
        if not start:
            return None
        elif currentNode in [start.left, start.right]:
            return start
        elif start.val>currentNode.val:
            return self.getParent(currentNode, start.left)
        elif start.val<currentNode.val:
            return self.getParent(currentNode, start.right)
    def removeNode(self, node, parent, root):
        if node == root:
            if root.right is not None and root.left is not None:
               pass
            elif root.right is not None:
                root = root.right
                root.right = None
                return root
            elif root.left is not None:
                root = root.left
                root.left = None
                return root
            else:
                root = None
                return root
        if node.left is None and node.right is None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None or node.right is None:
            if node.right is None and parent.left ==node:
                parent.left = node.left
            elif node.left is None and parent.left ==node:
                parent.left = node.right
            elif node.right is None and parent.right ==node:
                parent.right = node.left
            elif node.left is None and parent.right ==node:
                parent.right = node.right
        else:
            succ = self.findSuccessor(node, root)
            succParent = self.getParent(succ, root)
            node.val = succ.val
            root = self.removeNode(succ, succParent, root)
        return root
    def findMin(self,current):
        while current.left:
            current = current.left
        return current
    def findSuccessor(self, current, root):
        succ = None
        if current.right is not None:
            succ = self.findMin(current.right)
        else:
            parent = self.getParent(current, root)
            if parent is not None:
                   if current == parent.left:
                       succ = parent
                   else:
                       parent.right = None
                       succ = self.findSuccessor(parent, root)   
                       parent.right = current
        return succ



    
        
