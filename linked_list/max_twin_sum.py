'''
2130 maximum twin sum of a linked list
'''
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(8)
head.next.next.next = ListNode(12)
class Solutions:
    def max_twin_sum(self, head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        res = 0
        while slow:
            res = max(res, prev.val+slow.val)
            prev = prev.next
            slow = slow.next
        return res
sln=Solutions()
sln.max_twin_sum(head)
# %%
