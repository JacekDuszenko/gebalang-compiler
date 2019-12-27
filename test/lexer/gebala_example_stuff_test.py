from test.utils import *

ERST = """[ sito Eratostenesa ]
DECLARE
    n, j, sito(2:100)
BEGIN
    n ASSIGN 100;
    FOR i FROM n DOWNTO 2 DO
        sito(i) ASSIGN 1;
    ENDFOR
    FOR i FROM 2 TO n DO
        IF sito(i) NEQ 0 THEN
            j ASSIGN i PLUS i;
            WHILE j LEQ n DO
                sito(j) ASSIGN 0;
                j ASSIGN j PLUS i;
            ENDWHILE
            WRITE i;
        ENDIF
    ENDFOR
END"""


class TestGebalaExampleStuff:
    def test_erst_ok(self):
        simple_program_string = ERST
        with_removed_comment = ERST.replace("[ sito Eratostenesa ]", "")
        valid_string = remove_whitespace(with_removed_comment)
        valid_token_list_values = ['DECLARE', 'n', ',', 'j', ',', 'sito', '(', 2, ':', 100, ')', 'BEGIN', 'n', 'ASSIGN',
                                   100, ';', 'FOR', 'i', 'FROM', 'n', 'DOWNTO', 2, 'DO', 'sito', '(', 'i', ')',
                                   'ASSIGN', 1, ';', 'ENDFOR', 'FOR', 'i', 'FROM', 2, 'TO', 'n', 'DO', 'IF', 'sito',
                                   '(', 'i', ')', 'NEQ', 0, 'THEN', 'j', 'ASSIGN', 'i', 'PLUS', 'i', ';', 'WHILE', 'j',
                                   'LEQ', 'n', 'DO', 'sito', '(', 'j', ')', 'ASSIGN', 0, ';', 'j', 'ASSIGN', 'j',
                                   'PLUS', 'i', ';', 'ENDWHILE', 'WRITE', 'i', ';', 'ENDIF', 'ENDFOR', 'END']
        assert valid_string == lex_to_string(lexer, simple_program_string)
        for i, t in enumerate(lex_to_token_list(lexer, simple_program_string)):
            assert valid_token_list_values[i] == t.value
