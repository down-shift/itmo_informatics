import re


def extract_domain(s):
    if not re.search('@', s):
        return 'Fail!'
    address = s[:re.search('@', s).start()]
    clean_address = re.sub(r'[^A-Za-z0-9_.]', '', address)
    domain = s[re.search('@', s).end():]
    clean_domain = re.sub(r'[^A-Za-z.]', '', domain)
    if address != clean_address or domain != clean_domain or not re.search('\w\.\w', domain):
        return 'Fail!'
    return domain
    


print(extract_domain('0_a_a_b@cc.vdf'))  # cc.vdf
print(extract_domain('aabcc.vdf'))       # Fail!
print(extract_domain('u8gu82wgh@.'))     # Fail!
print(extract_domain('aaa._.@a.a'))      # a.a
print(extract_domain('._.@ya.ru'))       # ya.ru