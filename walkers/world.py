import itertools
import numpy as np
from walkers.agent import Agent
class World:

    new_name = itertools.count()

    def __init__(self, coords : tuple) -> None:
        self.name = "world_" + str(next(self.new_name))
        self.xlimit = coords[0]
        self.ylimit = coords[1]
        self.populace = Population()

    def get_limits(self):
        return (self.xlimit, self.ylimit)

    def get_name(self):
        return self.name

    def get_population(self):
        return self.populace.population

    def populate(self, n) -> None:
        """**populate function**

        This function populates the world object with a given number of Agents. 
        It calls the spawn function from the Population object a given number of times 
        using the xlimit and ylimit World attributes.

        :param n: number of agents to populate within world
        :type n: int
        """
        map(self.populace.spawn(self.xlimit, self.ylimit), range(n))


class Population:

    def __init__(self):
        self.population = []

    def spawn(self, xlimit, ylimit):
        """**spawn function**

        This function takes the xlimit and ylimit of the world instance and adds one Agent 
        into the world at a randomly seeded location that is not already occupied by an agent.

        :param xlimit: the maximum value for the x-axis of the bounded world
        :type xlimit: int
        :param ylimit: the maximum value for the y-axis of the bounded world
        :type ylimit: int
        :return: None
        """

        start_x = np.random.choice(range(0, xlimit))

        start_y = np.random.choice(range(0, ylimit))
        try:

            if (start_x, start_y) not in set([member.get_position() for member in self.population]):
                self.population.append(Agent(origin=(start_x, start_y), limits=(xlimit,ylimit)))
                return None

            else:
                self.spawn(xlimit, ylimit)

        except RecursionError as e:
            raise Exception("Can't spawn more Agents as world is full!") from e





    
