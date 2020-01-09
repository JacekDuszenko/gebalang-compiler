ID_COUNTER = 0


def get_id():
    global ID_COUNTER
    ID_COUNTER += 1
    return ID_COUNTER
