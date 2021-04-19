"""
83. 删除排序链表中的重复元素
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。
解题思路：普通遍历；递归
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        执行用时：28ms，击败70.92%
        内存消耗：13.3MB，击败5.19%
        普通遍历
        """
        if not head:
            return head
        point = head
        while point.next:
            if point.val == point.next.val:
                point.next = point.next.next
            else:
                point = point.next
        return head

    def deleteDuplicates1(self, head):
        """
        执行用时：40ms，击败9.18%
        内存消耗：13.1MB，击败33.29%
        递归，仍然是典型的牺牲时间换空间
        1.找终止条件
          当head指向链表只剩一个元素的时候，自然是不可能重复的，因此return
        2.想想应该返回什么值
          应该返回的自然是已经去重的链表的头节点
        3.每一步要做什么：
          宏观上考虑，此时head.next已经指向一个去重的链表了，
          而根据第二步，我应该返回一个去重的链表的头节点。
          因此这一步应该做的是判断当前的head和head.next是否相等，如果相等则说明重了，返回head.next，否则返回head
        """
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates1(head.next)
        if head.val == head.next.val:
            head = head.next
        return head