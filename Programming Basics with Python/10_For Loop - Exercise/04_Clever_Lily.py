N = int(input())
X = float(input())
P = int(input())

total_money = 0
total_toys = 0
money_received = 10

for year in range(1, N + 1):
    if year % 2 == 0:
        total_money += money_received
        money_received += 10
        total_money -= 1
    else:
        total_toys += 1

total_money += total_toys * P

if total_money >= X:
    print(f"Yes! {total_money - X:.2f}")
else:
    print(f"No! {X - total_money:.2f}")
