from test.utils import *


class TestDiv:
    def test_zero_div(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'2 0'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

    def test_normal_div(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'6 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 3

    def test_cut_div(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'7 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 3

    def test_some_more_numbers(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'35 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 17

        a = b'123456789 34'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 3631082

        a = b'102 8'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 12

        a = b'123123123 1'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 123123123

        a = b'3 5'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

    def test_cut_div_neg(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'7 -2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -4

    def test_cut_div_neg_swapped_signs(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'-7 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -4

    def test_div_double_neg(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                END
                                 """
        a = b'-7 -2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 3

    def test_div_more_numbers(self):
        simple_program_string = """
                                        DECLARE a, b, c BEGIN
                                        READ a;
                                        READ b;
                                        c ASSIGN a DIV b;
                                        WRITE c;
                                        END
                                         """
        a = b'5 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 2

        a = b'5 -2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -3

        a = b'-5 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -3

        a = b'-5 -2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 2

        a = b'7 4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1

        a = b'7 -4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -2

        a = b'-7 4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -2

        a = b'-7 -4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1

    def test_zero_left(self):
        simple_program_string = """
                                        DECLARE a, b, c BEGIN
                                        READ a;
                                        READ b;
                                        c ASSIGN a DIV b;
                                        WRITE c;
                                        END
                                         """
        a = b'0 5'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

    def test_equal_stuff(self):
        simple_program_string = """
                                        DECLARE a, b, c BEGIN
                                        READ a;
                                        READ b;
                                        c ASSIGN a DIV b;
                                        WRITE c;
                                        END
                                         """
        a = b'17 17'

        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1

    def test_ina_loop(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                FOR i FROM 0 TO 3 DO
                                READ a;
                                READ b;
                                c ASSIGN a DIV b;
                                WRITE c;
                                ENDFOR
                                END
                                 """
        # a = b'-7 -2 0 5 121 11 17 17'
        a = b'0 5 0 5 121 11 17 17'

        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0
        assert int(out[1]) == 0
        assert int(out[2]) == 11
        assert int(out[3]) == 1
