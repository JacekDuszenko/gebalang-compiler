from test.utils import *


class TestMod:
    def test_mod_(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a MOD b;
                                WRITE c;
                                END
                                 """
        a = b'5 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1

        a = b'5 -2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -1

        a = b'-5 2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1

        a = b'-5 -2'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -1

        a = b'7 4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 3

        a = b'7 -4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -1

        a = b'-7 4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1

        a = b'-7 -4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -3

    def test_mod_edge_cases(self):
        simple_program_string = """
                                        DECLARE a, b, c BEGIN
                                        READ a;
                                        READ b;
                                        c ASSIGN a MOD b;
                                        WRITE c;
                                        END
                                         """
        a = b'5 0'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

        a = b'0 5'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

    def test_mod_in_loop(self):
        simple_program_string = """
                                        DECLARE a, b, c BEGIN
                                        FOR i FROM 0 TO 3 DO
                                        READ a;
                                        READ b;
                                        c ASSIGN a MOD b;
                                        WRITE c;
                                        ENDFOR
                                        END
                                         """
        a = b'7 4 -7 4 7 -4 -7 -4'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 3
        assert int(out[1]) == 1
        assert int(out[2]) == -1
        assert int(out[3]) == -3

