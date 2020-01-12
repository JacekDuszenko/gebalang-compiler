from test.utils import *


class TestForUpTo:
    def test_nested_for(self):
        simple_program_string = """
                               DECLARE a,b,c
                                BEGIN
                                    READ a;
                                    READ b;
                                    FOR i FROM 0 TO a DO
                                        FOR j FROM 0 TO b DO
                                            c ASSIGN i PLUS j;
                                            WRITE c;
                                        ENDFOR
                                    ENDFOR
                                END
                                 """
        inp=b'10 20 '
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 11 * 21

    def test_array_ass(self):
        simple_program_string = """
                               DECLARE a(-1024:1024)
                                BEGIN
                                    FOR i FROM -1024 TO 1024 DO
                                        a(i) ASSIGN i;
                                    ENDFOR
                                    
                                    FOR i FROM -1024 TO 1024 DO
                                    WRITE a(i);
                                    ENDFOR
                                END
                                 """
        inp=b'10 20 '
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 2049
        for i, a in enumerate(range(-1024,1025)):
            assert int(out[i]) == a

    def test_variable_change(self):
        simple_program_string = """
                               DECLARE a, b BEGIN
                               READ a;
                               READ b;
                                    FOR i FROM a TO b DO
                                        WRITE i;
                                        b ASSIGN b PLUS 1;
                                    ENDFOR
                                END
                                 """
        inp = b'0 100'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 101
        valid_i = 0
        for i in out:
            assert int(i) == valid_i
            valid_i += 1

