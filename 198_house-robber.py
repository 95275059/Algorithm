"""
198.打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
解题思路：动态规划
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间击败94.51%，内存击败81.26%
        """
        if not nums or not len(nums):
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        p1, p2 = max(nums[0], nums[1]), nums[0]
        for k in range(2, length):
            fn = max(p2 + nums[k], p1)
            p2 = p1
            p1 = fn
        return p1