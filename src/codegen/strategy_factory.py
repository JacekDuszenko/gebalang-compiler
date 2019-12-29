from src.codegen.strategy import *


def create_visit_strats():
    return [AssignCgStrat(),
            IfThenElseCgStrat(),
            IfThenCgStrat(),
            WhileCgStrat(),
            DoWhileCgStrat(),
            ForUpToCgStrat(),
            ForDownToCgStrat(),
            ReadCgStrat(),
            WriteCgStrat()]


'''
Each strategy appends generated machine code 
'''
