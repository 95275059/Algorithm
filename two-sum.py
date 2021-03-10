"""
1.两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

测试用例：
nums = [2,7,11,15], target = 9 : [0,1];
nums = [3,2,4], target = 6 : [1,2];
nums = [3,3], target = 6 : [0,1];

解题思路：动态哈希表
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))