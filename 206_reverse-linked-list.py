"""
206.翻转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
解题思路：栈；双链表
"""
import ListNode
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        栈
        时间击败43.69%，内存击败71.38%
        """
        if not head:
            return head
        stack = list()
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        newhead = stack.pop()
        cur = newhead
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return newhead

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        双链表
        双链表求解是把原链表的结点一个个摘掉，每次摘掉的链表都让他成为新的链表的头结点，然后更新新链表。
        时间击败96.12%，内存击败63.76%
        """
        if not head:
            return head
        newhead = None
        while head:
            curnode = head
            head = head.next
            curnode.next = newhead
            newhead = curnode
        return newhead