class Printer:
    # constructor, initialize page per minute, 
    # current task state and remaning time equal zero
    def __init__(self, ppm):
        self.page_rate = ppm 
        self.current_task = None
        self.time_remaining = 0
    # this method evaluate current task state, calculate the remaining time less 1 second
    # if remaning time es equal or less than zero, then the task has finished
    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
    # this method evaluate if the task has finished and return true(finished) or false (busy) 
    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False
    # this method create a new task and calculate the remaining time to finish that task
    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.page_rate
