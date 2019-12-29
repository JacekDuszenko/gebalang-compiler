from src.ast import *
from src.codegen.cp import ConstantPool
from src.codegen.generator import CodeGenerator
from src.codegen.vmem import VirtualMemory
from src.codegen.vp import VariablePool


def allocate_variables(memory, variables):
    for variable_name, variable_dec in variables.pool:
        if isinstance(variable_dec, VariableDeclaration):
            memory.allocate_memory_for_variable(variable_name, variable_dec)


def create_code_generator(ptree):
    decs_dict = ptree.declarations.declarations
    memory = VirtualMemory()
    cpool = ConstantPool()
    vpool = VariablePool(decs_dict)
    allocate_variables(memory, vpool)
    generator = CodeGenerator(memory, cpool, vpool, ptree)
    return generator
