EXEC_START = 'EXEC_START'
EXEC_END = 'EXEC_END'
COND_EVAL_START = 'COND_EVAL_START'


def exec_start_label(id):
    return f'#{EXEC_START}_{id}\n'


def exec_end_label(id):
    return f'#{EXEC_END}_{id}\n'


def cond_eval_start_label(id):
    return f'#{COND_EVAL_START}_{id}\n'


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
