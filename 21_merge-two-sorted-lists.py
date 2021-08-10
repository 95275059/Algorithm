"""
21.合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
测试用例：
l1 = [1,2,4], l2 = [1,3,4] : [1,1,2,3,4,4];
l1 = [], l2 = [] : [];
l1 = [], l2 = [0] : [0];
提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
解题思路：递归和非递归(迭代)两种，推荐递归
"""
import ListNode

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        迭代
        时间击败90.85%，内存击败51.97%
        """
        if not l1:
            return l2
        if not l2:
            return l1
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return prehead.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        递归
        时间击败75.93%，内存击败26.93%
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

l1 = [1,2,4]
l1 = []
l1 = []

node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
l1 = node1

l2 = [1,3,4]
l2 = []
l2 = [0]

node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)
l2 = node4

solution = Solution()
result = solution.mergeTwoLists(l1, l2)
while result:
    print(result.val)
    result = result.next
