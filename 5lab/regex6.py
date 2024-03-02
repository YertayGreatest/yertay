import re
def replacewithcolon(s):
    pattern = r'[ .,]'
    newtext = re.sub(pattern, ":", s)
    return newtext
print(replacewithcolon("this is, tex.t"))