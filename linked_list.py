class Node:
    def __init__(self,data,next= None):
        self.data = data
        self.next = next
    
    # def  __str__(self):
    #     return str(self.data)
    


head = Node(data=1)
a = Node(data=2)
b = Node(data=3)

head.next = a
a.next = b

# print(head)
# print(head.next)
# print(a.next)
# print(b.next)

current = head

while current:
    print(current.data)
    current = current.next


def searchValue(start,value):
    current = start
    while current:
        if current.data == value:
            return True
        current = current.next
    
    return False

print(searchValue(start= head,value= 9))