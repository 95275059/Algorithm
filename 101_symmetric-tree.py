"""
101.对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的
进阶：你可以运用递归和迭代两种方法解决这个问题吗？
解题思路：递归，迭代
注意：中序遍历是回文串不代表原树是对称的，比如[1,2,null,1]这样的。
"""
import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        递归
        时间击败85.26%，内存击败10.62%
        """
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            return (left.val != right.val) and \
                   self.helper(left.left, right.right) and \
                   self.helper(left.right, right.left)
        else:
            return False

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        迭代
        「方法一」中我们用递归的方法实现了对称性的判断，那么如何用迭代的方法实现呢？
        首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
        初始化时我们把根节点入队两次。每次提取两个结点并比较它们的值（队列中每两个连续的结点应该是相等的，而且它们的子树互为镜像）
        然后将两个结点的左右子结点按相反的顺序插入队列中。
        当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续结点）时，该算法结束。
        时间击败78%，内存击败82%
        """
        return self.check(root, root)

    def check(self, left, right):
        queue = list()
        queue.append(left)
        queue.append(right)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if (not left or not right) or (left.val != right.val):
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True