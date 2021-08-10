"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
解题思路：
在对链表进行操作时，一种常用的技巧是添加一个哑节点（dummy node），它的 next 指针指向链表的头节点。
这样一来，我们就不需要对头节点进行特殊的判断了。
且，获取head必须通过dummy.next获取，因为如果有可能其实head已经为空了，但head指向的还是旧的head
    1.两次遍历，第一计算链表长度，第二次进行删除
    2.栈
    3.快慢双指针
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        时间击败82.06%，内存击败51.60%
        """
        j = -n
        node, tag = head, None
        while node:
            j += 1
            if j<1:
                pass
            elif j==1:
                tag = head
            else:
                tag = tag.next
            node = node.next
        if tag:
            tag.next = tag.next.next
        else:
            head = head.next
        return head

    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        栈
        在遍历链表的同时将所有节点依次入栈
        根据栈「先进后出」的原则，我们弹出栈的第 n 个节点就是需要删除的节点，并且目前栈顶的节点就是待删除节点的前驱节点。
        这样一来，删除操作就变得十分方便了。
        时间击败82.13%，内存击败29.58%
        """
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        快慢双指针
        由于我们需要找到倒数第 n 个节点，因此我们可以使用两个指针 first 和 second 同时对链表进行遍历,并且 first 比 second 超前 nn 个节点。
        当 first 遍历到链表的末尾时，second 就恰好处于倒数第 n 个节点。
        具体地，初始时 first 和 second 均指向头节点。我们首先使用 first 对链表进行遍历，遍历的次数为 n。
        此时，first 和 second 之间间隔了 n−1 个节点，即 first 比 second 超前了 n 个节点。
        在这之后，我们同时使用 first 和 second 对链表进行遍历。
        当 first 遍历到链表的末尾（即 first 为空指针）时，second 恰好指向倒数第 n 个节点。
        如果我们能够得到的是倒数第 n 个节点的前驱节点而不是倒数第 n 个节点的话，删除操作会更加方便。
        因此我们可以考虑在初始时将 second 指向哑节点，其余的操作步骤不变.
        这样一来，当 first 遍历到链表的末尾时，second 的下一个节点就是我们需要删除的节点。
        时间击败94.77%，内存击败41.06%
        """
        dummy = ListNode(0, head)
        first, second = head, dummy
        for i in range(n):
            first = first.next
        while first:
            first, second = first.next, second.next
        second.next = second.next.next
        return dummy.next