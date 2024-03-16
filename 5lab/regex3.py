import re
def lowercaseunder(s):
    x = re.findall(r"[a-z]+_[a-z]+(?:_[a-z]+)*", s)
    if x:
        return "_".join(x)
    else:
        return None
print(lowercaseunder("ssSSd_d_a_v_fSda ads"))   