import uuid
from taskresult import TaskResult
from taskresults import TaskResults
import subprocess
import time

class Task:
    def __init__(self, description, command, taskresults=None):
        """Parameters:
        desc        - String       A description of the task.
        command     - String       The command that will be run.
        taskresults - TaskResults  Instance of TaskResults which will be used to track task execution.
        """
        self.description =description
        self.command = command
        self.GUID = uuid.uuid4()
        self.taskresults = taskresults

    def execute(self):
        """Executes task, recording execution result in TaskResults instance if it exists."""
        if self.taskresults is not None:
            self.taskresults[self.GUID] = TaskResult(self.GUID)
        t_initial = time.time()
        try:
            output = subprocess.check_output(self.command)
            t_elapsed = t_initial - time.time()
            if self.taskresults is not None:
                self.taskresults[self.GUID].succeeded = True
                self.taskresults[self.GUID].return_code = 0
                self.taskresults[self.GUID].output = output
                self.taskresults[self.GUID].execution_duration = t_elapsed
                self.taskresults[self.GUID].completed = True
            print output
        except subprocess.CalledProcessError as e:
            t_elapsed = t_initial - time.time()
            if self.taskresults is not None:
                self.taskresults[self.GUID].return_code = e.returncode
                self.taskresults[self.GUID].output = e.output
                self.taskresults[self.GUID].execution_duration = t_elapsed
                self.taskresults[self.GUID].completed = True
            print e.output