class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        new_node.next = None

    def push(self,value):
        new_node = Node(value)
        temp = self.head
        if self.head is None:
            self.head = new_node 
            new_node.next = None
            return True
        self.head = new_node
        new_node.next = self.head
        return True
    def pop(self):
        temp = self.head
        if self.head is None:
            return None
        self.head = temp.next
        temp.next = None
        return temp
mystack = Stack(3)
print(mystack.head.value)
mystack.push(5)
mystack.pop()
print(mystack.head.value)
