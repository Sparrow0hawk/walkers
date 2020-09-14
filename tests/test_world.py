import unittest 
from walkers.world import World

class testWorldClass(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        
        self.test_world = World(coords = (100,100))

    def test_limits(self) -> None:

        self.assertEqual(self.test_world.get_limits(), (100,100))


    def test_get_name(self) -> None:

        self.assertTrue(isinstance(self.test_world.get_name(), str))

    def test_get_name_unique(self) -> None:
        
        world_set = set([World(coords = (10,10)).get_name() for _ in range(1000)])

        self.assertEqual(len(world_set), 1000)