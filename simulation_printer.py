# import the 3 classes from the files and asign to Queue, Printer, Task instance
from Queue import Queue
from Printer import Printer
from Task import Task

#import a library
import random

# the main simulation function
def simulation(num_seconds, pages_per_minute):
    #instance of Printer and indicates pages per minute
    lab_printer = Printer(pages_per_minute)
    # instance of Queue
    print_queue = Queue()
    # initialize an array to register the delay
    waiting_times = []

    # loop initialize in zero and finish in 3600 seconds (one hour)
    for currentSecond in range(num_seconds):
        # call function new_print_task, if it's time to new task, then
        # instance a task and enqueue the task 
        if new_print_task():
            task = Task(currentSecond)
            print_queue.enqueue(task)
        # call method busy, if not busy and queue is not empty then dequeue
        # it means the printer is free and dequeue
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            # append a new value (wait_time) to the array waiting_times
            waiting_times.append(next_task.wait_time(currentSecond))
            # call method to begin new task
            lab_printer.start_next(next_task)
        # call tick method, calculate the remaining time less 1 second
        # if remaning time es equal or less than zero, then the task has finished
        lab_printer.tick()

    # calculate the average wait and print in console (10 times)
    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %d tasks remaining." % (average_wait, print_queue.size()))

# funtion to define task value's, generate a random (1 to 180),
# if the numbers is 180 then begins a new task
def new_print_task(): 
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

# here begins the program, simulate 10 students, around 1 hour, equal to 3600 seconds 
# and 5 page per minute to print
for i in range(10):
    simulation(3600, 5)