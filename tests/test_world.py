import unittest
from walkers.agent import Agent 
from walkers.world import World, Population

class testWorldClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        
        cls.test_world = World(coords = (100,100))

    def test_limits(self) -> None:

        self.assertEqual(self.test_world.get_limits(), (100,100))


    def test_get_name(self) -> None:

        self.assertTrue(isinstance(self.test_world.get_name(), str))

    def test_get_name_unique(self) -> None:
        
        world_set = set([World(coords = (10,10)).get_name() for _ in range(1000)])

        self.assertEqual(len(world_set), 1000)

# do we need a reset function? to clear class attributes
class TestPopulationClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_pop = Population()

    def test_instanstiation(self):

        self.assertEqual(len(self.test_pop.population), 0)

    def test_spawn(self):

        self.test_pop.spawn(2,2)

        self.assertEqual(len(self.test_pop.population), 1)
        self.assertTrue(isinstance(self.test_pop.population[0], Agent))

        self.assertTrue(self.test_pop.population[0].get_position() in \
            [(0,0), (0,1), (1,0), (1,1)])

    def test_spawn_fail(self):

        with self.assertRaises(Exception) as cm:
            [self.test_pop.spawn(2,2) for _ in range(5)]

        self.assertTrue("Can't spawn more Agents as world is full!" in str(cm.exception))

if __name__ == '__main__':
    unittest.main()