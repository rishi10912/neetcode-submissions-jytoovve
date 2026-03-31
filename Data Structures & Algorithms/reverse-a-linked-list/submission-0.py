# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            # capture the orginal current node
            next_node = current.next
            # assign first node to NONE
            current.next = prev
            # flip the nodes
            prev = current
            # move forward and do the same
            current = next_node
        return prev
        