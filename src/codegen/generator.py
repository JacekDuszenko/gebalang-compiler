from src.codegen.visitor import CodeGenVisitor


class CodeGenerator:
    def __init__(self, vmem, cpool, vpool, ptree):
        self.memory = vmem
        self.vpool = vpool
        self.cpool = cpool
        self.ptree = ptree

    def generate_vm_code(self):
        cg = CodeGenVisitor(self)
        cg.visit(self.ptree.commands)
        return cg.code

