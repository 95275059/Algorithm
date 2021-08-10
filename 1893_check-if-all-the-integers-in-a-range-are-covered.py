"""
1893. 检查是否区域内所有整数都被覆盖
给你一个二维整数数组 ranges 和两个整数 left 和 right 。
每个 ranges[i] = [starti, endi] 表示一个从 starti 到 endi 的 闭区间 。
如果闭区间 [left, right] 内每个整数都被 ranges 中 至少一个 区间覆盖，那么请你返回 true ，否则返回 false 。
已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi ，那么我们称整数x被覆盖了。
提示：
1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
解题思路：差分数组
    为了判断某个区域内所有整数都被覆盖，我们需要对每个整数 x 计算覆盖该整数的区间数量，记作 cntx​。
    朴素的做法是，遍历 ranges 中的所有区间 [l,r]，将区间内每个整数的 cnt 值加上 1。
    遍历结束后，检查 [left,right] 内的每个整数的 cnt 值是否均大于 0，是则返回 true，否则返回 false。
    ranges 的长度为 n，需要计算的区间范围为 l，则上述做法的时间复杂度为 O(n⋅l)。
    下面介绍复杂度为 O(n+l) 的做法。
    我们可以用差分数组 diff 维护相邻两个整数的被覆盖区间数量变化量
    其中 diff[i] 对应覆盖整数 i 的区间数量相对于覆盖 i−1 的区间数量变化量。
    这样，当遍历到闭区间 [l,r] 时，l 相对于 l−1 被覆盖区间数量多 1，r+1 相对于 r 被覆盖区间数量少 1。
    对应到差分数组上，我们需要将 diff[l] 加上 1，并将 diff[r+1] 减去 1。
    在维护完差分数组 diff 后，我们遍历 diff 求前缀和得出覆盖每个整数的区间数量。
    下标 i 对应的被覆盖区间数量即为初始数量 0 加上 [1,i] 闭区间的变化量之和。
    在计算被覆盖区间数量的同时，我们可以一并判断 [left,right] 闭区间内的所有整数是否都被覆盖。
"""
class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        # 时间击败63.27%，内存击败77.55%
        diff = [0] * 52   # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True
