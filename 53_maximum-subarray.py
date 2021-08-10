"""
53.最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
解题思路：除了一般解法，还有分治法
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        暴力划窗，复杂度O(n^2)
        """
        if not nums:
            return None
        else:
            maxnum = nums[0]
            for i in range(len(nums)):
                num = nums[i]
                if num > maxnum:
                    maxnum = num
                for j in range(i + 1, len(nums)):
                    num += nums[j]
                    if num > maxnum:
                        maxnum = num
            return maxnum

    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划:status[n+1] = max(status[n],status[n] + nums[n+1])
        定义一个函数f(n)，以第n个数为结束点的子数列的最大和，存在一个递推关系f(n) = max(f(n-1) + A[n], A[n]);
        将这些最大和保存下来后，取最大的那个就是，最大子数组和。因为最大连续子数组 等价于 最大的以n个数为结束点的子数列和
        """
        res = -float('inf')
        if not len(nums):
            return None
        func_n = -1
        for i in range(len(nums)):
            func_n = max(nums[i], func_n + nums[i])
            res = max(func_n, res)
        return res

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    nums = [0]
    nums = [-100000]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray1(nums))