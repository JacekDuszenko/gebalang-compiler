from test.utils import *


class TestIfThen:
    def test_should_add_two_variables(self):
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
        inp=b'500 700'
        out, err, asm = run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 500