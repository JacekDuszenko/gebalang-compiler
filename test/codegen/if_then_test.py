from test.utils import *


class TestIfThen:
    def test_ge(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a GE b THEN
                                  WRITE 102;
                                  ENDIF
                                  IF b GE a THEN
                                  WRITE 500;
                                  ENDIF
                                  
                                  END
                                 """
        inp = b'500 700'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 500

    def test_le(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a LE b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'500 700'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_eq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a EQ b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'20 20'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_neq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a NEQ b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'20 21'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_leq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a LEQ b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'-50 -49'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_leq_eq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a LEQ b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'-50 -50'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_geq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a GEQ b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'-49 -50'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_geq_eq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a GEQ b THEN
                                  WRITE 5;
                                  ENDIF
                                  WRITE 10;
                                  END
                                 """
        inp = b'-50 -50'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 5
        assert int(out[1]) == 10

    def test_le_neg(self):
        simple_program_string = """
                                     DECLARE a,b BEGIN
                                     READ a;
                                     READ b;
                                     IF a LE b THEN
                                     WRITE 5;
                                     ENDIF
                                     WRITE 10;
                                     END
                                    """
        inp = b'700 500'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 10

    def test_eq_neg(self):
        simple_program_string = """
                                     DECLARE a,b BEGIN
                                     READ a;
                                     READ b;
                                     IF a EQ b THEN
                                     WRITE 5;
                                     ENDIF
                                     WRITE 10;
                                     END
                                    """
        inp = b'21 20'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 10

    def test_neq_neg(self):
        simple_program_string = """
                                     DECLARE a,b BEGIN
                                     READ a;
                                     READ b;
                                     IF a NEQ b THEN
                                     WRITE 5;
                                     ENDIF
                                     WRITE 10;
                                     END
                                    """
        inp = b'0 0'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 10

    def test_leq_neg(self):
        simple_program_string = """
                                     DECLARE a,b BEGIN
                                     READ a;
                                     READ b;
                                     IF a LEQ b THEN
                                     WRITE 5;
                                     ENDIF
                                     WRITE 10;
                                     END
                                    """
        inp = b'-48 -49'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 10

    def test_geq_neg(self):
        simple_program_string = """
                                     DECLARE a,b BEGIN
                                     READ a;
                                     READ b;
                                     IF a GEQ b THEN
                                     WRITE 5;
                                     ENDIF
                                     WRITE 10;
                                     END
                                    """
        inp = b'0 1'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 10

    def test_nested_if_1(self):
        simple_program_string = """
                                     DECLARE a,b,c BEGIN
                                     READ a;
                                     READ b;
                                     READ c;
                                     IF a GE b THEN
                                        WRITE 1;
                                        IF b GE c THEN
                                            WRITE 2;
                                        ENDIF
                                     ENDIF
                                     END
                                    """
        inp = b'2 1 0'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert int(out[1]) == 2

    def test_nested_if_2(self):
        simple_program_string = """
                                     DECLARE a,b,c BEGIN
                                     READ a;
                                     READ b;
                                     READ c;
                                     IF a GE b THEN
                                        WRITE 1;
                                        IF b GE c THEN
                                            WRITE 2;
                                        ENDIF
                                     ENDIF
                                     END
                                    """
        inp = b'2 1 3'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1

    def test_nested_if_3(self):
        simple_program_string = """
                                     DECLARE a,b,c,d,e(0:2) BEGIN
                                     READ a;
                                     READ b;
                                     READ c;
                                     IF a GE b THEN
                                        WRITE 1;
                                     ENDIF
                                     
                                     IF b GE c THEN
                                        d ASSIGN 123;
                                        e(0) ASSIGN 500;
                                     ENDIF
                                     
                                     IF e(0) EQ 500 THEN
                                        WRITE 0;
                                     ENDIF
                                     
                                     IF e(0) EQ 500 THEN
                                      IF a GE b THEN
                                        IF b GE c THEN
                                          IF a GE b THEN
                                            IF e(0) EQ 500 THEN
                                              IF a GE b THEN
                                                WRITE 303;
                                              ENDIF
                                            ENDIF
                                          ENDIF
                                        ENDIF
                                      ENDIF
                                     ENDIF
                                     END
                                    """
        inp = b'10 5 2'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert int(out[1]) == 0
        assert int(out[2]) == 303