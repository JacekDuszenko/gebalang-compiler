from src.codegen.create_constant import create_constant_number
from test.utils import remove_whitespace


class TestCreateConstants:
    def test_should_create_valid_constant_20(self):
        valid = """
        SUB 0 
        INC 
        ADD 0
        ADD 0
        INC
        ADD 0
        ADD 0
        """
        assembly = create_constant_number(20)
        formatted_valid = remove_whitespace(valid)
        formatted_assembly = remove_whitespace(assembly)
        assert formatted_assembly == formatted_valid

    def test_should_create_valid_constant_13(self):
        valid = """
        SUB 0 
        INC 
        ADD 0
        INC
        ADD 0
        ADD 0
        INC
        """
        assembly = create_constant_number(13)
        formatted_valid = remove_whitespace(valid)
        formatted_assembly = remove_whitespace(assembly)
        assert formatted_assembly == formatted_valid

    def test_should_create_valid_constant_0(self):
        valid = """
        SUB 0
        """
        assembly = create_constant_number(0)
        formatted_valid = remove_whitespace(valid)
        formatted_assembly = remove_whitespace(assembly)
        assert formatted_assembly == formatted_valid

    def test_should_create_valid_constant_negative_156(self):
        valid = """
        SUB 0
        DEC
        ADD 0
        ADD 0
        ADD 0
        DEC
        ADD 0
        DEC
        ADD 0
        DEC
        ADD 0
        ADD 0
        """
        assembly = create_constant_number(-156)
        formatted_valid = remove_whitespace(valid)
        formatted_assembly = remove_whitespace(assembly)
        assert formatted_assembly == formatted_valid

    def test_should_create_valid_constant_2_to_62(self):
        valid = "SUB 0" + "INC" + ("ADD 0 " * 62)
        assembly = create_constant_number(2 ** 62)
        formatted_valid = remove_whitespace(valid)
        formatted_assembly = remove_whitespace(assembly)
        assert formatted_assembly == formatted_valid

    def test_should_create_valid_constant_2_to_minus_62(self):
        valid = "SUB 0" + "DEC" + ("ADD 0 " * 62)
        assembly = create_constant_number(-2 ** 62)
        formatted_valid = remove_whitespace(valid)
        formatted_assembly = remove_whitespace(assembly)
        assert formatted_assembly == formatted_valid