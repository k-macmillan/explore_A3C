from actions import Action


class Environment:
    def __init__(self):
        self.actions = []


    def step(self, action):
        reward = 0
        self.actions.append(action)
        if len(self.actions) == 3:
            for item in self.actions:
                if item == big:
                    reward -= item
                else:
                    reward += item
                