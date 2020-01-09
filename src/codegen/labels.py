EXEC_START = 'EXEC_START'
EXEC_END = 'EXEC_END'
COND_EVAL_START = 'COND_EVAL_START'


def exec_start_label(id):
    return f'#{EXEC_START}_{id}\n'


def exec_end_label(id):
    return f'#{EXEC_END}_{id}\n'


def cond_eval_start_label(id):
    return f'#{COND_EVAL_START}_{id}\n'
