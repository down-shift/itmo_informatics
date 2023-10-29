def indent_level(s):
    s = s.replace('\n', '')
    return len(s) - len(s.lstrip())


def add_indent(s, level):
    return ' ' * level + s


def make_line(tag, contents, ind_level):
    return add_indent(f'<{tag}>{contents}</{tag}>', ind_level)


sched = open('lab3/d3210_schedule.yaml').readlines()
xml_sched = []
# for s in sched:
#     print(indent_level(s), s.rstrip())
tag_stack = []
for i in range(len(sched)):
    if not sched[i].strip():
        continue
    level = indent_level(sched[i])
    line = sched[i].strip()
    if line[0] == '-':
        continue
    elif ':' in line:
        tag = line[:line.index(':')]
        rest = line[line.index(':') + 1:].strip()
        if rest:
            xml_sched.append(make_line(tag, rest, level))
        else:
            tag_stack.append({level: tag})
            xml_sched.append(add_indent(f'<{tag}>', level))
        print([tag], [rest])
print(*xml_sched, sep='\n')