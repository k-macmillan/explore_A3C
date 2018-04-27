
class GlobalNetwork:
    def __init__(self, scope):
        self.scope = scope
        self.reset()

    def reset(self):
        self.value = 0
        self.policy


    def update(self, worker):
        self.value = worker.value # basic concept