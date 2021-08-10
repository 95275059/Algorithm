"""
108.将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
解题思路:中序遍历二叉树 -》有序数组。本题目是给定有序数组，还原平衡二叉树
二叉搜索树的中序遍历是升序序列，题目给定的数组是按照升序排序的有序数组，因此可以确保数组是二叉搜索树的中序遍历序列。
给定二叉搜索树的中序遍历，是否可以唯一地确定二叉搜索树？
    答案是否定的。
    如果没有要求二叉搜索树的高度平衡，则任何一个数字都可以作为二叉搜索树的根节点，因此可能的二叉搜索树有多个。
如果增加一个限制条件，即要求二叉搜索树的高度平衡，是否可以唯一地确定二叉搜索树？
    答案仍然是否定的。
    直观地看，我们可以选择中间数字作为二叉搜索树的根节点，这样分给左右子树的数字个数相同或只相差 1，可以使得树保持平衡。
    如果数组长度是奇数，则根节点的选择是唯一的
    如果数组长度是偶数，则可以选择中间位置左边的数字作为根节点或者选择中间位置右边的数字作为根节点，选择不同的数字作为根节点则创建的平衡二叉搜索树也是不同的。
确定平衡二叉搜索树的根节点之后，其余的数字分别位于平衡二叉搜索树的左子树和右子树中，左子树和右子树分别也是平衡二叉搜索树，因此可以通过递归的方式创建平衡二叉搜索树。
在给定中序遍历序列数组的情况下，每一个子树中的数字在数组中一定是连续的，因此可以通过数组下标范围确定子树包含的数字
    下标范围记为 [left,right]。
    对于整个中序遍历序列，下标范围从 left=0 到 right=nums.length−1。
    当 left>right 时，平衡二叉搜索树为空。
"""
import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        总是选择中间位置左边的数字作为根节点
        时间击败93.47%，内存击败15.06%
        """
        def helper(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        return help(0, len(nums)-1)
