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
        dummy = ListNode()
        curr = dummy
        while prev and head:
            curr.next = ListNode(head.val)
            curr = curr.next
            curr.next = ListNode(prev.val)
            curr = curr.next
            head = head.next
            prev = prev.next
        if head:
            curr.next = head
            
        return dummy.next
            
sln = Solutions()
h = sln.reorder_list(head)
# %%
