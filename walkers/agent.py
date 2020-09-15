import numpy as np
import itertools

class Agent:

    new_name = itertools.count()

    def __init__(self, origin : tuple):
        self.name = "agent_" + str(next(self.new_name))
        self.position = origin
        self.walker = RandomWalk(origin=origin)

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position 

    def step(self):
        return self.walker.step()

class RandomWalk:

    def __init__(self, origin : tuple):
        self.start = origin
        self.path = np.asarray(origin).reshape((1,2))
        self.step_set = [-1, 0, 1]

    def step(self):
        """RandomWalk Step function

        This function just controls the inner logic for how an agent would step.
        """

        step = np.random.choice(self.step_set, size=len(self.start))

        return step

    def update(self, step):

        np_step = np.asarray(step).reshape((1,2))

        self.path = np.concatenate([self.path, np_step]).cumsum(0)


    