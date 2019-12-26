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
