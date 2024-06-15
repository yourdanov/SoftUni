budget = int(input())
season = input()
number_of_fisherman = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Winter":
    boat_price = 2600
else:
    boat_price = 4200

if number_of_fisherman <= 6:
    boat_price *= 0.9
elif 7 <= number_of_fisherman <= 11:
    boat_price *= 0.85
else:
    boat_price *= 0.75

if season != "Autumn" and number_of_fisherman % 2 == 0:
    boat_price *= 0.95

if budget >= boat_price:
    print(f"Yes! You have {budget - boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_price - budget:.2f} leva.")
