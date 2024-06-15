flower_type = input()
number_of_flowers = int(input())
budget = int(input())

ROSES_PRICE = 5.00
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3.00
GLADIOLUS_PRICE = 2.50

total_price = 0

if flower_type == "Roses":
    total_price = number_of_flowers * ROSES_PRICE
    if number_of_flowers > 80:
        total_price *= 0.9
#       total_price = total_price - (total_price * 0.1)
#       total_price = total_price * 0.9

elif flower_type == "Dahlias":
    total_price = number_of_flowers * DAHLIAS_PRICE
    if number_of_flowers > 90:
        total_price *= 0.85

elif flower_type == "Tulips":
    total_price = number_of_flowers * TULIPS_PRICE
    if number_of_flowers > 80:
        total_price *= 0.85

elif flower_type == "Narcissus":
    total_price = number_of_flowers * NARCISSUS_PRICE
    if number_of_flowers < 120:
        total_price *= 1.15
#        total_price = total_price + (total_price * 0.15)

elif flower_type == "Gladiolus":
    total_price = number_of_flowers * GLADIOLUS_PRICE
    if number_of_flowers < 80:
        total_price *= 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
