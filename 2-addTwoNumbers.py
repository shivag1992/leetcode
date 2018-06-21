# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        carry = 0
        result = None
        
        while((t1 is not None) or (t2 is not None)):
            val1 = t1.val if t1 is not None else 0
            val2 = t2.val if t2 is not None else 0
            t = val1 + val2 + carry
            carry = t / 10
            t = t % 10
            newNode = ListNode(t)
            if result is None:
                result = newNode
                last = result
            else:
                last.next = newNode
                last = last.next
            if t1 is not None:
                t1 = t1.next
            if t2 is not None:
                t2 = t2.next
        if carry is not 0:
            last.next = ListNode(carry)
            last = last.next
        return result
