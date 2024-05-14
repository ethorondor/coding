'''
2487 remove nodes from linked list
'''
#%%
class Solutions:
    def remove_nodes(self, head):
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        
        dummy = ListNode()
        curr = dummy
        while stack:
            curr.next = ListNode(stack.pop().val)
            curr = curr.next
        head = dummy.next
        curr = head
        pre = None
        while curr:
            _tmp = curr.next
            curr.next = pre
            pre = curr
            curr = _tmp
        return pre
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)
sln = Solutions()
h = sln.remove_nodes(head)
# %%
