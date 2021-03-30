"""
27.移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

测试用例：
nums = [3,2,2,3], val = 3 : 2; nums = [2,2]
nums = [0,1,2,2,3,0,4,2], val = 2 : 5; nums = [0,1,4,0,3]
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
解题思路：其实是双指针的题目
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
        return len(nums[:j])

nums = [3,2,2,3]
val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
solution = Solution()
print(solution.removeElement1(nums, val))