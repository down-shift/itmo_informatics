def indent_level(s):
    s = s.replace('\n', '')
    return len(s) - len(s.lstrip())


sched = open('lab3/d3210_schedule.yaml').readlines()
xml_sched = ''
print(sched)
for s in sched:
    print(indent_level(s), s.rstrip())