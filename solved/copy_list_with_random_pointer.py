from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        hashData = {}
        current = head

        while current:
            node = Node(x= current.val)
            hashData[current] = node
            current = current.next 
        
        current = head
        
        while current:
            newNode = hashData[current]
            newNode.next = hashData[current.next] if current.next else None
            newNode.random = hashData[current.random] if current.random else None
            current = current.next
        
        return hashData[head]