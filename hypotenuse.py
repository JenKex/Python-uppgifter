import math

first_side = int(input("Hur lång är första sidan på triangeln?"))
second_side = int(input("Hur lång är andra sidan på triangeln?"))
third_side = math.sqrt(first_side ** 2 + second_side ** 2)
print(third_side)