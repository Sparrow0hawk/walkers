import itertools

class World:

    new_name = itertools.count()

    def __init__(self, coords : tuple) -> None:
        self.name = "word_" + str(next(self.new_name))
        self.xlimit = coords[0]
        self.ylimit = coords[1]

    def get_limits(self):
        return (self.xlimit, self.ylimit)