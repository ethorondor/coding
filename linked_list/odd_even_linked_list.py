'''
328 odd even linked list
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
class Solutions:
    def odd_even_list(self, head):
        if not head:
            return None
        if not head.next or not head.next.next:
            return head
        odd = head
        even = odd.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
        
sln = Solutions()
h=sln.odd_even_list(head)
# %%
