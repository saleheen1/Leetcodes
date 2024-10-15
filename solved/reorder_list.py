from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        node = head
        q = deque()

        while True:
            node = node.next
            if not node:
                break
            q.append(node)
        
        while q:
            if head:
                temp = q.pop()
                head.next = temp
                head = head.next
            
            if q:
                temp = q.popleft()
                head.next = temp
                head = head.next
        
        head.next = None