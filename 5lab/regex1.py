import re
def zeromorebs(s):
    return bool(re.match(r'a+b*', s))
print(zeromorebs("abgts"))