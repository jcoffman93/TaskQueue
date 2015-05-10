import uuid

class TaskResults(dict):

    def __init__(self):
        super(TaskResults, self).__init__()

    def __setitem__(self, key, value):
        if type(key) is not uuid.UUID:
            raise Exception("Key must be of type uuid.UUID")
        else:
            return dict.__setitem__(self, key, value)

    def result(self, guid):
        if type(guid) is not uuid.UUID:
            raise Exception("Key must be of type uuid.UUID")
        else:
            return dict.__getitem__(self, guid)

    def results(self, guid_list):
        return [self.result(guid) for guid in guid_list]