name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

beer_price = 1.20
total_beer_cost = beer_count * beer_price
chips_price_per_package = total_beer_cost * 0.45
total_chips_cost = chips_count * chips_price_per_package

if total_chips_cost % 1 != 0:
    total_chips_cost = int(total_chips_cost) + 1
else:
    total_chips_cost = int(total_chips_cost)

total_cost = total_beer_cost + total_chips_cost

if budget >= total_cost:
    money_left = budget - total_cost
    print(f"{name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = total_cost - budget
    print(f"{name} needs {money_needed:.2f} more leva!")
