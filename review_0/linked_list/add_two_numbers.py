'''
2 add two numbers
'''
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

class solutions:
    def add_two_nums(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            val = val_1 + val_2 + carry
            carry = val//10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
sln = solutions()
ans = sln.add_two_nums(l1,l2)

# %%
