from test.utils import *


class TestBinaryExpression:
    def test_should_add_two_variables(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN 2 PLUS 1;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 3

    def test_should_add_two_variables_one_neg(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN 2 PLUS -5;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -3

    def test_should_add_two_variables_one_zero(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN -10 PLUS 0;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -10

    def test_should_sub_two_variables(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN -10 MINUS -3;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -7

    def test_should_mul_two_variables(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN 1000000 TIMES 100000000;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 1000000 * 100000000

    def test_should_mul_two_variables_one_neg(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN -5 TIMES 15;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -75

    def test_should_mul_two_variables_two_neg(self):
        simple_program_string = """
                                  DECLARE c BEGIN
                                 c ASSIGN -5 TIMES -50;
                                 WRITE c;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 250

    def test_should_mul_two_variables_one_zero(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 0 TIMES 2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0

    def test_div_zero_(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 2343 DIV 0;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0

    def test_mod_zero_(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 2343 MOD 0;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0

    def test_zero_mod_(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 0 MOD 23;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0

    def test_zero_div_(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 0 DIV 223;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0

    def test_div_five_neg_two(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 5 DIV -2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -3

    def test_mod_five_neg_two(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 5 MOD -2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -1

    def test_div_five_two(self):
        simple_program_string = """
                                     DECLARE c BEGIN
                                    c ASSIGN 5 DIV 2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 2

    def test_mod_five_two(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN 5 MOD 2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 1

    def test_neg_five_div_neg_two(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN -5 DIV -2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 2

    def test_neg_five_mod_neg_two(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN -5 MOD -2;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -1

    def test_seven_div_neg_four(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN 7 DIV -4;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -2

    def test_seven_mod_neg_four(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN 7 MOD -4;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -1

    def test_neg_seven_div_four(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN -7 DIV 4;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -2

    def test_neg_seven_mod_four(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN -7 MOD 4;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 1

    def test_neg_seven_div_neg_four(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN -7 DIV -4;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 1

    def test_neg_seven_mod_neg_four(self):
        simple_program_string = """
                                    DECLARE c BEGIN
                                    c ASSIGN -7 MOD -4;
                                    WRITE c;
                                    END
                                    """
        out, err, asm, cost = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -3