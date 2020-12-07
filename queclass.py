class Queue:

    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to front element in the queue if present
        self.rear = -1  # rear points to last element in the queue
        self.count = 0  # current size of the queue

    # Function to remove front element from the queue
    def pop(self):
        # check for queue underflow
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating Program.")
            exit(1)

        print("Removing element...", self.q[self.front])

        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1

    # Function to add a value to the queue
    def append(self, value):
        # check for queue overflow
        if self.isFull():
            print("OverFlow!! Terminating Program.")
            exit(1)

        print("Inserting element...", value)

        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1

    # Function to return front element in the queue
    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating Program.")
            exit(1)

        return self.q[self.front]

    # Function to return the size of the queue
    def size(self):
        return self.count

    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self.capacity

    def __iter__(self):
        return (t for t in self.q)

if __name__ == '__main__':
    q = Queue(2)
    q.append(10)
    q.append(12)
    for i in q:
        print(i)