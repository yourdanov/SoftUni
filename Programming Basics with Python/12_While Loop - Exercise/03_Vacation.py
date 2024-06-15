need_money = float(input())
save_money = float(input())

days = 0
spend_days = 0

while True:
    command = input()
    money = float(input())

    if command == "spend":
        save_money -= money
        if save_money < 0:
            save_money = 0
        spend_days += 1
        days += 1

        if spend_days == 5:
            print(f"You can't save the money.")
            print(f"{days}")
            break

    else:
        save_money += money
        days += 1
        spend_days = 0
        if save_money >= need_money:
            print(f"You saved the money for {days} days.")
            break
