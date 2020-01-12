STARTING_MEMORY = 11
ENDING_MEMORY = 2 ** 62 -1


class VirtualMemory:
    def __init__(self):
        self.memory = {}
        self.memory_counter = STARTING_MEMORY
        self.local_memory_counter = ENDING_MEMORY

    def allocate_memory_for_local_variable(self, variable_name, variable_declaration):
        var_cell = VariableMemoryCell(self, variable_name, variable_declaration)
        self.memory[self.local_memory_counter] = var_cell
        variable_declaration.addr = self.local_memory_counter
        self.local_memory_counter -= 1
        return var_cell

    def pop_local_variable(self):
        self.local_memory_counter += 1
        del(self.memory[self.local_memory_counter])

    def allocate_memory_for_variable(self, variable_name, variable_declaration):
        var_cell = VariableMemoryCell(variable_declaration, variable_name, self.memory_counter)
        self.memory[self.memory_counter] = var_cell
        variable_declaration.addr = self.memory_counter
        self.memory_counter += 1
        return var_cell

    def allocate_memory_for_constant(self, value, value_reference):
        var_cell = ConstantMemoryCell(value, self.memory_counter)
        self.memory[self.memory_counter] = var_cell
        value_reference.addr = self.memory_counter
        self.memory_counter += 1
        return var_cell

    def allocate_memory_for_array(self, declaration, variable_name):
        start_index = declaration.start_index
        end_index = declaration.end_index
        result = []
        for i in range(start_index, end_index + 1):
            var = ArrayMemoryCell(declaration, variable_name, self.memory_counter)
            self.memory[self.memory_counter] = var
            result.append(self.memory_counter)
            self.memory_counter += 1
        declaration.addr = result
        return result


class MemoryCell:
    pass


class VariableMemoryCell(MemoryCell):
    def __init__(self, declaration, variable, addr):
        self.declaration = declaration
        self.variable = variable
        self.addr = addr


class ArrayMemoryCell(MemoryCell):
    def __init__(self, declaration, variable, addr):
        self.declaration = declaration
        self.variable = variable
        self.addr = addr


class ConstantMemoryCell(MemoryCell):
    def __init__(self, value, addr):
        self.value = value
        self.addr = addr
