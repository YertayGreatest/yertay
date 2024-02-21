from datetime import datetime, timedelta
datenow = datetime.today()
dateyesterday = datenow - timedelta(days=1)
datetomorrow = datenow + timedelta(days=1)
print(dateyesterday, datenow, datetomorrow)