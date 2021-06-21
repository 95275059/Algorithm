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
解题思路：递归和非递归两种，推荐递归
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(None)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return head.next

    @classmethod
    def mergeTwoLists1(cls, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = cls.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = cls.mergeTwoLists(l1, l2.next)
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
