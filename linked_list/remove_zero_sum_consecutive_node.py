'''
1171 remove zero sum consecutive nodes from linked list
'''
#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)
class Solutions:
    def remove_zero_sum(self, head):
        nums = []
        curr = head
        seen = set([0])
        total = 0
        while curr:
            nums.append(curr.val)
            total += curr.val
            if total in seen:
                curr_total = total
                total -= nums[-1]
                nums.pop()
                while total != curr_total:
                    seen.remove(total)
                    total -= nums[-1]
                    nums.pop()
            else:
                seen.add(total)
            curr = curr.next
        dummy = ListNode
        curr=dummy
        for num in nums:
            curr.next = ListNode(num)
            curr=curr.next 
        return dummy.next
sln = Solutions()
h = sln.remove_zero_sum(head)
        
# %%
