import math

first_side = float(input("Hur lång är första sidan på triangeln?"))
second_side = float(input("Hur lång är andra sidan på triangeln?"))
third_side = math.sqrt(first_side ** 2 + second_side ** 2)
print("Längden på tredje sidan av triangeln är: " + str(round(third_side)))