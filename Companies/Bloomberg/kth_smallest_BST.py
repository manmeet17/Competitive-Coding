# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.val=0
            
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def revert(root):
            if not root:
                return (None,False)
            l=revert(root.left)
            self.val+=1
            if(self.val==k):
                return (root.val,True)
            r=revert(root.right)
            if(l[1]):
                return l
            if(r[1]):
                return r
            return (None,False)
        return revert(root)[0]
