import numpy as np
import itertools

class Agent:

    new_name = itertools.count()

    def __init__(self):
        self.name = "agent_" + str(next(self.new_name))

    def get_name(self):
        return self.name