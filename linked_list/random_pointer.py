'''
138 copy list with random pointer
'''
class Solutions:
    def copy_list(self, head):
        old_to_copy = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
        return old_to_copy[head]