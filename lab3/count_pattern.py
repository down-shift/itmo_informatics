import re


def count_pattern(s, pattern):
    return len(re.findall(pattern=pattern, string=s))


pattern = r'X-\('
tests = ['aezropX-(gl', 'YX-X-(()X-(', '', 'X--(X(X-(X-(', 'abcdefux-(abc']
correct = [1, 2, 0, 2, 0]
print(*[count_pattern(s=s, pattern=pattern) for s in tests])
print(*correct)