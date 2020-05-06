

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if root:
    #         print(root.val)
    #         if root.left:
    #             if root.left.val < root.val:
    #                 self.isValidBST(root.left)
    #             else:
    #                 return False
    #         if root.right:
    #             if root.right.val > root.val:
    #                 self.isValidBST(root.right)
    #             else:
    #                 return False
    #     return True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(20)

sol = Solution()
ans = sol.isValidBST(bst)
print("^%$##", ans)
