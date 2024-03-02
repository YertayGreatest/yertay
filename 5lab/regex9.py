import re
def insertspaces(s):
    temp = re.findall(r'[A-Z][^A-Z]*', s)
    res = " ".join(temp)
    return res
print(insertspaces("HelloAlcoMass"))