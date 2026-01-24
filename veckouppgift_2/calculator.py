number_1 = int(input("Skriv in ett tal. "))
number_2 = int(input("Skriv in ett tal till. "))
number_3 = int(input("Skriv in ännu ett tal. "))

# Andra metoder: Använd nested ifs

if number_1 == number_2 == number_3:
    print("Alla tal är lika! Det mellersta talet är: " + str(number_2))
elif number_1 == number_2:
    print("Tal 1 är lika stort som tal 2.")
elif number_2 == number_3:
    print("Tal 2 är lika stort som tal 3.")
elif number_3 == number_1:
    print("Tal 3 är lika stort som tal 1.")
if number_1 < number_3 and number_2 < number_3:
    print(str(number_3) + " är störst.")
elif number_3 < number_2 and number_1 < number_2:
    print(str(number_2) + " är störst.")
else:
    print(str(number_1) + " är störst.")

if number_1 < number_2 < number_3 or number_3 < number_2 < number_1:
    print(str(number_2) + " är det mellersta talet.")
elif number_2 < number_3 < number_1 or number_1 < number_3 < number_2:
    print(str(number_3) + " är det mellersta talet.")
elif number_2 < number_1 < number_3 or number_3 < number_1 < number_2:
    print(str(number_1) + " är det mellersta talet.")
print("Summa summarum: " + str(number_1 + number_2 + number_3))