from src.ast.command import Commands


def create_commands(p):
    cmds = Commands()
    cmds.add_command(p[1])
    p[0] = cmds


def append_command(p):
    cmds = p[1]
    cmds.add_command(p[2])
    p[0] = cmds