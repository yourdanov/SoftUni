depozrana_suma = int(input("Депозирина сума:"))
srok_na_depozita = int(input("Срок на депозита в месеци:"))
godishen_lihven_procent = float(input("Годишен лихвен процент:"))

natrupana_lihva = depozrana_suma * (godishen_lihven_procent/100)
lihva_za_1_mesec = natrupana_lihva / 12
obshta_suma = depozrana_suma + srok_na_depozita * lihva_za_1_mesec

print(obshta_suma)