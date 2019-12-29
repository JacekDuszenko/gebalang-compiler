from src.ast import *
from src.util import error


def create_global_scope_from_decs(decs):
    return {dec.id: dec for dec in decs}


def validate_variable_not_declared(scope, variable_node):
    variable_name = variable_node.variable
    if variable_name not in scope:
        error(variable_node.line, ndeclared_msg(variable_name))


def validate_variable_wrong_usage(scope, variable_node):
    declared_variable = scope[variable_node.variable]
    if type(variable_node) not in declared_variable.variable_types():
        error(variable_node.line, wrong_usage(variable_node.variable, declared_variable.type_info()))


def validate_array_accessor_in_range(scope, variable_node):
    if isinstance(variable_node, IdentifierArrayNumber):
        accessor_index = variable_node.accessor
        declared_variable = scope[variable_node.variable]
        if not declared_variable.start_index <= accessor_index <= declared_variable.end_index:
            error(variable_node.line,
                  accessor_not_in_range(accessor_index, declared_variable.start_index, declared_variable.end_index,
                                        declared_variable.id))


def validate_identifier(scope, variable_node):
    validate_variable_not_declared(scope, variable_node)
    validate_variable_wrong_usage(scope, variable_node)
    validate_array_accessor_in_range(scope, variable_node)


def extract_identifiers_from_expression(expression):
    if isinstance(expression, UnaryExpression) and not expression.expression.is_leaf():
        return [expression.expression.value]
    elif isinstance(expression, BinaryExpression):
        return [expr.value for expr in [expression.left, expression.right] if not expr.is_leaf()]
    else:
        return []


def extract_identifiers_from_condition(condition):
    return [c.value for c in [condition.left, condition.right] if not c.is_leaf()]


def mark_as_initialized(scope, variable_node):
    variable_name = variable_node.variable
    if isinstance(variable_node, IdentifierVariable):
        scope[variable_name].initialized = True
    if isinstance(variable_node, IdentifierArrayNumber):
        index = variable_node.accessor
        scope[variable_name].initialized[index] = True
    if isinstance(variable_node, IdentifierArrayVariable):
        set_all_array_elems_to_initialized(scope, variable_name)


def set_all_array_elems_to_initialized(scope, variable_name):
    array_length = len(scope[variable_name].initialized)
    for i in range(0, array_length):
        scope[variable_name].initialized[i] = True


def validate_loop_iterator_modification(scope, variable_node):
    variable_name = variable_node.variable
    if variable_name in scope:
        dec = scope[variable_name]
        if dec.local is True:
            error(variable_node.line, loop_iterator_modifiaction(variable_name))


def validate_initialized(scope, variable_node):
    variable_name = variable_node.variable
    dec = scope[variable_name]
    if isinstance(variable_node, IdentifierVariable):
        if not dec.initialized:
            error(variable_node.line, variable_not_initialized(variable_name))
    if isinstance(variable_node, IdentifierArrayNumber):
        index = variable_node.accessor
        if not dec.initialized[index]:
            error(variable_node, variable_not_initialized(f'{variable_name}({index})'))
    if isinstance(variable_node, IdentifierArrayVariable):
        pass  # too complicated for this compiler


def extract_identifiers_from_forloop(value_from, value_to):
    return [v.value for v in [value_from, value_to] if not v.is_leaf()]


def validate_for_loop_identifiers(for_up_to_cmd, visitor):
    scope = visitor.scope
    cmd_identifiers = extract_identifiers_from_forloop(for_up_to_cmd.value_from, for_up_to_cmd.value_to)
    [validate_identifier(scope, i) for i in cmd_identifiers]
    [validate_initialized(scope, i) for i in cmd_identifiers]


def validate_iterator_not_in_scope(local_iterator, scope):
    variable_name = local_iterator.variable
    if variable_name in scope:
        error(local_iterator.line, local_iterator_already_declared(variable_name))


def add_local_variable_to_scope(visitor, local_iterator):
    variable_name = local_iterator.variable
    local_declaration = VariableDeclaration(variable_name, local_iterator.line, initialized=True, local=True)
    visitor.scope[variable_name] = local_declaration


def handle_local_iterator_logic(for_loop, visitor):
    scope = visitor.scope
    local_iterator = for_loop.local_iterator
    validate_iterator_not_in_scope(local_iterator, scope)
    validate_iterator_not_in_loop_range(for_loop, local_iterator)

    add_local_variable_to_scope(visitor, local_iterator)


def validate_iterator_not_in_loop_range(for_loop, local_iterator):
    identifiers = extract_identifiers_from_forloop(for_loop.value_from, for_loop.value_to)
    [error(local_iterator.line, using_local_in_loop_range(i.variable)) for i in identifiers if
     i.variable is local_iterator.variable]


def using_local_in_loop_range(identifier):
    return f'Loop iterator {identifier} used in loop range'


def ndeclared_msg(identifier):
    return f'Variable {identifier} has not been declared'


def wrong_usage(v, vtype):
    return f'Wrong usage of variable {v}. This variable is declared as {vtype}.'


def accessor_not_in_range(accessor, l, r, array_id):
    return f'Wrong usage of array {array_id}. It was accessed with number {accessor} but its range is from {l} to {r}'


def local_iterator_already_declared(variable_name):
    return f' Identifier {variable_name} is declared in enclosing scope, give this loop iterator another name'


def loop_iterator_modifiaction(variable_name):
    return f'Loop iterator {variable_name} modification detected'


def variable_not_initialized(variable_name):
    return f'Variable {variable_name} is not initialized'
