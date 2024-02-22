'''
206 reverse linked list
'''
#%%
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

class solutions:
    def reverse_linked_list(self, head):
        curr = head
        pre = None
        while curr:
            _temp = curr.next
            curr.next = pre
            pre = curr
            curr = _temp
        return pre
sln = solutions()
sln.reverse_linked_list(head=head)
# %%
