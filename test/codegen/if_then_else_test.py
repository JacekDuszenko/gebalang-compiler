from test.utils import *


class TestIfThenElse:
    def test_ge(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a GE b THEN
                                  WRITE 1;
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'100 -100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1
        inp = b'-100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert len(out) == 1

    def test_le(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a LE b THEN
                                  WRITE 1;
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'100 -100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert len(out) == 1
        inp = b'-100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1

    def test_eq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a EQ b THEN
                                  WRITE 1;
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1
        inp = b'-100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert len(out) == 1

    def test_neq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a NEQ b THEN
                                  WRITE 1;
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert len(out) == 1
        inp = b'-100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1

    def test_leq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a LEQ b THEN
                                  WRITE 1;
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1
        inp = b'-100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1

        inp = b'200 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert len(out) == 1

    def test_geq(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  READ b;
                                  IF a GEQ b THEN
                                  WRITE 1;
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1
        inp = b'-100 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 2
        assert len(out) == 1

        inp = b'200 100'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1
        assert len(out) == 1

    def test_cpx_1(self):
        simple_program_string = """
                                  DECLARE a,b,c,d,e,f,g,h BEGIN
                                  READ a;
                                  READ b;
                                  READ c;
                                  READ d;
                                  READ e;
                                  READ f;
                                  READ g;
                                  READ h;
                                  IF a LE b THEN
                                  IF b LE c THEN
                                  IF c LE d THEN
                                  IF d LE e THEN
                                  IF e LE f THEN
                                  IF f LE g THEN
                                  IF g LE h THEN
                                  WRITE 9;
                                  ELSE 
                                  WRITE 8;
                                  ENDIF
                                  ELSE 
                                  WRITE 7;
                                  ENDIF
                                  ELSE 
                                  WRITE 6;
                                  ENDIF
                                  ELSE
                                  WRITE 5;
                                  ENDIF
                                  ELSE
                                  WRITE 4;
                                  ENDIF
                                  ELSE
                                  WRITE 3;
                                  ENDIF
                                  ELSE
                                  WRITE 2;
                                  ENDIF
                                  END
                                 """
        inp = b'0 1 2 3 4 5 6 7'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 9
        assert len(out) == 1

        inp = b'0 1 2 3 4 5 7 6'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 8
        assert len(out) == 1

        inp = b'0 1 3 2 4 5 6 7'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 4
        assert len(out) == 1