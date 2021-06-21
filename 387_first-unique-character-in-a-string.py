"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
哈希表
"""
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        使用哈希表存储频数
        第一次遍历：统计字符串每个字符出现的次数
        第二次遍历：找第一个只出现一次的字符
        时间击败36.91%，内存击败54.02%
        """
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1

    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        使用哈希表存储索引
        具体地，对于哈希映射中的每一个键值对，键表示一个字符，值表示它的首次出现的索引（如果该字符只出现一次）或者 -1（如果该字符出现多次）。
        当我们第一次遍历字符串时，设当前遍历到的字符为 c，
            如果 c 不在哈希映射中，我们就将 c 与它的索引作为一个键值对加入哈希映射中
            否则我们将 c 在哈希映射中对应的值修改为 −1。
        在第一次遍历结束后，我们只需要再遍历一次哈希映射中的所有值，找出第一个不重复字符的索引。
            如果哈希映射中的所有值均为 −1，我们就返回 -1。
        时间击败95.79%，内存击败55.55%
        """
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            return -1
        return first

    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        队列
        队列具有「先进先出」的性质，因此很适合用来找出第一个满足某个条件的元素。
        我们使用与方法二相同的哈希映射，并且使用一个额外的队列，按照顺序存储每一个字符以及它们第一次出现的位置。
        当我们对字符串进行遍历时，设当前遍历到的字符为 c
            如果 c 不在哈希映射中，我们就将 c 与它的索引作为一个二元组放入队尾，
            否则我们就需要检查队列中的元素是否都满足「只出现一次」的要求，即我们不断地根据哈希映射中存储的值（是否为 −1）选择弹出队首的元素，直到队首元素「真的」只出现了一次或者队列为空。
        在遍历完成后，如果队列为空，说明没有不重复的字符，返回 −1，否则队首的元素即为第一个不重复的字符以及其索引的二元组。
        在维护队列时，我们使用了「延迟删除」这一技巧。
            也就是说，即使队列中有一些字符出现了超过一次，但它只要不位于队首，那么就不会对答案造成影响，我们也就可以不用去删除它。
            只有当它前面的所有字符被移出队列，它成为队首时，我们才需要将它移除。
        时间击败70.11%，内存击败44.83%
        """
        position = dict()
        q = collections.deque()
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((s[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return -1 if not q else q[0][1]

if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    result = solution.firstUniqChar(s)
    print(result)
