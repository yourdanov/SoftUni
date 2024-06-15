# actor_name = input()
# initial_points = float(input())
# n = int(input())
#
# total_points = initial_points
#
# for _ in range(n):
#     judge_name = input()
#     judge_points = float(input())
#
#     total_points += (len(judge_name) * judge_points) / 2
#
#     if total_points > 1250.5:
#         print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
#         break
# else:
#     needed_points = 1250.5 - total_points
#     print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
actor_name = input()
initial_points = float(input())
judges = int(input())

total_points = initial_points

for i in range(judges):
    judge_name = input()
    points = float(input())

    if total_points <= 1250.5:
        total_points += (len(judge_name) * points) / 2
    else:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
