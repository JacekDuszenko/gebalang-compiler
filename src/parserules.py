from src.ast_model.command import WhileCommand
from src.ast_model.program import *
from src.parse.cmd import *
from src.parse.commands import *
from src.parse.declaration import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left, TIMES', 'DIV', 'MOD')
)


def p_program(p):
    """
    program : DECLARE declarations BEGIN commands END
            | BEGIN commands END
    """
    if len(p) == 6:
        p[0] = Program(p[2], p[4])
    else:
        p[0] = Program(Declarations(), p[2])


def p_declarations_variables(p):
    """
    declarations : declarations COMMA ID
                 | ID
    """
    if len(p) == 4:
        append_variable_declaration(p)
    else:
        create_declarations_with_variable(p)


def p_declarations_arrays(p):
    """
    declarations : declarations COMMA ID LP NUM COLON NUM RP
                 | ID LP NUM COLON NUM RP
    """
    if len(p) == 9:
        append_array_declaration(p)
    else:
        create_declarations_with_array(p)


def p_commands(p):
    """
    commands : commands command
             | command
    """
    if len(p) == 3:
        append_command(p)
    else:
        create_commands(p)


def p_command_assign(p):
    """
    command : identifier ASSIGN expression SEMICOLON
    """
    create_assign_command(p)


def p_command_if_then(p):
    """
    command : IF condition THEN commands ENDIF
    """
    create_if_then_command(p)


def p_command_if_then_else(p):
    """
    command : IF condition THEN commands ELSE commands ENDIF
    """
    create_if_then_else_command(p)


def p_command_while(p):
    """
    command : WHILE condition DO commands ENDWHILE
    """
    create_while_command(p)

def p_command_do_while(p):
    """
    command : DO commands WHILE condition ENDDO
    """