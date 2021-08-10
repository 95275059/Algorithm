"""
1743. 从相邻元素对还原数组
存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。
给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。
题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。
返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。
"""


class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        时间击败75%，内存击败50%
        """
        dic = dict()
        result = []
        for u, v in adjacentPairs:
            if u in dic:
                dic[u].append(v)
            else:
                dic.setdefault(u, [v])
            if v in dic:
                dic[v].append(u)
            else:
                dic.setdefault(v, [u])
        for key, value in dic.items():
            if len(dic[key]) == 1:
                result.append(key)
                break
        result.append(dic[result[0]][0])
        n = len(adjacentPairs) + 1
        for i in range(2, n):
            result.append(dic[result[i-1]][1] if dic[result[i-1]][0] == result[i-2] else dic[result[i-1]][0])
        return result

if __name__ == "__main__":
    solution = Solution()
    adjacentPairs = [[2,1],[3,4],[3,2]]
    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    print(solution.restoreArray(adjacentPairs))