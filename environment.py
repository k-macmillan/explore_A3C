from actions import Action


##
## @brief      Class for environment. This simple environment represents the
##             training environment for the A3C exploration environment
##
class Environment:
    def __init__(self):
        self.max_actions = 5
        self.reset()

    def reset(self):
        self.actions = []
        


    ##
    ## @brief      Step function for the environment. Each step it will add the
    ##             action value to the list. When the list fills to 5 items it
    ##             will return a reward, otherwise it returns 0 reward.
    ##
    ## @param      self    The object
    ## @param      action  The action value
    ##
    ## @return     Tuple of reward, state
    ##
    def step(self, action):
        reward = 0
        self.actions.append(action)
        if len(self.actions) == self.max_actions:
            for item in self.actions:
                if item == Action.big:
                    reward -= item
                else:
                    reward += item
            self.actions = []
            return (reward, 0)
        else:
            return (0, len(self.actions))

        


