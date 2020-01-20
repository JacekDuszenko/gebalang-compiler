from test.utils import *


class TestWriteConstant:
    def test_should_generate_valid_constant_20(self):
        simple_program_string = """
                                 BEGIN
                                 WRITE 20;
                                 END
                                 """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 20
        print('cost is: ', cost)

    def test_should_generate_valid_constant_0(self):
        simple_program_string = """
                                    BEGIN
                                    WRITE 0;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 0

    def test_should_generate_valid_constant_minus_500(self):
        simple_program_string = """
                                    BEGIN
                                    WRITE -500;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        print(asm)

        assert int(out[0]) == -500

    def test_should_generate_valid_constant_2_to_62(self):
        two_to_sixty_two = str(2 ** 62)
        simple_program_string = f"""
                                    BEGIN
                                    WRITE {two_to_sixty_two};
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == 2 ** 62
        print('cost is: ', cost)

    def test_should_generate_valid_constant_minus_2_to_62(self):
        two_to_sixty_two = str(-2 ** 62)
        simple_program_string = f"""
                                    BEGIN
                                    WRITE {two_to_sixty_two};
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -2 ** 62

    def test_should_generate_valid_constant_minus_3(self):
        simple_program_string = f"""
                                    BEGIN
                                    WRITE -3;
                                    END
                                    """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        print(asm)
        assert int(out[0]) == -3

    def test_should_generate_valid_constant_couple_times(self):
        simple_program_string = f"""
                                       BEGIN
                                       WRITE -3;
                                       WRITE 1024;
                                       WRITE -103;
                                       WRITE 12;
                                       WRITE 1337;
                                       WRITE 500;
                                       WRITE -8;
                                       WRITE 0;
                                       END
                                       """
        out, err, asm, cost =  run_vm(simple_program_string)
        assert err is b''
        assert int(out[0]) == -3
        assert int(out[1]) == 1024
        assert int(out[2]) == -103
        assert int(out[3]) == 12
        assert int(out[4]) == 1337
        assert int(out[5]) == 500
        assert int(out[6]) == -8
        assert int(out[7]) == 0
