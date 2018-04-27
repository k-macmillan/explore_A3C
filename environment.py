from actions import Action


class Environment:
    def __init__(self):
        self.actions = []


    def step(self, action):
        reward = 0
        self.actions.append(action)
        if len(self.actions) == 4:
            for item in self.actions:
                if item == Action.big:
                    reward -= item
                else:
                    reward += item
        else:
            reward += action

        return reward
