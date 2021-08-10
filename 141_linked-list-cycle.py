"""
141.环形链表
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
进阶：你能用 O(1)（即，常量）内存解决此问题吗？
"""
import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        哈希表
        时间击败78.12%，内存击败12.87%
        """
        map = set()
        while head:
            if head in map:
                return True
            else:
                map.add(head)
            head = head.next
        return False

    def hasCycle1(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        快慢指针
        利用了Floyd 判圈算法，又称龟兔赛跑算法
            假想「乌龟」和「兔子」在链表上移动，「兔子」跑得快，「乌龟」跑得慢。
            当「乌龟」和「兔子」从链表上的同一个节点开始移动时，如果该链表中没有环，那么「兔子」将一直处于「乌龟」的前方；
            如果该链表中有环，那么「兔子」会先于「乌龟」进入环，并且一直在环内移动。
            等到「乌龟」进入环时，由于「兔子」的速度快，它一定会在某个时刻与乌龟相遇，即套了「乌龟」若干圈。
        具体地，我们定义两个指针，一快一慢。
        慢指针每次只移动一步，而快指针每次移动两步。
        初始时，慢指针在位置 head，而快指针在位置 head.next。
        这样一来，如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。
        为什么我们要规定初始时慢指针在位置 head，快指针在位置 head.next，而不是两个指针都在位置 head（即与「乌龟」和「兔子」中的叙述相同）？
            1.观察下面的代码，我们使用的是 while 循环，循环条件先于循环体。
            由于循环条件一定是判断快慢指针是否重合，如果我们将两个指针初始都置于 head，那么 while 循环就不会执行。
            2.当然，我们也可以使用 do-while 循环。
            此时，我们就可以把快慢指针的初始值都置为 head。
        时间击败60.77%，内存击败42.25%
        """
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


