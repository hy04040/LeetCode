class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = dummy = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return head.next

l1 = [1,2,4]
l2 = [1,3,4]
ll3 = ListNode(4, None)
ll2 = ListNode(3, ll3)
ll1 = ListNode(1, ll2)
l3 = ListNode(4, None)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
sol = Solution()
print(sol.mergeTwoLists(l1, ll1))


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = dummy = ListNode()
        while l1 or l2:
            if (l1 and not l2) or (l1 and l2 and l1.val <= l2.val):
                dummy.next = ListNode(l1.val)
                l1 = l1.next
            elif (not l1 and l2) or (l1 and l2 and l1.val > l2.val):
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            dummy = dummy.next
        return head.next
