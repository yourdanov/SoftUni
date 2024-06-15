product = input()
day = input()
quantity = float(input())

product_price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        product_price = 2.50
    elif product == "apple":
        product_price = 1.20
    elif product == "orange":
        product_price = 0.85
    elif product == "grapefruit":
        product_price = 1.45
    elif product == "kiwi":
        product_price = 2.70
    elif product == "pineapple":
        product_price = 5.50
    elif product == "grapes":
        product_price = 3.85
    else:
        print("error")
        exit()
elif day == "Saturday" or day == "Sunday":
    if product == "banana":
        product_price = 2.70
    elif product == "apple":
        product_price = 1.25
    elif product == "orange":
        product_price = 0.90
    elif product == "grapefruit":
        product_price = 1.60
    elif product == "kiwi":
        product_price = 3.00
    elif product == "pineapple":
        product_price = 5.60
    elif product == "grapes":
        product_price = 4.20
    else:
        print("error")
        exit()
else:
    print("error")
#    raise SystemExit
    exit()

total_price = product_price * quantity
print(f"{total_price:.2f}")
