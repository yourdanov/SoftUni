PAKET_HIMIKALI_CENA = 5.8
PAKET_MARKERI_CENA = 7.2
PREPARAT_CENA_ZA_LITAR = 1.2

broi_himikali = int(input("Брой химикали: "))
broi_markeri = int(input("Брой маркери: "))
litri_preparat = int(input("Литри препарат: "))
namalenie = int(input("Процент намаление: "))

cena_himikali = broi_himikali * PAKET_HIMIKALI_CENA
cena_markeri = broi_markeri * PAKET_MARKERI_CENA
cena_preparat = litri_preparat * PREPARAT_CENA_ZA_LITAR
obshta_cena = cena_himikali + cena_markeri + cena_preparat
cena_s_namalenie = obshta_cena - (obshta_cena * (namalenie/100))

# print(f'Обща цена с намаление: {cena_s_namalenie} лв.')

print(cena_s_namalenie)