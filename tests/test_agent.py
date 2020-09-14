import unittest
from walkers.agent import Agent

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

if __name__ == '__main__':
    unittest.main()