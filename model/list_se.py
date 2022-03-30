from .node import Node

class ListSE:
    def __init__(self):
        self.head= None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            #posicionados en el ultimo
            temp.next = Node(data)
