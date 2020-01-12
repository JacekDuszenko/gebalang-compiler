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

        """5 / 2 = 2
            5 / -2 = -3
            -5 / 2 = -3
            -5 / -2 = 2
            7 / 4 = 1
            7 / -4 = -2
            -7 / 4 = -2
            -7 / -4 = 1
"""
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