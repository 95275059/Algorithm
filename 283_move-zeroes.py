"""
283.移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
解题思路：非0的往前挪；双指针
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        双指针
        时间击败98.69%，内存击败92.41%
        """
        if not len(nums):
            return
        zero_num = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_num += 1
            else:
                nums[i-zero_num] = nums[i]
        for i in range(len(nums)-1, len(nums)-zero_num-1, -1):
            nums[i] = 0

    def moveZeroes1(self, nums):
        # 非零的往前挪
        # 时间击败82.37%，内存击败9.93%
        if not len(nums):
            return
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        双指针
        时间击败64.10%，内存击败5.00%
        """
        if not len(nums):
            return
        zero_num = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero_num += 1
            elif zero_num:
                nums[i-zero_num] = nums[i]
                nums[i] = 0

if __name__ == '__main__':
    solution = Solution()
    nums = [0,1,0,3,12]
    nums = []
    solution.moveZeroes(nums)
    print(nums)
