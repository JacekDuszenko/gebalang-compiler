from test.utils import *


class TestWriteConstant:
    def test_should_write_valid_value(self):
        simple_program_string = """
                                 DECLARE a, b(-50:50) BEGIN
                                 a ASSIGN 25;
                                 b(25) ASSIGN 10;
                                 WRITE b(a);
                                 a ASSIGN 10;
                                 WRITE b(25);
                                 b(10) ASSIGN 1337;
                                 WRITE b(a);
                                 END
                                 """
        out, err, asm = run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 10
        assert int(out[1]) == 10
        assert int(out[2]) == 1337

    def test_should_write_valid_array_val(self):
        simple_program_string = """
                                 DECLARE a, b(-2:2) BEGIN
                                 b(-2) ASSIGN 10;
                                 b(-1) ASSIGN 9;
                                 b(0) ASSIGN 8;
                                 b(1) ASSIGN 7;
                                 b(2) ASSIGN 6;
                                 
                                 READ a;WRITE b(a);
                                 READ a;WRITE b(a);
                                 READ a;WRITE b(a);
                                 READ a;WRITE b(a);
                                 READ a;WRITE b(a);
                                 END
                                 """
        input = b'-2 -1 0 1 2'
        out, err, asm = run_vm(simple_program_string,input=input)
        assert err is b''
        assert int(out[0]) == 10
        assert int(out[1]) == 9
        assert int(out[2]) == 8
        assert int(out[3]) == 7
        assert int(out[4]) == 6

    def test_should_read_valid_value(self):
        simple_program_string = """
                                 DECLARE a, b(-1:2) BEGIN
                                 a ASSIGN -1;
                                 READ b(a);
                                 WRITE b(a);
                                 
                                 a ASSIGN 0;
                                 READ b(a);
                                 WRITE b(a);
                                 
                                 a ASSIGN 1;
                                 READ b(a);
                                 WRITE b(a);
                                 
                                 a ASSIGN 2;
                                 READ b(a);
                                 WRITE b(a);
                                 END
                                 """
        input = b'15 -50 200000 -1333333333'
        out, err, asm = run_vm(simple_program_string, input=input)
        assert err is b''
        assert int(out[0]) == 15
        assert int(out[1]) == -50
        assert int(out[2]) == 200000
        assert int(out[3]) == -1333333333

    def test_should_assign_valid_value(self):
        simple_program_string = """
                                 DECLARE a, c, b(-5:5) BEGIN
                                 READ c;
                                 READ b(c);
                                 a ASSIGN b(c);
                                 WRITE a;
                                 
                                  READ c;
                                 READ b(c);
                                 a ASSIGN b(c);
                                 WRITE a;
                                 
                                  READ c;
                                 READ b(c);
                                 a ASSIGN b(c);
                                 WRITE a;
                                 END
                                 """
        input = b'0 50 5 123 -5 -500'
        out, err, asm = run_vm(simple_program_string, input=input)
        assert err is b''
        assert int(out[0]) == 50
        assert int(out[1]) == 123
        assert int(out[2]) == -500

    def test_should_assign_array_variable_on_left_valid_value(self):
        simple_program_string = """
                                 DECLARE a, b(-5:10), c, d(-3:100), e BEGIN
                                 READ a;
                                 b(a) ASSIGN -50000;
                                 WRITE b(a);
                                 
                                 READ c;
                                 b(a) ASSIGN c;
                                 WRITE b(a);
                                 
                                 READ e;
                                 READ d(e);
                                 b(a) ASSIGN d(e);
                                 WRITE b(a);
                                 END
                                 """
        input = b'0 420 100 -321'
        out, err, asm = run_vm(simple_program_string, input=input)
        print(asm)
        assert err is b''
        assert int(out[0]) == -50000
        assert int(out[1]) == 420
        assert int(out[2]) == -321


