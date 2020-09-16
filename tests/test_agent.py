import itertools
import unittest
import numpy as np
from walkers.agent import Agent, RandomWalk

class testAgentClass(unittest.TestCase):

    def setUp(self) -> None:
        self.test_agent1 = Agent(origin = (10,10))

    def test_get_name(self) -> None:

        self.assertTrue(isinstance(self.test_agent1.get_name(), str))

    def test_get_name_unique(self) -> None:
        
        agent_set = set([Agent(origin = (0,10)).get_name() for _ in range(10000)])

        self.assertEqual(len(agent_set), 10000)

    def test_get_position(self) -> None:

        self.assertEqual(self.test_agent1.get_position(), (10,10))
    
    def test_update(self):

        self.test_agent1.update(np.asarray((1,0)))

        self.assertEqual(self.test_agent1.get_path().shape, (2,2))

        self.assertTrue((self.test_agent1.get_path()[-1] == np.asarray((1,0))).all())

        self.assertFalse((self.test_agent1.get_path()[-1] == np.asarray((1,1))).all())

    def test_get_journey(self):

        self.test_agent1.update(np.asarray((1,0)))

        test_journey = self.test_agent1.get_journey()

        self.assertTrue((test_journey[-1] == np.asarray((11,10))).all())


class testRandomWalkClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_rwalk = RandomWalk(origin=(0,1))

    def test_instantiation(self):

        self.assertEqual(self.test_rwalk.start, (0,1))
        self.assertTrue(isinstance(self.test_rwalk.path, np.ndarray))
        self.assertEqual(self.test_rwalk.step_set, [-1, 0, 1])

    def test_step(self):
        
        step_output = self.test_rwalk.step()

        self.assertTrue(isinstance(step_output, np.ndarray))

        step_output_tuple = tuple(map(int, step_output))

        self.assertTrue(step_output_tuple in \
            list(itertools.product([-1, 0, 1], repeat=2)))

    def test_update(self):

        self.test_rwalk.update(step=(0,1))

        self.assertTrue(isinstance(self.test_rwalk.path, np.ndarray))

        self.assertEqual(len(self.test_rwalk.path), 2)

        self.assertTrue(self.test_rwalk.path[1][1], 2)


    @unittest.skip(reason="Moving some of these ideas into World which will handle step consequences")
    def test_step_distance(self):
        """
        Tests for stepping:
        - step is only within expected range (either -1, 0 or 1)
        - cannot step outside world limits
        - cannot step on existing agent
        """

        self.assertEqual(self.test_rwalk.path.shape, (2,2))

        test_step_length = tuple(map(int, self.test_rwalk.path[1] - self.test_rwalk[0]))

        self.assertTrue(test_step_length in \
            list(combinations_with_replacement([-1, 0, 1], 2)))

    @unittest.skip(reason="Skipped as looking to implement not within RW.step")
    def test_step_limits(self):

        [self.test_rwalk.step() for _ in range(10000)]

        flat_list_o_steps = [item for sublist in self.test_rwalk.path for item in sublist]

        self.assertFalse(-1 in flat_list_o_steps)

        self.assertFalse(5 in flat_list_o_steps)

    @unittest.skip(reason= "Left for future implementation")
    def test_dont_stepon(self):

        return None

if __name__ == '__main__':
    unittest.main()