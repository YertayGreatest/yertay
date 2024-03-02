import re
def seperateupper(s):
    temp = re.findall(r'[A-Z][^A-Z]*', s)
    return temp
print(seperateupper("HelloAlcoFear"))