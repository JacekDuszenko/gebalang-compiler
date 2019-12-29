class Commands:
    def __init__(self):
        self.commands = []

    def add_command(self, cmd):
        self.commands.append(cmd)

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return self.commands


class AssignCommand:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.identifier] + [self.expression]


class IfThenCommand:
    def __init__(self, condition, commands):
        self.condition = condition
        self.commands = commands

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.condition] + self.commands.commands


class IfThenElseCommand:
    def __init__(self, condition, commands_if, commands_else):
        self.condition = condition
        self.commands_if = commands_if
        self.commands_else = commands_else

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.condition] + self.commands_if.commands + self.commands_else.commands


class WhileCommand:
    def __init__(self, condition, commands):
        self.condition = condition
        self.commands = commands

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.condition] + self.commands.commands


class DoWhileCommand:
    def __init__(self, commands, condition):
        self.commands = commands
        self.condition = condition

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return self.commands.commands + [self.condition]


class ForUpToCommand:
    def __init__(self, local_iterator, value_from, value_to, commands):
        self.local_iterator = local_iterator
        self.value_from = value_from
        self.value_to = value_to
        self.commands = commands

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.value_from] + [self.value_to] + self.commands.commands


class ForDownToCommand:
    def __init__(self, local_iterator, value_from, value_to, commands):
        self.local_iterator = local_iterator
        self.value_from = value_from
        self.value_to = value_to
        self.commands = commands

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.value_from] + [self.value_to] + self.commands.commands


class ReadCommand:
    def __init__(self, identifier):
        self.identifier = identifier

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.identifier]


class WriteCommand:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_leaf(): return False

    def get_children(self):
        return [self.value]
