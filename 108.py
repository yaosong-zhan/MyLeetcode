# 题目：将升序数组，转换为高度平衡二叉搜索树

# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# 思路：高度平衡二叉树，那么根节点最直接的想法就是中位数，然后用递归可以得到左右两个分支的subtree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        mid = round(len(nums)/2)
        root = TreeNode(nums[mid])
        #递归，左右的subtree用同一个函数来求
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[(mid+1):])
        return root