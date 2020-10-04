from walkers.front import Front
from walkers.world import World

def main():

    world = World(coords=(100,100))

    width = 800
    height = 600

    frontend = Front(world, width, height)

    while frontend.is_active():
        frontend.update()


if __name__ == '__main__':
    main()