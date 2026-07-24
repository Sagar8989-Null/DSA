# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # Base case: if the list is empty, return None
        if not nums:
            return None
        
        # Find the middle index
        mid = len(nums) // 2
        
        # Make the middle element the root node
        root = TreeNode(nums[mid])
        
        # Recursively construct the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
        