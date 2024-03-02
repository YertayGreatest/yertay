import re
def cameltosnake(s):    
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    return s
print(cameltosnake("camelCase"))
