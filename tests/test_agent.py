import unittest
from walkers.agent import Agent

class testAgentClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_agent1 = Agent()


    def test_get_name(self) -> None:

        self.assertTrue(isinstance(self.test_agent1.get_name(), str))

    def test_get_name_unique(self) -> None:
        
        agent_set = set([Agent().get_name() for _ in range(10000)])

        self.assertEqual(len(agent_set), 10000)
