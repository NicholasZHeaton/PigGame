from typing import Dict

from Item import Item


class Location:
    def __init__(self, l_desc, thing=None):
        self.l_desc = l_desc
        self.thing = thing
        self.neighbors = {}

    def get_item(self):
        return self.thing

    def get_description(self):
        return self.l_desc

    def set_item(self, thing):
        self.thing = thing
        return self.thing

    def has_item(self):
        return self.thing is not None

    def get_neighbor(self, dir):
        if dir in self.neighbors.keys():
            return self.neighbors[dir]
        else:
            return None

    def add_neighbor(self, dir, loc):
        self.neighbors[dir] = loc

    def remove_item(self):
        remove_thing = self.thing
        self.thing = None
        return remove_thing

    def __str__(self):
        if self.thing is not None:
            return f'You are {self.l_desc}\nYou see {self.thing.get_description()}'
        else:
            return f'You are {self.l_desc}'


if __name__ == "__main__":
    description = "in a wasteland filled with lava"
    itm = Item("apple", "a red apple sitting in the lava", 5, True)
    area = Location(description, itm)
    print(area)
