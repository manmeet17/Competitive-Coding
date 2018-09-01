# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rotate(self,root):
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.rotate(root.left)
        self.rotate(root.right)
        return root
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if(root.left and root.right):
            root.right=self.rotate(root.right)
        def check(left,right):
            if not left and not right:
                return 1
            if (left and not right) or (right and not left):
                return 0
            # print (left.val,right.val)
            if(left.val!=right.val):
                return 0
            l=check(left.left,right.left)
            r=check(left.right,right.right)
            return (l and r)
        return (bool(check(root.left,root.right)))
