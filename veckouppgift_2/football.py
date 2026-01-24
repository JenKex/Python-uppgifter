print("Matchen är över! Nu ska vi räkna.")
tottenham_goals = int(input("Hur många mål gjorde Tottenham? "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool? "))

if tottenham_goals > liverpool_goals:
    print("Tottenham vann med " + str(tottenham_goals - liverpool_goals) + " mål!")
elif tottenham_goals == liverpool_goals:
    print("Det blev oavgjort! :I")
else:
    print("Liverpool vann med " + str(liverpool_goals - tottenham_goals) + " mål!")

# Värden: Tottenham: 4, Liverpool: 2
# Tottenham: 1, Liverpool: 1
# Tottenham: 1, Liverpool: 3