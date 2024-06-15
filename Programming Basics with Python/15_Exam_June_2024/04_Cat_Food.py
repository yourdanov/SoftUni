number_of_cats = int(input())

group1_count = 0
group2_count = 0
group3_count = 0

price_per_kg = 12.45

total_food_grams = 0

for _ in range(number_of_cats):
    food_grams = float(input())
    total_food_grams += food_grams

    if 100 <= food_grams < 200:
        group1_count += 1
    elif 200 <= food_grams < 300:
        group2_count += 1
    elif 300 <= food_grams <= 400:
        group3_count += 1

total_food_kg = total_food_grams / 1000

total_price = total_food_kg * price_per_kg

print(f"Group 1: {group1_count} cats.")
print(f"Group 2: {group2_count} cats.")
print(f"Group 3: {group3_count} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
