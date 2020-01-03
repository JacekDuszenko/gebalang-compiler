from src.ast import *
from src.codegen.visitor import CodeGenVisitor


def append_halt(func):
    def wrapper(arg):
        return func(arg) + 'HALT'

    return wrapper


class CodeGenerator:
    def __init__(self, vmem, cpool, vpool, ptree):
        self.memory = vmem
        self.vpool = vpool
        self.cpool = cpool
        self.ptree = ptree
        self.k = 0

    @append_halt
    def generate_vm_code(self):
        cg = CodeGenVisitor(self)
        return cg.visit(self.ptree.commands)

    def get_address_by_variable_name(self, variable_name, index=None):
        dec = self.vpool.pool[variable_name]
        if isinstance(dec, VariableDeclaration):
            return dec.addr
        if isinstance(dec, ArrayDeclaration):
            return dec.addr[index]

    def get_declaration_by_variable_name(self, variable_name):
        dec = self.vpool.pool[variable_name]
        return dec
