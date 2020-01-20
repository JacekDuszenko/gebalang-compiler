import math

ONE_REG = 13
SUM_REG = 14
POW_REG = 15


def place_one_in_onereg():
    code = ""
    code += "SUB 0\n"
    code += "INC\n"
    code += f"STORE {ONE_REG}\n"
    return code

def create_constant_number(num, storage_addr=0):
    return cc(num, storage_addr=storage_addr)

def cc(num, storage_addr=0):
    result = ""
    is_negative = num < 0
    if abs(num) <= 10:
        return small_number(is_negative, num, storage_addr=storage_addr)
    if is_negative:
        num = -num
    while num > 0:
        if num % 2 == 0:
            num //= 2
            result = add_to_itself() + result
        else:
            num -= 1
            result = dec() + result if is_negative else inc() + result
    result = clear_register() + result
    if storage_addr != 0:
        result += store_to_addr(storage_addr)
    return result


def small_number(is_negative, num, storage_addr=0):
    code = "SUB 0\n"
    if is_negative:
        num = -num
    for i in range(num):
        code += "INC\n" if not is_negative else "DEC\n"
    if storage_addr != 0:
        code += f"STORE {storage_addr}\n"
    return code


def store_to_addr(addr):
    return f"STORE {addr}\n"


def clear_register():
    return "SUB 0\n"


def add_to_itself():
    return f"SHIFT {ONE_REG}\n"


def inc():
    return "INC\n"


def dec():
    return "DEC\n"
