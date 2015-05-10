class TaskResult:

    def __init__(self, task_guid):
        self.task_guid = task_guid
        self.succeeded = False
        self.return_code = None
        self.output = ""
        self.exception = ""
        self.execution_duration = 0
        self.completed = False