"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 遍历所有链表的元素，排序，重新生成链表
class Solution:
    def mergeTwoLists(self, l1, l2):
        res = []
        while l1:
            res.append(l1.val)
            l1 = l1.next
        while l2:
            res.append(l2.val)
            l2 = l2.next
        
        res = sorted(res)
        l = t = ListNode(0)
        for i in res:
            x = ListNode(i)
            t.next = x
            t = t.next
        return l.next


# 遍历两个链表，每次判断移动一个链表的指针,另一个链表指针不移动
class Solution:
    def mergeTwoLists(self, l1, l2):
        l = x = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                x.next = l1
                l1 = l1.next
            else:
                x.next = l2
                l2 = l2.next
            x = x.next
        if l1:
            x.next = l1
        if l2:
            x.next = l2
        return l.next


def get_list(d):
    l = ListNode(0)
    t = l
    for i in d:
        x = ListNode(i)
        t.next, t = x, x
    return l.next


def traverse(l):
    t = l
    while t:
        print(t.val)
        t = t.next


def main(): 
    l1, l2 = get_list([1, 2, 4]), get_list([1, 3, 4]) 
    # l1, l2 = get_list([1, 2, 4]), get_list([1, 3]) 
    # l1, l2 = get_list([4]), get_list([1, 3]) 

    s = Solution()
    res = s.mergeTwoLists(l1, l2)  # 1->2->4, 1->3->4
    traverse(res)


if __name__ == "__main__":
    main()
