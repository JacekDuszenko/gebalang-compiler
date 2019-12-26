from src.util import error, is_in_range, create_not_in_range_message

tokens = (
    # program statements
    'DECLARE', 'BEGIN', 'END', 'COMMA', 'SEMICOLON',
    # identifiers and numbers
    'ID', 'NUM',
    # arrays
    'LP', 'RP', 'COLON',
    # operators
    'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD',
    # conditions
    'EQ', 'NEQ', 'LE', 'GE', 'LEQ', 'GEQ',
    # assignment
    'ASSIGN',
    # control flow
    'IF', 'THEN', 'ELSE', 'ENDIF',
    # while/ do while loops
    'WHILE', 'DO', 'ENDWHILE', 'ENDDO',
    # for loops
    'FOR', 'FROM', 'TO', 'ENDFOR', 'DOWNTO',
    # io
    'READ', 'WRITE'
)


def t_newline(t):
    r'\r?\n+'
    t.lexer.lineno += len(t.value)
    pass


def t_error(t):
    error(t.lexer.lineno, 'Unknown symbol: {}'.format(t.value[0]))
    pass


# numbers
def t_NUM(t):
    r'-?\d+'
    num = int(t.value)
    if not is_in_range(num):
        error(t.lexer.lineno, create_not_in_range_message(num))
    t.value = num
    return t


# ignored signs - ws & comments
t_ignore = ' \t'
t_ignore_COMMENT = r'\[[^\]]*\]'
# program statements
t_DECLARE = r'DECLARE'
t_BEGIN = r'BEGIN'
t_END = r'END'
t_COMMA = r','
t_SEMICOLON = r';'
# io
t_READ = r'READ'
t_WRITE = r'WRITE'
# for loops
t_FOR = r'FOR'
t_FROM = r'FROM'
t_TO = r'TO'
t_ENDFOR = r'ENDFOR'
t_DOWNTO = r'DOWNTO'
# while loops
t_WHILE = r'WHILE'
t_DO = r'DO'
t_ENDWHILE = r'ENDWHILE'
t_ENDDO = r'ENDDO'
# control flow
t_IF = r'IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_ENDIF = r'ENDIF'
# assignment
t_ASSIGN = r'ASSIGN'
# conditions
t_EQ = r'EQ'
t_NEQ = r'NEQ'
t_LE = r'LE'
t_GE = r'GE'
t_LEQ = r'LEQ'
t_GEQ = r'GEQ'
# operators
t_PLUS = r'PLUS'
t_MINUS = r'MINUS'
t_TIMES = r'TIMES'
t_DIV = r'DIV'
t_MOD = r'MOD'
# arrays
t_LP = r'\('
t_RP = r'\)'
t_COLON = r':'
# identifiers
t_ID = r'[_a-z]+'
