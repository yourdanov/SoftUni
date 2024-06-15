city = input()
money = float(input())

percent_commission = 0

if city == "Sofia":
    if money < 0:
        print("error")
        exit()
    elif money <= 500:
        percent_commission = 0.05
    elif money <= 1000:
        percent_commission = 0.07
    elif money <= 10_000:
        percent_commission = 0.08
    else:
        percent_commission = 0.12
elif city == "Varna":
    if money < 0:
        print("error")
        exit()
    elif money <= 500:
        percent_commission = 0.045
    elif money <= 1000:
        percent_commission = 0.075
    elif money <= 10_000:
        percent_commission = 0.10
    else:
        percent_commission = 0.13
elif city == "Plovdiv":
    if money < 0:
        print("error")
        exit()
    elif money <= 500:
        percent_commission = 0.055
    elif money <= 1000:
        percent_commission = 0.08
    elif money <= 10_000:
        percent_commission = 0.12
    else:
        percent_commission = 0.145
else:
    print("error")
    exit()

commission = money * percent_commission

print(f"{commission:.2f}")
