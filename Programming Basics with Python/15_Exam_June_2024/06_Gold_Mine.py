number_of_locations = int(input())

for location in range(number_of_locations):
    expected_average_gold_per_day = float(input())
    number_of_days = int(input())

    total_gold = 0.0

    for day in range(number_of_days):
        gold_per_day = float(input())
        total_gold += gold_per_day

    average_gold_per_day = total_gold / number_of_days

    if average_gold_per_day >= expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        gold_needed = expected_average_gold_per_day - average_gold_per_day
        print(f"You need {gold_needed:.2f} gold.")
