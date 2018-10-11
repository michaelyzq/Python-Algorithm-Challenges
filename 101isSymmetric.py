"""
https://leetcode.com/problems/symmetric-tree/description/
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left is not None and root.right is not None and root.left.val != root.right.val:
            return False
        tempList = []
        self.inOrderTravel( tempList, root)
        print tempList
        while len(tempList)>1:
            if tempList.pop(0) !=tempList.pop():
                return False
        return True
    def inOrderTravel(self,tempList,root):
        if root.left != None:
            self.inOrderTravel( tempList, root.left)       
        tempList.append(root.val)     
        if root.right != None:
            self.inOrderTravel( tempList, root.right)
"""
