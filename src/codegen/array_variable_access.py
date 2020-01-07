from src.codegen.create_constant import create_constant_number

"""
USED REGISTERS:
0, 1, 2
"""


def load_array_variable_addr(codegen, identifier):
    code = ""
    array_name = identifier.variable
    array_dec = codegen.get_declaration_by_variable_name(array_name)
    array_start_index = array_dec.start_index

    code += store_array_start_index_in_one(array_start_index)

    array_start_addr = array_dec.addr[0]
    code += store_array_start_index_addr_in_two(array_start_addr)

    accessor_variable_name = identifier.accessor
    accessor_variable_address = codegen.get_address_by_variable_name(accessor_variable_name)
    code += store_accessor_value_in_zero(accessor_variable_address)

    code += get_relative_array_index()
    code += get_array_element_address()
    return code


def load_array_variable_accessed_value(codegen, identifier):
    code = ""
    code += load_array_variable_addr(codegen, identifier)
    code += get_value_under_address()
    return code


def store_accessor_value_in_zero(addr):
    return f"""LOAD {addr}
"""


def store_array_start_index_in_one(start_index):
    return create_constant_number(start_index, storage_addr=1)


def get_relative_array_index():
    return """SUB 1
"""


def store_array_start_index_addr_in_two(array_start_addr):
    return create_constant_number(array_start_addr, storage_addr=2)


def get_array_element_address():
    return "ADD 2\n"


def get_value_under_address():
    return "LOADI 0\n"
