import re

def snaketocamel(s):
    te = re.split(r'_+', s)
    result = te[0] + ''.join(map(lambda x: x.title(), te[1:]))
    return result
print(snaketocamel("aa_asd_sds_ads"))


