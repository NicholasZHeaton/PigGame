class Item:
    def __init__(self, name, desc, weight, edible):
        self.name = name
        self.desc = desc
        self.weight = weight
        self.edible = edible

    def is_edible(self):
        if self.edible is True:
            return True
        else:
            return False

    def set_edible(self, edible):
        self.edible = edible

    def get_weight(self):
        return self.weight

    def set_weight(self, wt):
        self.weight = wt

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.desc

    def set_description(self, desc):
        self.desc = desc

    def __str__(self):
        return self.desc
