import re
def atob(s):
    pattern = r'a{1,}.+b'
    x = re.findall(pattern, s)
    if x:
        return True
    else:
        return False
print(atob("asdadsbdfd"))
#check with .findall()