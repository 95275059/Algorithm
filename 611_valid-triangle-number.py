"""
611.有效三角形的个数
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
解题思路：排序加二分查找
    我们可以将数组 nums 进行升序排序，随后使用二重循环枚举 a 和 b。
    设 a=nums[i],b=nums[j]，为了防止重复统计答案，我们需要保证 i<j。
    剩余的边 c 需要满足 c<nums[i]+nums[j]
    我们可以在 [j+1,n−1] 的下标范围内使用二分查找（其中 n 是数组 nums 的长度），找出最大的满足 nums[k]<nums[i]+nums[j] 的下标 k
    这样一来，在 [j+1,k] 范围内的下标都可以作为边 c 的下标，我们将该范围的长度 k−j 累加入答案。
    注意到题目描述中 nums 包含的元素为非负整数，即除了正整数以外，nums 还会包含 0。
        但如果我们将 nums 进行升序排序，那么在枚举 a 和 b 时出现了 0，那么 nums[i] 一定为 0。
        此时，边 c 需要满足 c<nums[i]+nums[j]=nums[j]，而下标在 [j+1,n−1] 范围内的元素一定都是大于等于 nums[j] 的，因此二分查找会失败。
        若二分查找失败，我们可以令 k=j，此时对应的范围长度 k−j=0，我们也就保证了答案的正确性。
    当枚举完成后，我们返回累加的答案即可。
"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间击败5.71%，内存击败77.14%
        """
        length = len(nums)
        if length < 3:
            return 0
        nums.sort()
        result = 0
        for i in range(0, length):
            for j in range(i+1, length):
                left, right, k = j+1, length-1, j
                while left<=right:
                    mid = left + (right - left) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid+1
                    else:
                        right = mid-1
                result += k-j
        return result