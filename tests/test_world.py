import unittest 
from walkers.world import World

class testWorldClass(unittest.TestCase):

    def setUp(self) -> None:
        
        self.test_world = World(coords = (100,100))

    def test_limits(self) -> None:

        self.assertEqual(self.test_world.get_limits(), (100,100))