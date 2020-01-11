from test.utils import *


class TestForDownto:
    def test_nested_for(self):
        simple_program_string = """
                               DECLARE a,b,c
                                BEGIN
                                    READ a;
                                    READ b;
                                    FOR i FROM a DOWNTO 0 DO
                                        FOR j FROM b DOWNTO 0 DO
                                            c ASSIGN i PLUS j;
                                            WRITE c;
                                        ENDFOR
                                    ENDFOR
                                END
                                 """
        inp = b'10 20 '
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 11 * 21

    def test_array_ass(self):
        simple_program_string = """
                               DECLARE a(-1024:1024)
                                BEGIN
                                    FOR i FROM 1024 DOWNTO -1024 DO
                                        a(i) ASSIGN i;
                                    ENDFOR

                                    FOR i FROM 1024 DOWNTO -1024 DO
                                    WRITE a(i);
                                    ENDFOR
                                END
                                 """
        inp = b'10 20 '
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 2049
        for i, a in enumerate(range(1024, -1025, -1)):
            assert int(out[i]) == a

    def test_gebalang_part(self):
        simple_program_string = """
                                  [ loopiii.imp - zagniezdzone petle 
                                0 0 0
                                31000 40900 2222010
                                
                                1 0 2
                                31001 40900 2222012
                            ]
                            DECLARE 
                                a, b, c
                            BEGIN
                                READ a;
                                READ b;
                                READ c;
                                FOR i FROM 111091 TO 111110 DO
                                    FOR j FROM 209 DOWNTO 200 DO
                                        FOR k FROM 11 TO 20 DO
                                            a  ASSIGN  a PLUS k;
                                        ENDFOR
                                        b  ASSIGN  b PLUS j;
                                    ENDFOR
                                    c  ASSIGN  c PLUS i;
                                ENDFOR
                                WRITE a;
                                WRITE b;
                                WRITE c;
                            END

                                         """
        inp = b'0 0 0 '
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 31000
        assert int(out[1]) == 40900
        assert int(out[2]) == 2222010

        inp = b'1 0 2'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 31001
        assert int(out[1]) == 40900
        assert int(out[2]) == 2222012

