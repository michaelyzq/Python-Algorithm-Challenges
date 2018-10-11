
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.balance = True
        self.travelRoot(root)
        return self.balance
    def travelRoot(self,root):     
        
        if root.left != None:
            if self.travelRoot(root.left) == False:
                return False
        print root.val
        if abs(self.findH(root.left) - self.findH(root.right) )>1:
            print False
            self.balance = False
            return False
        if root.right != None:       
            if self.travelRoot(root.right) == False:
                return False
       

    def findH(self, node):
        return 1+max(self.findH(node.left), self.findH(node.right)) if node else 0