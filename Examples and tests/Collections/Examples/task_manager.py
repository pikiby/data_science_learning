tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

from collections import defaultdict, deque

def task_manager(tasks):
    task_defaultdict = defaultdict(deque)
    for task in tasks:
        if task[3]:
            task_defaultdict[task[1]].appendleft(task[0])
        else:
            task_defaultdict[task[1]].append(task[0])
    return task_defaultdict

print (task_manager(tasks))