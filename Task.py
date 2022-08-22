import random


class Task:
    # constructor, initialize time (current time), 
    # generate a random between 1 to 20, represent the number of pages
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    # method to get the timestamp
    def get_stamp(self):
        return self.timestamp
    # method to get the number of pages calculate in the constructor (1 to 20)
    def get_pages(self):
        return self.pages
    # method to calculate the time in queue
    def wait_time(self, current_time):
        return current_time - self.timestamp
