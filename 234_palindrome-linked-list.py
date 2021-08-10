"""
234.回文链表
请判断一个链表是否为回文链表。
进阶：能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
import ListNode


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        将值复制到数组中后判断是否为回文数组
        时间击败67.61%，内存击败20.75%
        """
        li = list()
        cur = head
        while cur:
            li.append(cur.val)
            cur = cur.next
        return li == li[::-1]

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        快慢指针
        我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。
        比较完成后我们应该将链表恢复原样。
        该方法虽然可以将空间复杂度降到 O(1)，但是在并发环境下，该方法也有缺点。
        在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执行过程中链表会被修改。
        整个流程可以分为以下五个步骤：
            找到前半部分链表的尾节点。
            反转后半部分链表。
            判断是否回文。
            恢复链表。
            返回结果。
        时间击败41.07%，内存击败59.07%
        """
        if head is None:
            return True
        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
                break
            first_position = first_position.next
            second_position = second_position.next
        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast, slow = head, head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        newhead = None
        curhead = head
        while curhead is not None:
            curnode = curhead
            curhead = curhead.next
            curnode.next = newhead
            newhead = curnode
        return newhead