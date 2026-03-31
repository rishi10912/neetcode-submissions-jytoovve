# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # check edge case
        if not head and not head.next: return
        
        # Find middle 
        hare = tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
        # tortoise now at start of second half of list 
        current = tortoise.next
        tortoise.next = None # cuts the list in half
        prev = None

        # reverse second list
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # now prev is reverse second half of list 
        first = head
        second = prev

        #Implement zip()
        while second:
            tmp1 = first.next
            tmp2= second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        





