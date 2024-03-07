'''
2095 delete middle node of a linked list
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
    def del_middle_node(self, head):
        if not head.next:
            return None 
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
sln = Solutions()
sln.del_middle_node(head)
# %%
