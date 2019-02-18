"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""

class Solution1:
    def addTwoNumbers(self, l1, l2):
        def _get_list(l):
            res = []
            while l:
                res.append(l.val)
                l = l.next
            return res
        
        def _get_num(l):
            key = 1
            result = 0
            for i in l:
                result += key * i
                key *= 10
            return result

        l1, l2 = _get_list(l1), _get_list(l2)
        # reduce(lambda m, n: m + n, map(lambda x: x * 10 ** l1.index(x), l1))
        result_l1 = _get_num(l1)  # TODO
        result_l2 = _get_num(l2)
        result = result_l1 + result_l2
        print(result)
        head = tmp = ListNode(0)
        while 1:
            val = result % 10
            result //= 10
            tmp.next = ListNode(val)
            tmp = tmp.next
            if not result:
                break
        return head.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        pre = head
        digit = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            val = digit + x + y
            digit = val // 10
            pre.next = ListNode(val % 10)
            pre = pre.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if digit:
            pre.next = ListNode(1)
        return head.next


# python版单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def string_to_list_node(l):
    head = ListNode(0)
    ptr = head
    for x in l:
        ptr.next = ListNode(x)
        ptr = ptr.next
    ptr = head.next
    return ptr


def main():
    s = Solution()
    l1 = string_to_list_node([2,4,3])
    l2 = string_to_list_node([5,6,4])
    # l1 = string_to_list_node([1, 2])
    # l2 = string_to_list_node([1, 2, 3])
    # l1 = string_to_list_node([])
    # l2 = string_to_list_node([1, 2, 3])
    # l1 = string_to_list_node([0])
    # l2 = string_to_list_node([0])
    
    s.addTwoNumbers(l1, l2)


if __name__ == "__main__":
    main()
