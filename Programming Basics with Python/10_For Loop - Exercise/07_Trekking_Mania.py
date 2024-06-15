groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

total = 0

for _ in range(groups):
    group_size = int(input())
    total += group_size

    if group_size <= 5:
        musala += group_size
    elif 6 <= group_size <= 12:
        monblan += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro += group_size
    elif 26 <= group_size <= 40:
        k2 += group_size
    else:
        everest += group_size

musala_procent = (musala / total) * 100
monblan_procent = (monblan / total) * 100
kilimanjaro_procent = (kilimanjaro / total) * 100
k2_procent = (k2 / total) * 100
everest_procent = (everest / total) * 100

print(f"{musala_procent:.2f}%")
print(f"{monblan_procent:.2f}%")
print(f"{kilimanjaro_procent:.2f}%")
print(f"{k2_procent:.2f}%")
print(f"{everest_procent:.2f}%")
