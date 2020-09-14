import numpy as np
import itertools

class Agent:

    new_name = itertools.count()

    def __init__(self, origin : tuple, limits : tuple):
        self.name = "agent_" + str(next(self.new_name))
        self.position = origin
        self.walker = RandomWalk(origin=origin, limits=limits)

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position 

    def get_limits(self):
        return self.walker.limits

    def step(self):
        return self.walker.step()

class RandomWalk:

    def __init__(self, origin : tuple, limits : tuple):
        self.limits = limits
        self.start = origin
        self.path = np.zeros((1, len(origin)))
        self.step_set = [-1, 0, 1]

    def step(self) -> None:
        """RandomWalk Step function

        This function just controls the inner logic for how an agent would step.
        """

        step = np.random.choice(self.step_set, size=len(self.start))

        return step


    