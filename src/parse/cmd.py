from src.ast.command import *


def create_assign_command(p):
    cmd = AssignCommand(p[1], p[3])
    p[0] = cmd


def create_if_then_command(p):
    cmd = IfThenCommand(p[2], p[4])
    p[0] = cmd


def create_if_then_else_command(p):
    cmd = IfThenElseCommand(p[2], p[4], p[6])
    p[0] = cmd


def create_while_command(p):
    cmd = WhileCommand(p[2], p[4])
    p[0] = cmd


def create_do_while_command(p):
    cmd = DoWhileCommand(p[2], p[4])
    p[0] = cmd


def create_for_up_to_command(p):
    cmd = ForUpToCommand(p[2], p[4], p[6], p[8])
    p[0] = cmd


def create_for_down_to_command(p):
    cmd = ForDownToCommand(p[2], p[4], p[6], p[8])
    p[0] = cmd


def create_read_command(p):
    cmd = ReadCommand(p[2])
    p[0] = cmd


def create_write_command(p):
    cmd = WriteCommand(p[2])
    p[0] = cmd
