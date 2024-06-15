cena = int(input("Цена на тренировки за една година: "))

kecove = cena - (cena*0.4)
ekip = kecove - (kecove*0.2)
topka = ekip*0.25
aksesoari = topka*0.2

obshta_cena = cena + kecove + ekip + topka + aksesoari

# print(f'Обща цена на тренировки и екипировка: {obshta_cena} лв.')

print(obshta_cena)