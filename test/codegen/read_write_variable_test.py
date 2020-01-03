from test.utils import *


class TestWriteConstant:
    def test_should_be_ok_couple_variables(self):
        simple_program_string = """
                                 DECLARE a,b,c,d(0:5) BEGIN
                                 READ a;
                                 WRITE a;
                                 READ b;
                                 READ c;
                                 WRITE b;
                                 WRITE c;
                                 READ d(0);
                                 WRITE d(0);
                                 READ d(1);
                                 WRITE d(1);
                                 END
                                 """
        a = b'10 20 30 0 1'
        out, err, asm = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 10
        assert int(out[1]) == 20
        assert int(out[2]) == 30
        assert int(out[3]) == 0
        assert int(out[4]) == 1

    def test_changing_variable_value(self):
        simple_program_string = """
                               DECLARE a 
                               BEGIN
                               READ a;
                               WRITE a;
                               READ a;
                               WRITE a;
                               READ a;
                               WRITE a;
                               END
                                 """
        input_values = b'1337 0 -530'
        out, err, asm = run_vm(simple_program_string, input=input_values)
        assert err is b''
        assert int(out[0]) == 1337
        assert int(out[1]) == 0
        assert int(out[2]) == -530

    def test_changing_array_value(self):
        simple_program_string = """
                               DECLARE a(-101:-99) BEGIN
                               READ a(-101);
                               READ a(-100);
                               READ a(-99);
                               WRITE a(-101);
                               WRITE a(-100);
                               WRITE a(-99);
                               
                               READ a(-101);
                               READ a(-100);
                               READ a(-99);
                               WRITE a(-101);
                               WRITE a(-100);
                               WRITE a(-99);
                               END
                                 """
        input_values = b'1337 0 -530 -1 -2 -3'
        out, err, asm = run_vm(simple_program_string, input=input_values)
        assert err is b''
        assert int(out[0]) == 1337
        assert int(out[1]) == 0
        assert int(out[2]) == -530

        assert int(out[3]) == -1
        assert int(out[4]) == -2
        assert int(out[5]) == -3
