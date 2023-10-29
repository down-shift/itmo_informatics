import re


def extract_domain(email):
    """
    Check if an email address is valid. 
    
    Mail address can contain letters, numbers, dots (.) and underscores (_).
    Server address can contain letters, dots (.) and a top-level domain.
    """
    pattern = r'([a-zA-Z0-9._]+)@([a-zA-Z]+).([a-zA-Z]{2,})'
    if re.match(pattern, email):
        return re.sub(r'([a-zA-Z0-9._]+)@', '', email)
    return 'Fail!'
    

# Examples
print(extract_domain('0_a_a_b@cc.vdf'))  # cc.vdf
print(extract_domain('aabcc.vdf'))       # Fail!
print(extract_domain('u8gu82wgh@.'))     # Fail!
print(extract_domain('aaa._.@a.a'))      # Fail!
print(extract_domain('._.@ya.ru'))       # ya.ru