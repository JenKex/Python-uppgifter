# Var lite osäker här på om det gäller '75% av originalpriset' (1500) eller '75% avdraget från priset' (500)', speciellt i sammanhanget av användarinput.
# Skrev koden som att båda gäller X% av originalpriset, men inkluderade utkommenterat kod för det motsatta fallet.
jacka_pris = 2000
rea_procent = 75
slut_pris = jacka_pris * (rea_procent / 100)
print("Jackan på " + str(100 - rea_procent) + "% rea kostar: " + str(slut_pris) + " kronor.")
användar_rea_procent = int(input("Skriv in hur många procent som ska dras av. "))
användar_slut_pris = jacka_pris * ((100 - användar_rea_procent) / 100)
# användar_slut_pris = jacka_pris * ((100 - användar_rea_procent) / 100)
print("Jackans originalpris är: " + str(jacka_pris) + ".")
# test_rea_procent = 90
# test_slut_pris = jacka_pris * (test_rea_procent / 100)
print("Jackan på " + str(användar_rea_procent) + "% rea kostar: " + str(användar_slut_pris) + " kronor.")