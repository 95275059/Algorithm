"""
88.合并两个有序数组
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。
解题思路：直接合并后排序；双指针；逆向双指针
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        直接合并后排序
        时间击败99.79%，内存击败47.94%
        """
        nums1[m:] = nums2
        nums1.sort()

    def merge1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        双指针
        时间击败99.79%，内存击败22.27%
        """
        sorted = list()
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                sorted.append(nums1[i])
                i += 1
            else:
                sorted.append(nums2[j])
                j += 1
        if i < m:
            sorted += nums1[i:m]
        if j < n:
            sorted += nums2[j:n]
        nums1[:] = sorted

    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        逆向双指针
        方法二中，之所以要使用临时变量，是因为如果直接合并到数组num1中，num1中的元素可能会在取出之前被覆盖。
        那么如何直接避免覆盖nums1中的元素呢？
            观察可知，nums1的后半部分是空的，可以直接覆盖而不会影响结果。
            因此可以指针设置为从后向前遍历，每次取两者之中的较大者放进nums1的最后面。
            严格来说，在此遍历过程中的任意一个时刻，nums1数组中有 m−p1−1 个元素被放入 nums1的后半部，nums2数组中有 n−p2−1 个元素被放入 nums1的后半部，
            而在指针 p1的后面，nums1 数组有 m+n−p1−1 个位置。
            由于 m+n-p1-1 >= m+n−p1−1  等价于  p2 >= -1永远成立
            因此 p1 后面的位置永远足够容纳被插入的元素，不会产生 p1 的元素被覆盖的情况。
        时间击败87.46%，内存击败8.98%
        """
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if i >= 0:
            nums1[:k+1] = nums1[:i+1]
        if j >= 0:
            nums1[:k+1] = nums2[:j+1]

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge2(nums1, m, nums2, n)
    print(nums1)