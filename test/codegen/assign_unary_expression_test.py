from test.utils import *


class TestAssignUnaryExpression:
    def test_should_assign_unary_exprs(self):
        simple_program_string = """
                                 DECLARE a,b,c,d(0:5) BEGIN
                                 READ a;
                                 b ASSIGN a;
                                 d(0) ASSIGN a;
                                 d(1) ASSIGN 123;
                                 d(2) ASSIGN b;
                                 d(3) ASSIGN 0;
                                 d(4) ASSIGN d(3);
                                 d(5) ASSIGN d(0);
                                 
                                 WRITE a;
                                 WRITE b;
                                 WRITE d(0);
                                 WRITE d(1);
                                 WRITE d(2);
                                 WRITE d(3);
                                 WRITE d(4);
                                 WRITE d(5);

                                 END
                                 """
        a = b'1337'
        out, err, asm = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == 1337  # a
        assert int(out[1]) == 1337  # b
        assert int(out[2]) == 1337  # d0
        assert int(out[3]) == 123  # d1
        assert int(out[4]) == 1337  # d2
        assert int(out[5]) == 0  # d3
        assert int(out[6]) == 0  # d4
        assert int(out[7]) == 1337  # d5

    def test_should_reassign(self):
        simple_program_string = """
                                 DECLARE a,b BEGIN
                                 READ a;
                                 b ASSIGN a;
                                 WRITE b;
                                 b ASSIGN -1337;
                                 WRITE b;
                                 a ASSIGN b;
                                 WRITE a;
                                 
                                 END
                                 """
        a = b'-500'
        out, err, asm = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -500
        assert int(out[1]) == -1337
        assert int(out[2]) == -1337

    def test_swap(self):
        simple_program_string = """
                                 DECLARE a,b,c BEGIN
                                 READ a;
                                 READ b;
                                 c ASSIGN b;
                                 b ASSIGN a;
                                 a ASSIGN c;
                                 WRITE a; [should be b]
                                 WRITE b; [should be a]
                                 END
                                 """
        a = b'123 -10001'
        out, err, asm = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -10001
        assert int(out[1]) == 123

    def test_swap_array(self):
        simple_program_string = """
                                 DECLARE a(-1:1) BEGIN
                                 READ a(-1);
                                 READ a(1);
                                 a(0) ASSIGN a(-1);
                                 a(-1) ASSIGN a(1);
                                 a(1) ASSIGN a(0);
                                 
                                 WRITE a(-1); [should be a(1)]
                                 WRITE a(1); [should be a(-1)]
                                 END
                                 """
        a = b'123 -10001'
        out, err, asm = run_vm(simple_program_string, input=a)
        assert err is b''
        assert int(out[0]) == -10001
        assert int(out[1]) == 123
