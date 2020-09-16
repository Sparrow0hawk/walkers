from walkers.world import World
import matplotlib.pyplot as plt

def main():

    world = World(coords=(100,100))

    world.populate(3)

    for _ in range(100):
        world.step()

    print(world.get_population()[0].get_journey())

    for agent in world.get_population():

        plt.plot(agent.get_journey(), label=agent.get_name())

        plt.legend(bbox_to_anchor=(1,1.0))

        plt.show()



if __name__ == '__main__':
    main()