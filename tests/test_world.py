import unittest
import itertools
import numpy as np
from walkers.agent import Agent 
from walkers.world import ToeGuard, World, Population

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

    def test_get_population(self) -> None:

        self.assertTrue(isinstance(self.test_world.get_population(),list))

    def test_populate(self) -> None:

        self.test_world.populate(5)

        self.assertEqual(len(self.test_world.get_population()), 5)

        self.assertEqual(len(set(self.test_world.get_population())), 5)

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

class TestToeGuardClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.ag1 = Agent(origin=(0,1))

        cls.ag2 = Agent(origin=(0,2))

        cls.test_toe = ToeGuard(population=[cls.ag1, cls.ag2], limits=(5,5))

    def test_instanstiation(self):

        self.assertTrue(isinstance(self.test_toe.population[0], Agent))

        self.assertEqual(self.test_toe.xlimit, 5)

        self.assertEqual(self.test_toe.ylimit, 5)

    def test_step(self):

        self.test_toe.step()

        self.assertEqual(self.ag1.get_path().shape, (2,2))

        self.assertEqual(self.ag2.get_path().shape, (2,2))

    def test_step_value(self):

        self.test_toe.step()

        flat_list_o_steps = [item for sublist in self.ag1.get_path() for item in sublist]

        self.assertTrue(len(flat_list_o_steps), 6)

        self.assertTrue(np.unique(flat_list_o_steps).tolist(), [-1, 0, 1])

    def test_step_limits(self):

        for _ in range(10000):
            self.test_toe.step()

        flat_list_o_steps = [item for sublist in self.ag1.get_journey() for item in sublist]

        self.assertFalse(-1 in flat_list_o_steps)

        self.assertFalse(5 in flat_list_o_steps)


    def test_step_noShared(self):

        self.assertEqual(self.ag1.get_journey().shape, (10002,2))

        self.assertFalse(np.any(np.all(self.ag1.get_journey() == self.ag2.get_journey(), axis=1)))

if __name__ == '__main__':
    unittest.main()