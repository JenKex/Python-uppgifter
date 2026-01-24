ticket_price = 100  # biljettpris
available_money = 200  # pengar på fickan
# Behöver konvertera variablerna till en sträng för att printa dem.
# Behöver lägga till ett plustecken mellan variablerna och andra delen av strängen.
print("Det blir " + str((available_money - ticket_price)) + " kronor över.")
# Separerar ut 'z = y -x / 2' i flera variabler för att undvika oförklarade magic numbers (tvåan).
leftover_money = int(available_money - ticket_price)
amount_of_people = 2
# Behöver konvertera variabeln till en sträng, återigen, för att printa den.
print("Det finns " + str(amount_of_people) + " personer.")
print("Varje person får " + str(leftover_money / amount_of_people) + " kronor.")
