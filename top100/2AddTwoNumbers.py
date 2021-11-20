# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = curr = ListNode()
        carry = 0
        while l1 or l2:
            l1_val = l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            curr.next = ListNode(val)
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(carry)
        return head.next

l3 = ListNode(3,None)
l2 = ListNode(4,l3)
l1 = ListNode(2,l2) 
ll3 = ListNode(4,None)
ll2 = ListNode(6,ll3)
ll1 = ListNode(5,ll2)    
sol = Solution()
print(sol.addTwoNumbers(l1, ll1))




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = dummy = ListNode()
        add = 0
        while l1 or l2:
            l1_val = l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            val = l1_val + l2_val + add
            add = val // 10
            dummy.next = ListNode(val % 10)
            dummy = dummy.next
        if add == 1:
            dummy.next = ListNode(1)
        return head.next