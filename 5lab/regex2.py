import re
def twoorthree(s):
    pattern = r"a(b{2}|b{3})$"
    return bool(re.match(pattern, s))
print(twoorthree("abb"))