"""
1104.二叉树寻路
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。
给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。
示例：
输入：label = 14
输出：[1,3,4,14]
输入：label = 26
输出：[1,2,6,10,26]
"""
import math

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        时间击败70%，内存击败30%
        """
        if label == 1:
            return [1]
        row = int(math.ceil(math.log(label+1, 2)))
        result = [label]
        for i in range(row-1, 1, -1):
            sum = 2**(i-1) + 2**(i) - 1
            label = sum - int(label / 2)
            result.append(label)
        result.append(1)
        return result[::-1]


if __name__ == "__main__":
    solution = Solution()
    label = 26
    print(solution.pathInZigZagTree(label))