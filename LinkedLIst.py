from datetime import datetime


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class doubly_linked_list:

    def __init__(self, val=0):
        self.zero = datetime(1, 1, 1)
        val = self.zero
        self.head = Node(val)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeLast(self, val):
        if self.head.value == self.zero:
            self.head.value = val.value
            return

        current = self.head
        while current.next != None:
            current = current.next
        newNode = Node(val)
        current.next = newNode
        newNode.prev = current
        self.tail = newNode

    def insertNode(self, val, newVal):
        if self.tail.value == val.value:
            self.addNodeLast(newVal)
        elif self.head.value == val.value:
            newNode = Node(newVal)
            newNode.next = self.head.next
            self.head.next = newNode
        else:
            current = self.head.next
            while current.value.value != val.value:
                current = current.next
            newNode = Node(newVal)
            newNode.next = current.next
            current.next = newNode

    def insert_node_when_smaller(self, val):
        if val.value > self.head.value.value:
            if self.head.value.value == self.zero:
                newNode = Node(val)
                self.head.value = val
                return
            newNode = Node(val)
            newNode.next = self.head
            newNode.next.prev = newNode
            self.head = newNode
            return

        if val.value < self.tail.value.value:
            if self.tail.value.value == self.zero:
                newNode = Node(val)
                self.tail.value = val
                return

            self.addNodeLast(val)
            return


        else:
            i = self.head
            while i.value.value > val.value:
                if i.next:
                    i = i.next
                else:
                    break
            self.insertNode(i.prev.value, val)

    def removeNode(self, val):
        if self.head.value == val:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.value == val:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head.next
            while current.value != val:
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev

    def showReverse(self):
        current = self.tail
        while current != None:
            print(current.value)
            current = current.prev

    def show(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next


if __name__ == '__main__':

    dl = doubly_linked_list()
    dl.insert_node_when_smaller(4)
    dl.insert_node_when_smaller(1)
    dl.insert_node_when_smaller(5)
    dl.insert_node_when_smaller(7)
    dl.insert_node_when_smaller(6)
    dl.insert_node_when_smaller(2)
    dl.insert_node_when_smaller(10)
    dl.insert_node_when_smaller(8)

    i = dl.head
    while True:
        if i:
            print(i.value)
            i = i.next
        else:
            break
