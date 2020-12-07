from LinkedLIst import doubly_linked_list, Node
from datetime import datetime
from queclass import Queue
from datetime import date
import json

class Task:
    def __init__(self, description = "Initial one", date_time = datetime(1, 1, 1)):
        self.value = date_time
        self.description = description

    def __str__(self):
        return str(self.value)

class TaskList:
    writeFile = "writeFile.json"
    readFile = "readFile.json"
    def __init__(self):
        self.llist = doubly_linked_list()
        x = Task()
        self.llist.head = Node(x)
        self.llist.tail = Node(x)
        self.Queuelist = Queue(3)

        print("New tasklist initalized")
    def addatask(self, task):
        self.llist.addNodeLast(task)
        #self.Queuelist.append(task)





a = datetime(2012, 7, 1)
b = datetime(2016, 12, 4)
c = datetime(2018, 7, 15)
d = datetime(2020, 10, 1)
e = datetime(2024, 7, 7)
t1 = Task( "go to neighbor's house", a)
t2 = Task("do linear algebra", b)
t3 = Task("do electricity and magnetism", c)
t4 = Task("s", d)
t5 = Task("watch movie", e)
tasklist = TaskList()

tasklist.addatask(t1)
tasklist.addatask(t2)


i = tasklist.llist.head
if __name__ == '__main__':
    while True:
        if i:
            print(i.value)
            i = i.next
        else:
            break


