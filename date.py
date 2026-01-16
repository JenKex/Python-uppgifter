from datetime import timedelta, datetime

date_today = datetime.now()
date_in_a_week = datetime.now() + timedelta(7)

print(date_today)
print(date_in_a_week)