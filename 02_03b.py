from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority
    
    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

task_queue = deque()

def add_task (task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_tasks():
    for t in task_queue:
        print(t.taskDesc)

# def print_items(items):
#     return print(items)

# def add_items(items, new_item):
#     d = deque(items)
#     d.append(new_item)
#     print_items(d)

# def add_priority(items, priority_item):
#     d = deque(items)
#     d.appendleft(priority_item)
#     print_items(d)

def main():
    #add code here
    # items = ["STA001", "ENT003", "DES004"]
    # print_items(items)
    # add_items(items, "STA004")
    # add_priority(items, "DES005")
    add_task(Task("Make List"))
    add_task(Task("Make Breakfast"))
    add_task(Task("Respond to Email", True))
    print_tasks()
    do_task()
    print_tasks()
    return

if __name__ == "__main__":
    main()