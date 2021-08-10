"""
102.二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
解题思路：广度优先搜索
"""
import TreeNode


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        广度优先搜索
        时间击败18.86%，内存击败80.38%
        """
        if not root:
            return []
        result, queue = list(), list()
        queue.append(root)
        while queue:
            size = len(queue)
            curline = list()
            for i in range(size):
                curnode = queue.pop(0)
                curline.append(curnode.val)
                if curnode.left:
                    queue.append(curnode.left)
                if curnode.right:
                    queue.append(curnode.right)
            result.append(curline)
        return result