"""
581.最短无序连续子数组
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
示例：
    输入：nums = [2,6,4,8,10,9,15]
    输出：5
    解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
解题思路：
排序
    我们将给定的数组 nums 表示为三段子数组拼接的形式，分别记作 numsA，numsB，numsC。
    当我们对 numsB进行排序，整个数组将变为有序。
    换而言之，当我们对整个序列进行排序，numsA 和 numsC 都不会改变。
    本题要求我们找到最短的 numsB ，即找到最大的 numsA和 numsC的长度之和。
    因此我们将原数组 nums 排序与原数组进行比较，取最长的相同的前缀为 numsA，取最长的相同的后缀为numsC，这样我们就可以取到最短的 numsB
    特别地，当原数组有序时，numsB的长度为 0，我们可以直接返回结果。
一次遍历
    假设 numsB在 nums 中对应区间为 [left,right]。
    注意到 numsB和 numsC中任意一个数都大于等于 numsA中任意一个数。
    最小元素左边比它大的元素都要参与排序，最大元素右边比它小的元素都要调整
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序
        时间击败94.78%，内存击败27.71%
        """
        length = len(nums)

        def issorted():
            for i in range(length-1):
                if nums[i] > nums[i+1]:
                    return False
            return True

        if issorted():
            return 0
        nums_copy = nums[:]
        nums_copy.sort()
        left_index = 0
        while nums[left_index] == nums_copy[left_index]:
            left_index += 1
        right_index = length - 1
        while nums[right_index] == nums_copy[right_index]:
            right_index -= 1
        return right_index - left_index + 1

    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        一次遍历
        时间击败87.15%，内存击败35.74%
        """
        length = len(nums)
        minn, left = float('inf'), -1
        maxn, right = float('-inf'), -1
        for i in range(length):
            if minn < nums[length - i - 1]:
                left = length - i - 1
            else:
                minn = nums[length - i - 1]
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
        return 0 if right == -1 else right - left + 1