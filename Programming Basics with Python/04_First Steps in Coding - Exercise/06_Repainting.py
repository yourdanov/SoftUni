NAILON_CENA = 1.5
BOYA_CENA = 14.50
RAZREDITEL_CENA = 5.0
TORBICHKI_CENA = 0.4

nailon_kolichestvo = int(input("Необходимо количество найлон (кв.м.): "))
boya_kolichestvo = int(input("Необходимо количество боя (литри): "))
razreditel_kolichestvo = int(input("Необходимо количество разредител (литри): "))
chasove = int(input("Часове работа: "))

nailon_suma = (nailon_kolichestvo + 2) * NAILON_CENA
boya_suma = (boya_kolichestvo + (boya_kolichestvo*0.1)) * BOYA_CENA
razreditel_suma = razreditel_kolichestvo * RAZREDITEL_CENA
torbichki_suma = TORBICHKI_CENA
obshta_suma_materiali = nailon_suma + boya_suma + razreditel_suma + torbichki_suma
obshta_suma_turd = (obshta_suma_materiali * 0.3) * chasove
obshta_suma_materiali_trud = obshta_suma_materiali + obshta_suma_turd

# print(f'Обща цена на материали и труд: {obshta_suma_materiali_trud} лв.')

print(obshta_suma_materiali_trud)