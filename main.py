from task import Task
from taskqueue import TaskQueue
from taskresults import TaskResults
import sys

if __name__ == '__main__':
    simple_tasks = TaskQueue()
    taskresults = TaskResults()
    simple_tasks.push(Task(description='My first task', command="ping -n 3 google-public-dns-a.google.com", taskresults=taskresults))
    simple_tasks.push(Task(description='My second task', command="ping -n 3 google-public-dns-b.google.com", taskresults=taskresults))
    while simple_tasks.peek_next():
        t = simple_tasks.pop()
        sys.stdout.write("Running task ")
        sys.stdout.write(str(t.GUID))
        sys.stdout.write("\n")
        t.execute()
        res = taskresults.result(t.GUID)
        sys.stdout.write("Task suceeded: %s\n" % str(res.succeeded))