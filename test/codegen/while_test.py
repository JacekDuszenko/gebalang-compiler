from test.utils import *


class TestWhile:
    def test_1(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  WHILE a LEQ b DO
                                      IF a GEQ 5 THEN
                                      WRITE 1;
                                      ELSE WRITE 2;
                                      ENDIF
                                      a ASSIGN a PLUS 1;                                  
                                  ENDWHILE
                                  END
                                 """
        inp = b'0 10'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert int(out[1]) == 2
        assert int(out[2]) == 2
        assert int(out[3]) == 2
        assert int(out[4]) == 2
        assert int(out[5]) == 1
        assert int(out[6]) == 1
        assert int(out[7]) == 1
        assert int(out[8]) == 1
        assert int(out[9]) == 1
        assert int(out[10]) == 1
        assert len(out) == 11

    # TODO speed it up by caching constants
    def test_2(self):
        simple_program_string = """
                                  DECLARE a(-10000:10000), b, c BEGIN
                                  b ASSIGN -10000;
                                  WHILE b LEQ 10000 DO
                                  a(b) ASSIGN 2;
                                  b ASSIGN b PLUS 1;                      
                                  ENDWHILE
                                  
                                  c ASSIGN -10000;
                                  WHILE c LEQ 10000 DO
                                  WRITE a(c);
                                  c ASSIGN c PLUS 1;
                                  ENDWHILE
                                  END
                                 """
        out, err, asm = run_vm(simple_program_string)
        assert err is b''
        for r in out:
            assert int(r) is 2
        assert len(out) == 20001

    def test_3(self):
        simple_program_string = """
                                     DECLARE b, c, d BEGIN
                                     READ b;
                                     READ c;
                                     d ASSIGN 0;
                                     WHILE b NEQ c DO
                                        WHILE d NEQ 20 DO
                                            WRITE 5;
                                            d ASSIGN d PLUS 1;
                                        ENDWHILE
                                        d ASSIGN 0;
                                        b ASSIGN b PLUS 1;                   
                                     ENDWHILE
                                     END
                                    """
        inp = b'0 10'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        for r in out:
            assert int(r) is 5
        assert len(out) == 20 * 10
