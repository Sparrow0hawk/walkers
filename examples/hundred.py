from walkers.world import World
import matplotlib.pyplot as plt

def main():

    world = World(coords=(100,100))

    world.populate(100)

    for _ in range(100):
        world.step()

    for agent in world.get_population():

        plt.plot(agent.get_journey()[:,0],agent.get_journey()[:, 1], label=agent.get_name(),
                 zorder=1)

        plt.plot(agent.get_journey()[0,0], agent.get_journey()[0,1],'ro', zorder=2)

        plt.axis([0, world.get_limits()[0], 0, world.get_limits()[1]])

        plt.title("Hundreds of walkers")

    plt.savefig('examples/outputs/hundreds.png', bbox_inches='tight', dpi=300)
    plt.show()

if __name__ == '__main__':
    main()