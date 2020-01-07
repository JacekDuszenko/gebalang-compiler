def create_constant_number(num, storage_addr=0):
    is_negative = num < 0
    if is_negative:
        num = -num
    result = ""

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


def store_to_addr(addr):
    return f"STORE {addr}\n"


def clear_register():
    return "SUB 0\n"


def add_to_itself():
    return "ADD 0\n"


def inc():
    return "INC\n"


def dec():
    return "DEC\n"
