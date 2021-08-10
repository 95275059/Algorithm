"""
743.网络延迟时间
有 n 个网络节点，标记为 1 到 n。
给你一个列表 times，表示信号经过 有向 边的传递时间。 
    times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
示例：
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
解题思路：本题需要用到单源最短路径算法 Dijkstra
现在让我们回顾该算法，其主要思想是贪心。
    将所有节点分成两类：已确定从起点到当前点的最短路长度的节点，以及未确定从起点到当前点的最短路长度的节点（下面简称「未确定节点」和「已确定节点」）。
    每次从「未确定节点」中取一个与起点距离最短的点，将它归类为「已确定节点」，并用它「更新」从起点到其他所有「未确定节点」的距离。
    直到所有点都被归类为「已确定节点」。
    用节点 A「更新」节点 B 的意思是，用起点到节点 A 的最短路长度加上从节点 A 到节点 B 的边的长度，去比较起点到节点 B 的最短路长度，如果前者小于后者，就用前者更新后者。这种操作也被叫做「松弛」。
    这里暗含的信息是：每次选择「未确定节点」时，起点到它的最短路径的长度可以被确定。
    可以这样理解，因为我们已经用了每一个「已确定节点」更新过了当前节点，无需再次更新（因为一个点不能多次到达）。而当前节点已经是所有「未确定节点」中与起点距离最短的点，不可能被其它「未确定节点」更新。所以当前节点可以被归类为「已确定节点」。
根据题意，从节点 k 发出的信号，到达节点 x 的时间就是节点 k 到节点 x 的最短路的长度。
因此我们需要求出节点 k 到其余所有点的最短路，其中的最大值就是答案。
若存在从 k 出发无法到达的点，则返回 -1。
下面的代码将节点编号减小了 1，从而使节点编号位于 [0,n−1] 范围。
"""
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        时间击败100%，内存击败50.85%
        """
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x-1][y-1] = time
        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1

if __name__ == '__main__':
    solution = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    times = [[1, 2, 1]]
    n = 2
    k = 1
    times = [[1, 2, 1]]
    n = 2
    k = 2
    times = [[1, 2, 1], [2, 1, 3]]
    n = 2
    k = 2
    times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
    n = 3
    k = 1
    print(solution.networkDelayTime(times, n, k))