from src.ast import *
from src.sa.util import *
"""
Each strategy's apply function returns new scope as a function of current state
"""


class AssignVisitStrategy:
    def is_applicable(self, assign_cmd):
        return isinstance(assign_cmd, AssignCommand)

    def apply(self, visitor, assign_cmd):
        scope = visitor.scope
        variable_node = assign_cmd.identifier
        validate_identifier(scope, variable_node)
        validate_loop_iterator_modification(scope, variable_node)
        expr_identifiers = extract_identifiers_from_expression(assign_cmd.expression)
        [validate_identifier(scope, i) for i in expr_identifiers]
        mark_as_initialized(scope, variable_node)
        [validate_initialized(scope, i) for i in expr_identifiers]


class IfThenVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, IfThenCommand)

    def apply(self, visitor, if_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(if_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        [validate_initialized(scope, i) for i in cond_identifiers]
        return visitor.scope


class IfThenElseVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, IfThenElseCommand)

    def apply(self, visitor, if_else_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(if_else_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        [validate_initialized(scope, i) for i in cond_identifiers]
        return visitor.scope


class WhileVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, WhileCommand)

    def apply(self, visitor, while_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(while_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        [validate_initialized(scope, i) for i in cond_identifiers]
        return visitor.scope


class DoWhileVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, DoWhileCommand)

    def apply(self, visitor, do_while_cmd):
        scope = visitor.scope
        cond_identifiers = extract_identifiers_from_condition(do_while_cmd.condition)
        [validate_identifier(scope, i) for i in cond_identifiers]
        [validate_initialized(scope, i) for i in cond_identifiers]
        return visitor.scope


class ForUpToVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, ForUpToCommand)

    def apply(self, visitor, for_up_to_cmd):
        handle_local_iterator_logic(for_up_to_cmd, visitor)
        validate_for_loop_identifiers(for_up_to_cmd, visitor)
        return visitor.scope


class ForDownToVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, ForDownToCommand)

    def apply(self, visitor, for_downto_cmd):
        handle_local_iterator_logic(for_downto_cmd, visitor)
        validate_for_loop_identifiers(for_downto_cmd, visitor)
        return visitor.scope


class ReadVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, ReadCommand)

    def apply(self, visitor, read_cmd):
        scope = visitor.scope
        identifier = read_cmd.identifier
        validate_identifier(scope, identifier)
        validate_loop_iterator_modification(scope, identifier)
        mark_as_initialized(scope, identifier)
        return visitor.scope


class WriteVisitStrategy:
    def is_applicable(self, node):
        return isinstance(node, WriteCommand)

    def apply(self, visitor, write_cmd):
        scope = visitor.scope
        if not write_cmd.value.is_leaf():
            identifier = write_cmd.value.value
            validate_identifier(scope, identifier)
            validate_initialized(scope, identifier)
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


