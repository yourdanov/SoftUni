broi_stranici = int(input("Брой страници в текущата книга:"))
stranici_za_chas = int(input("Брой страници, който прочита за час:"))
broi_dni = int(input("Брой дни:"))

obshto_vreme_za_chetene_na_knigata = broi_stranici / stranici_za_chas
neobhodimi_chasove_na_den = obshto_vreme_za_chetene_na_knigata / broi_dni

print(int(neobhodimi_chasove_na_den))
