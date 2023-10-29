import re 


def extract_domain(s):
    if re.search('@', s):
        # address = s[:re.search('@', s).start()]
        domain = s[re.search('@', s).end():]
        return domain
    return 'Fail!'


print(extract_domain('ab@cc.vdf'))
print(extract_domain('abcc.vdf'))