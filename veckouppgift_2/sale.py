is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)

# Logiskt fel: level1 kommer alltid aktiveras om man skriver in 300, borde vara en elif
# Logiskt fel: discount kommer adderas ihop och kombinera rabatter, om det inte är det man vill borde man sätta discount = [rabatt]
# Logiskt/småfel: Price är större än/lika med på level 2, men inte på level 1. Om man köper en jacka för exakt 100 kronor kommer man inte få rabatten.
if price > level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10
if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
# Småfel: final_price inte konverterad till sträng i originalkoden
print("Efter rabatter blir priset... " + str(final_price))