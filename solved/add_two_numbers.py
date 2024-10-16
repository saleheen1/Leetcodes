from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 =""
        n2 = ""

        while l1:
            n1 = n1+ str(l1.val)
            l1 = l1.next
        
        while l2:
            n2 = n2+ str(l2.val)
            l2 = l2.next

        summ = int(n1[::-1]) + int(n2[::-1]) ##reversing string with this [::-1]
        
        dummy_node = ListNode()
        current = dummy_node
        for v in reversed(str(summ)):
            new_node = ListNode(val= v)
            current.next = new_node
            current = new_node
        
        return dummy_node.next

        
        