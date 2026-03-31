"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_dict = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            my_dict[curr] = copy
            curr = curr.next
        #Second Pass
        curr = head
        while curr:
            copy = my_dict[curr]
            copy.next = my_dict[curr.next]
            copy.random = my_dict[curr.random]
            curr = curr.next

        return my_dict[head]