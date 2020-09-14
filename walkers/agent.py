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

