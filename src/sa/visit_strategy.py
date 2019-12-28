from src.ast import *
from src.util import error

"""
Each strategy's apply function returns new scope as a function of current state
"""


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


def extract_identifiers_from_condition(condition):
    return [c.value for c in [condition.left, condition.right] if not c.is_leaf()]


class AssignVisitStrategy:
    def is_applicable(self, assign_cmd):
        return isinstance(assign_cmd, AssignCommand)

    def apply(self, visitor, assign_cmd):
        scope = visitor.scope
        variable_node = assign_cmd.identifier
        validate_identifier(scope, variable_node)
        expr_identifiers = extract_identifiers_from_expression(assign_cmd.expression)
        [validate_identifier(scope, i) for i in expr_identifiers]


class IfThenVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, IfThenCommand)

    def apply(self, visitor, if_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(if_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        return visitor.scope


class IfThenElseVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, IfThenElseCommand)

    def apply(self, visitor, if_else_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(if_else_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        return visitor.scope


class WhileVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, WhileCommand)

    def apply(self, visitor, while_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(while_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        return visitor.scope


class DoWhileVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, DoWhileCommand)

    def apply(self, visitor, do_while_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(do_while_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        return visitor.scope


class ForUpToVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, ForUpToCommand)

    def apply(self, visitor, node):
        return visitor.scope            #TODO


class ForDownToVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, ForDownToCommand)

    def apply(self, visitor, node):
        return visitor.scope            #TODO


class ReadVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, ReadCommand)

    def apply(self, visitor, read_cmd):
        scope = visitor.scope
        validate_identifier(scope, read_cmd.identifier)
        return visitor.scope


class WriteVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, WriteCommand)

    def apply(self, visitor, write_cmd):
        scope = visitor.scope
        if not write_cmd.value.is_leaf():
            validate_identifier(scope, write_cmd.value.value)
        return visitor.scope


def create_visit_strats():
    return [AssignVisitStrategy(),
            IfThenElseVisitStrategy(),
            IfThenVisitStrategy(),
            WhileVisitStrategy(),
            DoWhileVisitStrategy(),
            ForUpToVisitStrategy(),
            ForDownToVisitStrategy(),
            ReadVisitStrategy(),
            WriteVisitStrategy()]


def ndeclared_msg(identifier):
    return "Variable {} has not been declared".format(identifier)


def wrong_usage(v, vtype):
    return "Wrong usage of variable {}. This variable is declared as {}.".format(v, vtype)


def accessor_not_in_range(accesor, l, r, array_id):
    return "Wrong usage of array {}. It was accessed with number {} but its range is from {} to {}".format(array_id,
                                                                                                           accesor, l,
                                                                                                           r)
