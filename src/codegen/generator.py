from src.codegen.visitor import CodeGenVisitor


def append_halt(func):
    def wrapper(arg):
        return func(arg) + ' HALT'
    return wrapper


class CodeGenerator:
    def __init__(self, vmem, cpool, vpool, ptree):
        self.memory = vmem
        self.vpool = vpool
        self.cpool = cpool
        self.ptree = ptree
        self.k = 0

    @append_halt
    def generate_vm_code(self):
        cg = CodeGenVisitor(self)
        return cg.visit(self.ptree.commands)
