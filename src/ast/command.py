class Commands:
    def __init__(self):
        self.commands = []

    def add_command(self, cmd):
        self.commands.append(cmd)


class AssignCommand:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression


class IfThenCommand:
    def __init__(self, condition, commands):
        self.condition = condition
        self.commands = commands


class IfThenElseCommand:
    def __init__(self, condition, commands_if, commands_else):
        self.condition = condition
        self.commands_if = commands_if
        self.commands_else = commands_else


class WhileCommand:
    def __init__(self, condition, commands):
        self.condition = condition
        self.commands = commands


class DoWhileCommand:
    def __init__(self, commands, condition):
        self.commands = commands
        self.condition = condition


class ForUpToCommand:
    def __init__(self, id, value_from, value_to, commands):
        self.id = id
        self.value_from = value_from
        self.value_to = value_to
        self.commands = commands


class ForDownToCommand:
    def __init__(self, id, value_from, value_down_to, commands):
        self.id = id
        self.value_from = value_from
        self.value_down_to = value_down_to
        self.commands = commands


class ReadCommand:
    def __init__(self, identifier):
        self.identifier = identifier


class WriteCommand:
    def __init__(self, value):
        self.value = value
