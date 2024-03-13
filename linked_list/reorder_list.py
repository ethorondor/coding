'''
143 reorder list
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
head.next.next.next.next = ListNode(5)
class Solutions:
    def reorder_list(self, head):
        # find the middle of the linked list
        if not head or not head.next or not head.next.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = slow.next
        slow.next = None
        # now reverse tail
        prev = None
        while tail:
            _tmp = tail.next
            tail.next = prev
            prev = tail
            tail = _tmp
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
        return head
            
sln = Solutions()
h = sln.reorder_list(head)
# %%
