from test.utils import *


class TestWriteRead:
    def tests_mul(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a TIMES b;
                                WRITE c;
                                END
                                 """
        a = b'2 3'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 6

        a = b'-2 3'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -6

        a = b'2 -3'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -6

        a = b'-2 -3'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 6

        a = b'0 1233123'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

        a = b'12312312 0'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

        a = b'0 0'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 0

        a = b'-817263 918263'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -750462374169

        a = b'-817263 -918263'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 750462374169

    def test_simple_mul(self):
        simple_program_string = """
                            DECLARE a, b, c BEGIN
                            READ a;
                            READ b;
                            c ASSIGN a TIMES b;
                            WRITE c;
                            END
                             """
        a = b'666 15'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 666 * 15

    def test_simple_mul_2(self):
        simple_program_string = """
                            DECLARE a, b, c BEGIN
                            READ a;
                            READ b;
                            c ASSIGN a TIMES b;
                            WRITE c;
                            END
                             """
        a = b'2020320230 123123'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 2020320230 * 123123

    def test_simple_mul_3(self):
        simple_program_string = """
                            DECLARE a, b, c BEGIN
                            READ a;
                            READ b;
                            c ASSIGN a TIMES b;
                            WRITE c;
                            END
                             """
        a = b'-3 7'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -21

    def test_simple_mul_4(self):
        simple_program_string = """
                            DECLARE a, b, c BEGIN
                            READ a;
                            READ b;
                            c ASSIGN a TIMES b;
                            WRITE c;
                            END
                             """
        a = b'-3 -7'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 21

    def test_simple_mul_5(self):
        simple_program_string = """
                            DECLARE a, b, c BEGIN
                            READ a;
                            READ b;
                            c ASSIGN a TIMES b;
                            WRITE c;
                            END
                             """
        a = b'3 -7'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -21

    def test_simple_mul_6(self):
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                WRITE 15;
                                c ASSIGN a TIMES b;
                                WRITE 100;
                                WRITE c;
                                WRITE 2;
                                END
                                 """
        a = b'3 -7'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 15
        assert int(out[1]) == 100
        assert int(out[2]) == -21
        assert int(out[3]) == 2
        print('cost is', cost)

    def test_reverse_cost(self):
        """
        Cost without number swap is 3946
        Cost with number swap is  1040 - works
        """
        simple_program_string = """
                                DECLARE a, b, c BEGIN
                                READ a;
                                READ b;
                                c ASSIGN a TIMES b;
                                WRITE c;
                                END
                                 """
        a = b'123123123 15'
        out, err, asm, cost = run_vm(simple_program_string, input=a)
        assert err is b''
        print('cost is', cost)


