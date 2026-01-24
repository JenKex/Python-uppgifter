distance = 470
speed = int(input("Hur fort ska du köra i km/h?"))
total_time = distance / speed
total_time_in_minutes = total_time * 60
# total_time_no_decimals = round(total_time)
# total_time_in_minutes_no_decimals = round(total_time_in_minutes)
# print(f"An example of a format line: {total_time:.2f}.")
total_time_no_decimals = distance // speed
remainder_minutes = int(total_time_in_minutes % 60)

print("Det tar totalt: " + str(round(total_time, 2)) + " timmar exakt.")
print("Det tar totalt: " + str(round(total_time_in_minutes, 2)) + " minuter exakt.")
print(f"Det tar totalt: {total_time_no_decimals} timmar och {remainder_minutes} minuter att åka från Göteborg till Stockholm.")
