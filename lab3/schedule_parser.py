def indent_level(s):
    s = s.replace('\n', '')
    return len(s) - len(s.lstrip())


def add_indent(s, level):
    return ' ' * level + s


def make_line(tag, contents, ind_level):
    return add_indent(f'<{tag}>{contents.strip()}</{tag}>', ind_level)


def yaml_to_xml(sched):
    """
    Convert a YAML file into an XML file.
    """
    xml_sched = []
    tag_stack = []
    all_tags = []
    for i in range(len(sched)):
        if not sched[i].strip():
            continue
        level = indent_level(sched[i])
        next_level = indent_level(sched[i + 1]) if i + 1 < len(sched) else -1
        line = sched[i].strip()
        if line[0] == '-':
            rest = line[2:]
            xml_sched.append(make_line(all_tags[-1], rest.replace('"', ''), level))
        elif ':' in line:
            # print(i)
            tag = line[:line.index(':')]
            all_tags.append(tag)
            rest = line[line.index(':') + 1:].strip()
            if rest:
                xml_sched.append(make_line(tag, rest.replace('"', ''), level))
            elif sched[i + 1].lstrip()[0] != '-':
                print(i)
                tag_stack.append([level, tag])
                xml_sched.append(add_indent(f'<{tag}>', level))
        if tag_stack:
            if next_level <= tag_stack[-1][0]:
                xml_sched.append(add_indent(f'</{tag_stack[-1][1]}>', tag_stack[-1][0]))
                tag_stack.pop()
    for ind, tag in tag_stack[::-1]:
        xml_sched.append(add_indent(f'</{tag}>', ind))
        tag_stack.pop()
    return '\n'.join(xml_sched)


yaml_sched = open('lab3/d3210_schedule.yaml').readlines()
xml_sched = yaml_to_xml(yaml_sched)
with open('lab3/d3210_schedule.xml', 'w') as f:
    f.write(xml_sched)
print(xml_sched)
