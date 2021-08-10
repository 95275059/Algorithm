"""
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
解题思路：深度优先搜索 + 哈希表
    若将 target 当作树的根结点，我们就能从 target 出发，使用深度优先搜索去寻找与 target 距离为 k 的所有结点，即深度为 k 的所有结点。
    由于输入的二叉树没有记录父结点，为此，我们从根结点 root 出发，使用深度优先搜索遍历整棵树，同时用一个哈希表记录每个结点的父结点。
    然后从 target 出发，使用深度优先搜索遍历整棵树，除了搜索左右儿子外，还可以顺着父结点向上搜索。
    代码实现时，由于每个结点值都是唯一的，哈希表的键可以用结点值代替。
    此外，为避免在深度优先搜索时重复访问结点，递归时额外传入来源结点 from，在递归前比较目标结点是否与来源结点相同，不同的情况下才进行递归。
"""
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        时间击败100%，内存击败6.12%
        """
        parents = dict()
        result = list()

        def findParents(node):
            if node.left:
                parents.setdefault(node.left.val, node)
                findParents(node.left)
            if node.right:
                parents.setdefault(node.right.val, node)
                findParents(node.right)

        def findAns(node, fromnode, depth, k):
            if not node:
                return
            if depth == k:
                result.append(node.val)
                return
            if node.left != fromnode:
                findAns(node.left, node, depth+1, k)
            if node.right != fromnode:
                findAns(node.right, node, depth+1, k)
            if parents[node.val] != fromnode:
                findAns(parents[node.val], node, depth+1, k)

        # 从root出发DFS，记录每个结点的父结点
        parents.setdefault(root.val, None)
        findParents(root)
        # 从target出发DFS，寻找所有深度为k的结点
        findAns(target, None, 0, k)
        return result

