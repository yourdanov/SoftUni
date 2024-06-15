n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    else:
        p5 += 1

p1_diap = (p1 / n) * 100
p2_diap = (p2 / n) * 100
p3_diap = (p3 / n) * 100
p4_diap = (p4 / n) * 100
p5_diap = (p5 / n) * 100

print(f"{p1_diap:.2f}%")
print(f"{p2_diap:.2f}%")
print(f"{p3_diap:.2f}%")
print(f"{p4_diap:.2f}%")
print(f"{p5_diap:.2f}%")
