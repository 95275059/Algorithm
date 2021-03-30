"""
35.搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
测试用例：
[1,3,5,6],5 : 2
[1,3,5,6],2 : 1
[1,3,5,6],7 : 4
[1,3,5,6],0 : 0
解题思路：
二分法
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            middle = int((i + j) / 2)
            if nums[middle] > target:
                j = middle - 1
            elif nums[middle] == target:
                return middle
            else:
                i = middle + 1
        return i

    def searchInsert1(self, nums, target):
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low

if __name__ == '__main__':
   solution = Solution()
   nums = [1, 3, 5, 6]
   target = 2
   print(solution.searchInsert1(nums, target))