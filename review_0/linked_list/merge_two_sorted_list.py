'''
21 merge two sorted linked list
'''
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(5)

class Solutions:
    def merge_two_list(self, l1, l2):
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        return dummy.next 
sln = Solutions()
sln.merge_two_list(l1,l2)    
# %%
