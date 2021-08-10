"""
104.二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
解题思路:深度优先搜索;广度优先搜索
    如果我们知道了左子树和右子树的最大深度 l 和 r，那么该二叉树的最大深度即为 max(l,r)+1
    而左子树和右子树的最大深度又可以以同样的方式进行计算。
"""
import TreeNode


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        深度优先搜索
        具体而言，在计算当前二叉树的最大深度时，可以先递归计算出其左子树和右子树的最大深度，然后在 O(1) 时间内计算出当前二叉树的最大深度。
        递归在访问到空节点时退出。
        时间击败57.07%，内存击败70.85%
        """
        if not root:
            return 0
        else:
            left_len = self.maxDepth(root.left)
            right_len = self.maxDepth(root.right)
            return max(left_len, right_len) + 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        广度优先搜索
        我们也可以用「广度优先搜索」的方法来解决这道题目，但我们需要对其进行一些修改
        此时我们广度优先搜索的队列里存放的是「当前层的所有节点」。
        每次拓展下一层的时候，不同于广度优先搜索的每次只从队列里拿出一个节点，我们需要将队列里的所有节点都拿出来进行拓展
        这样能保证每次拓展完的时候队列里存放的是当前层的所有节点，即我们是一层一层地进行拓展
        最后我们用一个变量 ans 来维护拓展的次数，该二叉树的最大深度即为 ans。
        时间击败31.93%，内存击败34.49%
        """
        if not root:
            return 0
        queue = list()
        queue.append(root)
        result = 0
        while queue:
            result += 1
            length = len(queue)
            for i in range(length):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
        return result