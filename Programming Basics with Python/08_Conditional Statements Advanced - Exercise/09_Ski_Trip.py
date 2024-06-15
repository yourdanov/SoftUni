days = int(input())
room_type = input()
rating = input()

price_per_night = 0
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

nights = days - 1

initial_price = nights * price_per_night

if room_type == "apartment":
    if nights < 10:
        discount = 0.30
    elif 10 <= nights <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif room_type == "president apartment":
    if nights < 10:
        discount = 0.10
    elif 10 <= nights <= 15:
        discount = 0.15
    else:
        discount = 0.20
else:
    discount = 0.00

final_price = initial_price * (1 - discount)

if rating == "positive":
    final_price *= 1.25
elif rating == "negative":
    final_price *= 0.90

print(f"{final_price:.2f}")
