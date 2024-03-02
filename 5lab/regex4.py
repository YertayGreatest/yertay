import re
def upperthenlower(s):
    pattern = r"[A-Z]{1,}[a-z].+[a-z]"
    x = re.findall(pattern, s)
    if x:
        return x
    else:
        return None
print(upperthenlower("SasdadsA"))