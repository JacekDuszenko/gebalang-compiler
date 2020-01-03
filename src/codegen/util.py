def calculate_shifted_index(declaration_node, variable_node):
    start_index = declaration_node.start_index
    return abs(start_index - variable_node.accessor)


def get_array_const_index_address(codegen, identifier):
    variable_name = identifier.variable
    dec = codegen.get_declaration_by_variable_name(variable_name)
    shifted_index = calculate_shifted_index(dec, identifier)
    addr = codegen.get_address_by_variable_name(variable_name, shifted_index)
    return addr