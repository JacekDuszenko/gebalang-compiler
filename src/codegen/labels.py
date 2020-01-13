EXEC_START = 'EXEC_START'
EXEC_END = 'EXEC_END'
COND_EVAL_START = 'COND_EVAL_START'
EXEC_ELSE = 'EXEC_ELSE'
START_LOOP = 'START_LOOP'
END_LOOP = 'END_LOOP'

MUL_START_LABEL = 'MUL_START'
MUL_ZERO_LABEL = 'MUL_ZERO'
MUL_DONE_LABEL = 'MUL_DONE'
MUL_L_EVEN_LABEL = 'MUL_L_EVEN'
MUL_L_ODD_LABEL = 'MUL_L_ODD'
MUL_DONE_NEG_RESULT_LABEL = 'MUL_DONE_NEG_RESULT'
MUL_LEFT_POSITIVE_LABEL = 'MUL_LEFT_POSITIVE'
MUL_RIGHT_POSITIVE_LABEL = 'MUL_RIGHT_POSITIVE'
MUL_DO_NOT_SWAP_LABEL = 'MUL_DO_NOT_SWAP'

DIV_ZERO_LABEL = 'DIV_ZERO'
DIV_OUTER_LOOP_LABEL = 'DIV_OUTER_LOOP'
DIV_FINALIZE_LABEL = 'DIV_FINALIZE'
DIV_MAX_TWO_POW_LABEL = 'MAX_TWO_POW'
DIV_MAX_TWO_POW_RELOOP_LABEL = 'MAX_TWO_POW_RELOOP'
DIV_MAX_TWO_POW_EXIT_LABEL = 'MAX_TWO_POW_EXIT'

DIV_ISNEG_RNEG_LABEL = 'ISNEG_RNEG'
DIV_ISNEG_LNEG_LABEL = 'ISNEG_LNEG'
DIV_ISNEG_BOTH_NEG_LABEL = 'ISNEG_BOTH_NEG'
DIV_ISNEG_END_LABEL = 'ISNEG_END'

DIV_NOTHING_TO_BE_DONE_IN_FINALIZE = 'NOTHING_TO_BE_DONE_IN_FINALIZE'
MOD_REMAINDER_NEGATIVE = 'REMAINDER_NEGATIVE'
MOD_END_REMAINDER_NEGATIVE_CHECK = 'REMAINDER_NEGATIVE_CHECK_END'
MOD_REM_POSITIVE = 'REM_POSITIVE'
MOD_DO_NOT_COMPLEMENT = 'DO_NOT_COMPLEMENT'
REM_MUST_BE_NEG = 'REM_MUST_BE_NEG'
REM_FIXING_END = 'REM_FIXING_END'


def rem_fixing_end_label(id):
    return f'#{REM_FIXING_END}_{id}\n'


def rem_must_be_neg_label(id):
    return f'#{REM_MUST_BE_NEG}_{id}\n'


def mod_do_not_complement_label(id):
    return f'#{MOD_DO_NOT_COMPLEMENT}_{id}\n'


def mod_rem_positive_label(id):
    return f'#{MOD_REM_POSITIVE}_{id}\n'


def mod_end_remainder_negative_check_label(id):
    return f'#{MOD_END_REMAINDER_NEGATIVE_CHECK}_{id}\n'


def mod_remainder_negative_label(id):
    return f'#{MOD_REMAINDER_NEGATIVE}_{id}\n'


def div_nothing_to_be_done_in_finalize_label(id):
    return f'#{DIV_NOTHING_TO_BE_DONE_IN_FINALIZE}_{id}\n'


def div_isneg_end_label(id):
    return f'#{DIV_ISNEG_END_LABEL}_{id}\n'


def div_isneg_both_neg_label(id):
    return f'#{DIV_ISNEG_BOTH_NEG_LABEL}_{id}\n'


def div_isneg_lneg_label(id):
    return f'#{DIV_ISNEG_LNEG_LABEL}_{id}\n'


def div_isneg_rneg_label(id):
    return f'#{DIV_ISNEG_RNEG_LABEL}_{id}\n'


def div_max_two_pow_exit_label(id):
    return f'#{DIV_MAX_TWO_POW_EXIT_LABEL}_{id}\n'


def div_max_two_pow_reloop_label(id):
    return f'#{DIV_MAX_TWO_POW_RELOOP_LABEL}_{id}\n'


def div_max_two_pow_label(id):
    return f'#{DIV_MAX_TWO_POW_LABEL}_{id}\n'


def div_finalize_label(id):
    return f'#{DIV_FINALIZE_LABEL}_{id}\n'


def div_outer_loop_label(id):
    return f'#{DIV_OUTER_LOOP_LABEL}_{id}\n'


def div_zero_label(id):
    return f'#{DIV_ZERO_LABEL}_{id}\n'


def mul_do_not_swap_label(id):
    return f'#{MUL_DO_NOT_SWAP_LABEL}_{id}\n'


def mul_right_positive_label(id):
    return f'#{MUL_RIGHT_POSITIVE_LABEL}_{id}\n'


def mul_left_positive_label(id):
    return f'#{MUL_LEFT_POSITIVE_LABEL}_{id}\n'


def mul_l_odd_label(id):
    return f'#{MUL_L_ODD_LABEL}_{id}\n'


def mul_l_even_label(id):
    return f'#{MUL_L_EVEN_LABEL}_{id}\n'


def mul_start_label(id):
    return f'#{MUL_START_LABEL}_{id}\n'


def mul_done_neg_result_label(id):
    return f'#{MUL_DONE_NEG_RESULT_LABEL}_{id}\n'


def mul_done_label(id):
    return f'#{MUL_DONE_LABEL}_{id}\n'


def mul_zero_label(id):
    return f'#{MUL_ZERO_LABEL}_{id}\n'


def exec_start_label(id):
    return f'#{EXEC_START}_{id}\n'


def exec_end_label(id):
    return f'#{EXEC_END}_{id}\n'


def exec_else_label(id):
    return f'#{EXEC_ELSE}_{id}\n'


def cond_eval_start_label(id):
    return f'#{COND_EVAL_START}_{id}\n'


def start_loop_label(id):
    return f'#{START_LOOP}_{id}\n'


def end_loop_label(id):
    return f'#{END_LOOP}_{id}\n'


def resolve_labels(code):
    lines = code.split('\n')
    label_map = create_label_map(lines)
    inject_labels(lines, label_map)
    return '\n'.join(lines)


def inject_labels(lines, label_map):
    for i, l in enumerate(lines):
        if is_jump(l):
            [instr, label] = l.split('#')
            jump_addr = label_map[label]
            lines[i] = f'{instr} {jump_addr}'


def create_label_map(lines):
    lines_with_ctr = create_lines_with_ctr(lines)
    m = {}
    for index, (l, k) in enumerate(lines_with_ctr):
        if is_label(l):
            label = l.split('#')[1]
            m[label] = k
    return m


def create_lines_with_ctr(lines):
    with_ctr = []
    ctr = 0
    for l in lines:
        with_ctr.append((l, ctr))
        if not is_label(l):
            ctr += 1
    return with_ctr


def is_label(l):
    return l.startswith('#')


def is_jump(l):
    return l.startswith('JUMP') or \
           l.startswith('JPOS') or \
           l.startswith('JZERO') or \
           l.startswith('JNEG')
