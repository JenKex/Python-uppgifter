from datetime import timedelta, datetime

date_today = datetime.now()
date_in_a_week = datetime.now() + timedelta(7)

print("Dagens datum är: " + date_today)
print("Om en vecka är det: " + date_in_a_week)