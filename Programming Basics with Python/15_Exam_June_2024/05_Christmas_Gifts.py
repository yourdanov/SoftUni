adults_count = 0
kids_count = 0

toy_price = 5
sweater_price = 15

while True:
    command = input()
    if command == "Christmas":
        break
    age = int(command)

    if age <= 16:
        kids_count += 1
    else:
        adults_count += 1

money_for_toys = kids_count * toy_price
money_for_sweaters = adults_count * sweater_price

print(f"Number of adults: {adults_count}")
print(f"Number of kids: {kids_count}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
