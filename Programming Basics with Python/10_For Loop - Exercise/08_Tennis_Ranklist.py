# import math
#
# # Четене на входните данни
# num_tournaments = int(input("Enter the number of tournaments: "))
# initial_points = int(input("Enter the initial points: "))
#
# # Променливи за съхранение на точките и броя победи
# total_points = initial_points
# points_earned = 0
# tournaments_won = 0
#
# # Обработка на всеки турнир
# for _ in range(num_tournaments):
#     result = input("Enter the result (W, F, SF): ")
#     if result == "W":
#         points_earned += 2000
#         tournaments_won += 1
#     elif result == "F":
#         points_earned += 1200
#     elif result == "SF":
#         points_earned += 720
#
# # Изчисляване на крайните точки
# total_points += points_earned
#
# # Изчисляване на средните точки
# average_points = points_earned // num_tournaments
#
# # Изчисляване на процента на спечелените турнири
# win_percentage = (tournaments_won / num_tournaments) * 100
#
# # Отпечатване на резултатите
# print(f"Final points: {total_points}")
# print(f"Average points: {average_points}")
# print(f"{win_percentage:.2f}%")

from math import floor

number_of_tournaments = int(input())
initial_points = int(input())

points = 0
wins = 0

W = 2000
F = 1200
SF = 720

for i in range(number_of_tournaments):
    status = input()
    if status == "W":
        points += W
        wins += 1
    elif status == "F":
        points += F
    elif status == "SF":
        points += SF

print(f"Final points: {points + initial_points}")
print(f"Average points: {floor(points / number_of_tournaments)}")
print(f"{wins / number_of_tournaments * 100:.2f}%")
