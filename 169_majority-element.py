"""
169.多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序后遍历
        时间击败97.05%，内存击败26.77%
        """
        nums.sort()
        count = 0
        nown = None
        length = len(nums)/2
        for n in nums:
            if nown is None:
                nown = n
                count += 1
            elif nown == n:
                count += 1
                if count > length:
                    return nown
            else:
                count = 1
                nown = n
        return nown

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序
        如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为 ⌊ n/2 ⌋ 的元素（下标从 0 开始）一定是众数。
        时间击败90.77%，内存击败82.40%
        """
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Boyer-Moore 投票算法
        如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。
        Boyer-Moore 算法的详细步骤：
            我们维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；
            我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：
                如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
                如果 x 与 candidate 不等，那么计数器 count 的值减少 1。
            在遍历完成后，candidate 即为整个数组的众数。
        时间击败90.77%，内存击败31.39%
        O(n), O(1)
        """
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if candidate == n else -1
        return candidate