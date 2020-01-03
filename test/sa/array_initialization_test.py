import pytest

from src.sa.static_analysis import execute_static_analysis, GebalangException
from test.utils import *


class TestSaArrays:
    def test_valid_initialization_of_arrays(self):
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
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)

    def test_wrong_initialization_of_arrays(self):
        simple_program_string = """
                                DECLARE a(-101:-99) BEGIN
                                READ a(-101);
                                READ a(-100);
                                WRITE a(-101);
                                WRITE a(-100);
                                WRITE a(-99); [this is wrong]
                                END
                                      """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_wrong_initialization_of_arrays_positive_indexes(self):
        simple_program_string = """
                                   DECLARE a(0:2) BEGIN
                                   READ a(0);
                                   READ a(1);
                                   WRITE a(0);
                                   WRITE a(1);
                                   WRITE a(2); [this is wrong]
                                   END
                                         """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_wrong_initialization_of_arrays_mixed_indexes(self):
        simple_program_string = """
                                      DECLARE a(-3:2) BEGIN
                                      READ a(-3);
                                      READ a(0);
                                      WRITE a(-3);
                                      WRITE a(0);
                                      WRITE a(1); [this is wrong]
                                      END
                                            """
        ptree = parse(simple_program_string)
        with pytest.raises(GebalangException):
            execute_static_analysis(ptree)

    def test_correct_initialization_of_arrays_mixed_indexes(self):
        simple_program_string = """
                                         DECLARE a(-3:2) BEGIN
                                         READ a(-3);
                                         READ a(-2);
                                         READ a(-1);
                                         READ a(0);
                                         READ a(1);
                                         READ a(2);
                                         WRITE a(-3);
                                         WRITE a(-2);
                                         WRITE a(-1);
                                         WRITE a(0);
                                         WRITE a(1);
                                         WRITE a(2);
                                         END
                                               """
        ptree = parse(simple_program_string)
        execute_static_analysis(ptree)