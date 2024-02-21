from datetime import datetime
def differenceinseconds(date1, date2):
    diff = date1 - date2
    return int(diff.total_seconds())
date1 = datetime(24, 10, 26, 4, 10, 58)
date2 = datetime(24, 10, 25, 3, 45, 5)
#date1 > date2
print(differenceinseconds(date1, date2))
