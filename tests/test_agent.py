from itertools import combinations_with_replacement
import unittest
import numpy as np
from walkers.agent import Agent, RandomWalk

class testAgentClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_agent1 = Agent(origin = (10,10), limits=(20,20))


    def test_get_name(self) -> None:

        self.assertTrue(isinstance(self.test_agent1.get_name(), str))

    def test_get_name_unique(self) -> None:
        
        agent_set = set([Agent(origin = (0,10), limits=(10,10)).get_name() for _ in range(10000)])

        self.assertEqual(len(agent_set), 10000)

    def test_get_position(self) -> None:

        self.assertEqual(self.test_agent1.get_position(), (10,10))

    def test_get_limits(self) -> None:

        self.assertEqual(self.test_agent1.get_limits(), (20,20))

class testRandomWalkClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_rwalk = RandomWalk(origin=(0,1), limits=(5,5))

    def test_instantiation(self):

        self.assertEqual(self.test_rwalk.start, (0,1))
        self.assertTrue(isinstance(self.test_rwalk.path, np.ndarray))
        self.assertEqual(self.test_rwalk.step_set, [-1, 0, 1])
        self.assertEqual(self.test_rwalk.limits, (5,5))

    def test_step_distance(self):
        """
        Tests for stepping:
        - step is only within expected range (either -1, 0 or 1)
        - cannot step outside world limits
        - cannot step on existing agent
        """

        self.test_rwalk.step()

        self.assertEqual(self.test_rwalk.path.shape, (2,2))

        test_step_length = tuple(map(int, self.test_rwalk.path[1] - self.test_rwalk[0]))

        self.assertTrue(test_step_length in \
            list(combinations_with_replacement([-1, 0, 1], 2)))


if __name__ == '__main__':
    unittest.main()