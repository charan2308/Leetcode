import heapq
from collections import deque

# Global data structures
priority_queue = []  # Min-heap for managing priorities
task_map = {}  # Maps priority to a deque of tasks with that priority
size = 0  # Number of tasks

def add_task(task_name, priority, execution_time):
    global size
    if priority not in task_map:
        task_map[priority] = deque()
    task_map[priority].append((task_name, execution_time))
    heapq.heappush(priority_queue, -priority)  # Use negative for max-heap simulation
    size += 1

def dequeue_task():
    global size
    while priority_queue:
        priority = -heapq.heappop(priority_queue)  # Get highest priority
        if priority in task_map and task_map[priority]:
            task_name, execution_time = task_map[priority].popleft()
            size -= 1
            if not task_map[priority]:
                del task_map[priority]
            return task_name
    return "Queue is empty"

def execute_task():
    global size
    while priority_queue:
        priority = -priority_queue[0]  # Peek at the highest priority
        if priority in task_map and task_map[priority]:
            task_name, execution_time = task_map[priority].popleft()
            if not task_map[priority]:
                heapq.heappop(priority_queue)  # Remove priority from heap if no tasks left
                del task_map[priority]
            size -= 1
            return f"Executed {task_name}"
    return "Queue is empty"

def get_size():
    return size

def task_scheduler(n, task_names, priorities, execution_times, m, queries):
    global priority_queue, task_map, size
    # Initialize data structures
    priority_queue = []
    task_map = {}
    size = 0
    
    # Adding tasks
    for i in range(n):
        add_task(task_names[i], priorities[i], execution_times[i])
    
    results = []
    
    # Processing queries
    for query in queries:
        if query[0] == 1:  # Dequeue
            results.append(dequeue_task())
        elif query[0] == 2:  # Execute
            results.append(execute_task())
        elif query[0] == 3:  # Size
            results.append(str(get_size()))
    
    return results

# Example usage:
n = 5
task_names = ['A', 'B', 'C', 'D', 'E']
priorities = [2, 1, 3, 2, 1]
execution_times = [5, 3, 2, 6, 4]
m = 4
queries = [(1,), (2,), (3,), (2,)]

results = task_scheduler(n, task_names, priorities, execution_times, m, queries)
for result in results:
    print(result)





