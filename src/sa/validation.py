from src.util import *


def detect_redeclaration(node, list_of_declarations):
    list_of_ids = map(lambda n: n.id, list_of_declarations)
    if node.id in list_of_ids:
        error(node.line, "Second declaration of variable {}".format(node.id))


def detect_wrong_array_range(node):
    if node.start_index > node.end_index:
        error(node.line, "Invalid range of array with id {}.".format(node.id))
