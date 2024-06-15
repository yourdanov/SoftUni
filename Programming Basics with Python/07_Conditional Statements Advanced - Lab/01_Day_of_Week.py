number = int(input())

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if 1 <= number <= 7:
    print(f"{days[number]}")
else:
    print("Error")
