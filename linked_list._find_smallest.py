class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        node = Node(data)
        if self.head != None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def find_smallest(self):
        current = self.head
        smallest = self.head
        while current != None:
            if current.data < smallest.data:
                smallest = current
                current = current.next
            else:
                current = current.next
        return smallest.data

    def __repr__(self) -> str:
        linked_list = []
        current = self.head
        while current != None:
            linked_list.append(f'|{current.data}|')
            current = current.next
        return ' -> '.join(linked_list)
        

linked_list = LinkedList()
linked_list.add(9)
linked_list.add(2)
linked_list.add(3)
linked_list.add(11)
linked_list.add(7)
print(linked_list)
print(f'Smallest: {linked_list.find_smallest()}')


            