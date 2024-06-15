PILESHKO_MENU_CENA = 10.35
RIBNO_MENU_CENA = 12.40
VEGAN_MENU_CENA = 8.15
DOSTAVKA = 2.50

broi_pileshko_menu = int(input("Брой пилешки менюта: "))
broi_ribno_menu = int(input("Брой рибни менюта: "))
broi_vegan_menu = int(input("Брой вегатариански менюта: "))

pileshko_obshta_cena = broi_pileshko_menu * PILESHKO_MENU_CENA
ribno_obshta_cena = broi_ribno_menu * RIBNO_MENU_CENA
vegan_obshta_cena = broi_vegan_menu * VEGAN_MENU_CENA

obshta_menu_cena = pileshko_obshta_cena + ribno_obshta_cena + vegan_obshta_cena

desert_cena = obshta_menu_cena*0.2

obshta_cena = obshta_menu_cena + desert_cena + DOSTAVKA

# print(f'Обща цена на поръчката: {obshta_cena} лв.')

print(obshta_cena)