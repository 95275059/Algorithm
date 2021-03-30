"""
26.删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

测试用例：
nums = [1,1,2] : 2; [1,2]
nums = [0,0,1,1,1,2,2,3,3,4] : 5; [0, 1, 2, 3, 4]
解题思路：正序遍历和倒序遍历都可
倒着来，比较最后两个数字，若相等，则删除掉后者。这种方法不用考虑删除数字后数组的长度。但是内存消耗更大
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i + 1 >= len(nums):
                break
            elif nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)

    def removeDuplicates1(self, nums):
        length = len(nums) - 1
        if length > 0:
            for i in range(length):
                if nums[length-i] == nums[length-i-1]:
                    del nums[length-i-1]
        return len(nums)


nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,3]
solution = Solution()
print(solution.removeDuplicates1(nums))