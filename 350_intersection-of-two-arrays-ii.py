"""
350.两个数组的交集II
给定两个数组，编写一个函数来计算它们的交集。

解题思路：哈希表，排序双指针
哈希表
    由于同一个数字在两个数组中都可能出现多次，因此需要用哈希表存储每个数字出现的次数。
    对于一个数字，其在交集中出现的次数等于该数字在两个数组中出现次数的最小值。
    首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，
    然后遍历第二个数组，对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。
    为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
    如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中。
    那么就无法高效地对 nums2 进行排序，因此推荐使用方法一而不是方法二。
    在方法一中，nums2 只关系到查询操作，因此每次读取 nums2 中的一部分数据，并进行处理即可。
"""
import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        排序后双指针比较
        时间击败80.24%，内存击败68.65%
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

    def intersect1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        哈希表
        时间击败67.74%，内存击败61.29%
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            count = m.get(num, 0)
            if count > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection

    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        哈希表
        时间击败80.24%，内存击败5.34%
        """
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return list(num.elements())

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    result = solution.intersect2(nums1, nums2)
    print(result)