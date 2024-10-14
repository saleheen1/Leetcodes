class Node:
    def __init__(self, data, next = None):
        self.value = data
        self.next = next



head = Node(data= 1)
a = Node(data=2)
b = Node (data= 3)
c = Node (data= 4)

head.next = a 
a.next = b 
b.next = c


current = head

while current:
    print(current.value)
    current = current.next


def searchValue(start,v):
    current = start
    while current:
       if current.value == v:
           return True
       current = current.next
    
    return False

print (searchValue(start=head,v= 3))





