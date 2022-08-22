class Queue:
    # initialize the queue
    def __init__(self):
        self.items = []

    # method to evaluate is empty the queue
    def is_empty(self):
        return self.items == []

    # method to append a new item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # method to dequeue
    def dequeue(self):
        return self.items.pop()

    # method to calculate the number of item in the queue
    def size(self):
        return len(self.items)