month = input()
number_of_days = int(input())

studio_price = 0
appt_price = 0

if month == "May" or month == "October":
    studio_price = 50
    appt_price = 65
    if 7 < number_of_days <= 14:
        studio_price *= 0.95
    elif number_of_days > 14:
        studio_price *= 0.7

elif month == "June" or month == "September":
    studio_price = 75.20
    appt_price = 68.70
    if number_of_days > 14:
        studio_price *= 0.8

elif month == "July" or month == "August":
    studio_price = 76
    appt_price = 77

if number_of_days > 14:
    appt_price *= 0.9

price_appt = appt_price * number_of_days
price_std = studio_price * number_of_days

print(f"Apartment: {price_appt:.2f} lv.")
print(f"Studio: {price_std:.2f} lv.")
