from test.utils import *


class TestDoWhile:
    def test_1(self):
        simple_program_string = """
                                  DECLARE a BEGIN
                                  READ a;
                                  DO
                                      IF a GEQ 50 THEN
                                      WRITE 10;
                                      ELSE
                                      WRITE 5;
                                      ENDIF
                                      a ASSIGN a PLUS 1;
                                  WHILE a LE 100 ENDDO
                                  END
                                 """
        inp = b'0'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 100
        for i, r in enumerate(out):
            assert int(r) == 5 if i < 50 else 10

    def test_2(self):
        simple_program_string = """
                                  DECLARE a BEGIN
                                  READ a;
                                  DO
                                      IF a GEQ 50 THEN
                                      WRITE 5;
                                      ELSE
                                      WRITE 10;
                                      ENDIF
                                      a ASSIGN a MINUS 1;
                                  WHILE a GE 0 ENDDO
                                  END
                                 """
        inp = b'100'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 100
        for i, r in enumerate(out):
            assert int(r) == 5 if i < 50 else 10

    def test_3(self):
        simple_program_string = """
                                  DECLARE a,b,c BEGIN
                                  READ a;
                                  READ b;
                                  READ c;
                                  
                                  DO
                                    DO
                                      DO
                                        WRITE 1337;
                                        c ASSIGN c PLUS 1;
                                      WHILE c LE 10 ENDDO
                                      b ASSIGN b PLUS 1;
                                      c ASSIGN 0;
                                    WHILE b LE 10 ENDDO
                                    a ASSIGN a PLUS 1;
                                    b ASSIGN 0;
                                  WHILE a LE 10 ENDDO
                                  END
                                 """
        inp = b'0 0 0 '
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert len(out) == 1000
        for o in out:
            assert int(o) == 1337