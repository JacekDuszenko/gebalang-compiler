from src.ast import *
from src.codegen.array_variable_access import *
from src.codegen.util import *


def store_value_in_register(codegen, value, storage_addr):
    if value.is_leaf():
        number = value.value
        return create_constant_number(number, storage_addr=storage_addr)
    else:
        identifier = value.value
        return store_variable_in_reg(codegen, identifier, storage_addr=storage_addr)


def store_variable_in_reg(codegen, identifier, storage_addr=0):
    variable_name = identifier.variable
    if isinstance(identifier, IdentifierVariable):
        variable_addr = codegen.get_address_by_variable_name(variable_name)
        return f"LOAD {variable_addr}\nSTORE {storage_addr}\n"
    if isinstance(identifier, IdentifierArrayNumber):
        array_index_addr = get_array_const_index_address(codegen, identifier)
        return f"LOAD {array_index_addr}\nSTORE {storage_addr}\n"
    if isinstance(identifier, IdentifierArrayVariable):
        code = load_array_variable_accessed_value(codegen, identifier)
        code += f"STORE {storage_addr}\n"
        return code
