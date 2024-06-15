dalzhina = int(input("Дължина в см: "))
shirochina = int(input("Широчина в см: "))
visochina = int(input("Височина в см: "))
procent = float(input("Процент: "))

obem = dalzhina * shirochina * visochina
obem_v_litri = obem * 0.001
zaeto_prostranstvo = procent/100

nuzhni_litri = obem_v_litri * (1 - zaeto_prostranstvo)

# print(f'Нужни литри вода: {nuzhni_litri} л.')

print(nuzhni_litri)