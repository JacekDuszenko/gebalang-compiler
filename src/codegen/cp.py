import collections


class ConstantPool:
    def __init__(self):
        self.pool = collections.OrderedDict()

    def add_to_pool(self, val, addr):
        self.pool[val] = addr
