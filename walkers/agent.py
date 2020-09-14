import numpy as np
import itertools

class Agent:

    new_name = itertools.count()

    def __init__(self, origin : tuple):
        self.name = "agent_" + str(next(self.new_name))
        self.position = origin

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position 