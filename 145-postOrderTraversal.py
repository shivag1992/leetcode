# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        self.helper(root, results)
        return results
    
    def helper(self, root, results):
        if(root == None):
            return
        self.helper(root.left, results)
        self.helper(root.right, results)
        results.append(root.val)
        return
