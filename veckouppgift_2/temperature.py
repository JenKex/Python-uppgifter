
# fahrenheit_temperature = int(input("Skriv in en temperatur i grader Fahrenheit."))

temperature_unit = str(input("Vill du använda Celsius eller Fahrenheit? Skriv C, för Celsius, eller F, för Fahrenheit. "))

# Kan också göra det här med en y/n och en bool, men blir lite trixigare.
if temperature_unit == "c":
    temperature = float(input("Skriv in en temperatur i grader Celsius. "))
    converted_temperature = (temperature * 9 / 5) + 32
    if converted_temperature < 50:
        print("Det är " + str(converted_temperature) + " grader ute. Se till att ta på dig varma kläder!")
    elif converted_temperature > 68:
        print("Det är " + str(converted_temperature) + " grader ute. Dags att sticka ner till stranden!")
elif temperature_unit == "f":
    temperature = float(input("Skriv in en temperatur i grader Fahrenheit. "))
    converted_temperature = (temperature - 32) * 5 / 9
    if converted_temperature < 10:
        print("Det är " + str(converted_temperature) + " grader ute. Se till att ta på dig varma kläder!")
    elif converted_temperature > 20:
        print("Det är " + str(converted_temperature) + " grader ute. Dags att sticka ner till stranden!")
else: print("Jag förstår inte. :( Kontrollera din stavning och försök igen.")