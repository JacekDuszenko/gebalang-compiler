from src.ast import *
from src.codegen.cp import ConstantPool
from src.codegen.generator import CodeGenerator
from src.codegen.vmem import VirtualMemory
from src.codegen.vp import VariablePool


def allocate_variables(memory, variables):
    for variable_name, variable_dec in variables.pool.items():
        if isinstance(variable_dec, VariableDeclaration):
            memory.allocate_memory_for_variable(variable_name, variable_dec)
        if isinstance(variable_dec, ArrayDeclaration):
            memory.allocate_memory_for_array(variable_dec, variable_name)


def create_code_generator(ptree, globals):
    memory = VirtualMemory()
    cpool = ConstantPool()
    vpool = VariablePool(globals)
    allocate_variables(memory, vpool)
    generator = CodeGenerator(memory, cpool, vpool, ptree)
    return generator
