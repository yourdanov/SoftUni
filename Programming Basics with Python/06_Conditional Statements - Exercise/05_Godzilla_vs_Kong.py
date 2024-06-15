budget = float(input())
staff = int(input())
wear_price = float(input())

amount_of_wear = staff * wear_price
decore = budget * 0.1

if staff > 150:
    amount_of_wear *= 0.9  # amount_of_wear = amount_of_wear*0.9

total_cost = decore + amount_of_wear

difference = abs(total_cost - budget)

if total_cost > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
