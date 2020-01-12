from test.utils import *


class TestBinaryExpressionVariablePlusMinus:
    def test_should_add_two_variables(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  b ASSIGN a PLUS 10;
                                  WRITE b;
                                  END
                                 """
        inp=b'10'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 20

    def test_should_subtract_two_variables(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  b ASSIGN a MINUS 10;
                                  WRITE b;
                                  END
                                 """
        inp=b'10'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 0

    def test_should_add_two_variables_reverse_sequence(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  b ASSIGN -40 PLUS a ;
                                  WRITE b;
                                  END
                                 """
        inp=b'10'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == -30

    def test_should_subtract_two_variables_reverse_sequence(self):
        simple_program_string = """
                                  DECLARE a,b BEGIN
                                  READ a;
                                  b ASSIGN -40 MINUS a;
                                  WRITE b;
                                  END
                                 """
        inp=b'40'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == -80

    def test_should_add_two_vars(self):
        simple_program_string = """
                                  DECLARE a,b,c BEGIN
                                  READ a;
                                  READ b;
                                  c ASSIGN a PLUS b;
                                  WRITE c;
                                  END
                                 """
        inp=b'1 2'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 3

    def test_should_subtract_two_vars(self):
        simple_program_string = """
                                     DECLARE a,b,c BEGIN
                                     READ a;
                                     READ b;
                                     c ASSIGN a MINUS b;
                                     WRITE c;
                                     END
                                    """
        inp = b'1 2'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == -1

    def test_should_add_two_array_access_vars(self):
        simple_program_string = """
                                     DECLARE a,b(2:5),c BEGIN
                                     READ a;
                                     READ b(5);
                                     c ASSIGN a PLUS b(5);
                                     WRITE c;
                                     END
                                    """
        inp = b'1 15'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 16

    def test_should_subtract_two_array_constant_access_vars(self):
        simple_program_string = """
                                     DECLARE a,b(2:5),c BEGIN
                                     READ a;
                                     READ b(5);
                                     c ASSIGN a PLUS b(5);
                                     WRITE c;
                                     END
                                    """
        inp = b'1 0'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 1

    def test_should_add_array_variable_access(self):
        simple_program_string = """
                                     DECLARE a,b(2:5),c,d BEGIN
                                     READ a;
                                     READ b(a);
                                     READ c;
                                     d ASSIGN c PLUS b(a);
                                     WRITE d;
                                     END
                                    """
        inp = b'3 100 -100'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 0

    def test_should_subtract_array_variable_access(self):
        simple_program_string = """
                                     DECLARE a,b(2:5),c,d BEGIN
                                     READ a;
                                     READ b(a);
                                     READ c;
                                     d ASSIGN c MINUS b(a);
                                     WRITE d;
                                     END
                                    """
        inp = b'3 100 -100'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == -200

    def test_should_subtract_array_variable_access_2(self):
        simple_program_string = """
                                     DECLARE a,b(0:5),c,d,e BEGIN
                                     READ a;
                                     READ b(a);
                                     READ c;
                                     READ e;
                                     d ASSIGN c MINUS b(a);
                                     WRITE d;
                                     d ASSIGN 2 PLUS e;
                                     WRITE d;
                                     d ASSIGN d PLUS d;
                                     WRITE d;
                                     END
                                    """
        inp = b'0 0 0 2'
        out, err, asm, cost =  run_vm(simple_program_string, input=inp)
        assert err is b''
        assert int(out[0]) == 0
        assert int(out[1]) == 4
        assert int(out[2]) == 8

    def test_incrementation(self):
        simple_program_string = """
                                     DECLARE a BEGIN
                                     a ASSIGN 0;
                                     WRITE a;
                                     a ASSIGN a PLUS 1;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                     END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0
        assert int(out[1]) == 1
        assert int(out[2]) == 2
        assert int(out[3]) == 4
        assert int(out[4]) == 8
        assert int(out[5]) == 16
        assert int(out[6]) == 32
        assert int(out[7]) == 64

    def test_decrementation(self):
        simple_program_string = """
                                     DECLARE a BEGIN
                                     a ASSIGN 0;
                                     WRITE a;
                                     a ASSIGN a MINUS 1;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                      a ASSIGN a PLUS a;
                                     WRITE a;
                                     END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0
        assert int(out[1]) == -1
        assert int(out[2]) == -2
        assert int(out[3]) == -4
        assert int(out[4]) == -8
        assert int(out[5]) == -16
        assert int(out[6]) == -32
        assert int(out[7]) == -64