class Program:
    def __init__(self, declarations, commands):
        self.declarations = declarations
        self.commands = commands

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return self.commands.commands + self.declarations.declarations
