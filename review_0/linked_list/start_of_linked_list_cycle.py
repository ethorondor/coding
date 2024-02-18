'''
find the start of a linked list cycle
'''
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = head.next.next.next
class solutions:
    def start_linked_list_cycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow_2 = head
        while slow:
            slow_2 = slow_2.next
            slow = slow.next
            if slow==slow_2:
                return slow
            
sln = solutions()
sln.start_linked_list_cycle(head)
# %%
