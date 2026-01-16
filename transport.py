distance = 470
speed = int(input("Hur fort ska du köra i km/h?"))
total_time = distance / speed
total_time_in_minutes = total_time * 60
# total_time_no_decimals = round(total_time)
# total_time_in_minutes_no_decimals = round(total_time_in_minutes)
total_time_no_decimals = distance // speed
total_time_in_minutes_no_decimals = distance // speed * 60
print(f"Det tar totalt: {total_time_no_decimals}")