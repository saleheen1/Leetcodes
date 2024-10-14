from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = ListNode(val=head)
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        

s =Solution()
print(s.reverseList(head=[1,2,3,4,5]))