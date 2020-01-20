from src.ast import *
from src.codegen.create_constant import place_one_in_onereg
from src.codegen.labels import resolve_labels
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
        code = ""
        code += place_one_in_onereg()
        code_without_labels = cg.visit(self.ptree.commands)
        code += code_without_labels
        # print(code_without_labels)
        return resolve_labels(code)

    def get_address_by_variable_name(self, variable_name, index=None):
        dec = self.vpool.pool[variable_name]
        if isinstance(dec, VariableDeclaration):
            return dec.addr
        if isinstance(dec, ArrayDeclaration):
            return dec.addr + index

    def get_declaration_by_variable_name(self, variable_name):
        dec = self.vpool.pool[variable_name]
        return dec

    def allocate_local_variable_with_term_cond(self, variable_name):
        term_cond_variable_name = f'{variable_name}_term_cond'
        dec = VariableDeclaration(variable_name, 0, initialized=True, local=True)
        term_cond_dec = VariableDeclaration(term_cond_variable_name, 0, initialized=True, local=True)
        self.memory.allocate_memory_for_local_variable(variable_name, dec)
        self.vpool.pool[variable_name] = dec
        self.memory.allocate_memory_for_local_variable(term_cond_variable_name, term_cond_dec)
        self.vpool.pool[term_cond_variable_name] = term_cond_dec

    def deallocate_local_variable_with_term_cond(self, variable_name):
        term_cond_variable_name = f'{variable_name}_term_cond'
        del(self.vpool.pool[term_cond_variable_name])
        self.memory.pop_local_variable()
        del(self.vpool.pool[variable_name])
        self.memory.pop_local_variable()

