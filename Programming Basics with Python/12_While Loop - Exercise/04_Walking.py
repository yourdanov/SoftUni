GOAL = 10000

all_steps = 0

while all_steps < GOAL:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        all_steps += last_steps
        break
    steps = int(command)
    all_steps += steps

diff = abs(all_steps - GOAL)

if all_steps >= GOAL:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

# goal = 10000
# steps_taken = 0
# steps_over = 0
# command = input()
#
# while command != 'Going home':
#     steps_to_do = int(command)
#     steps_taken += steps_to_do
#     if steps_taken >= goal:
#         steps_over = steps_taken - goal
#         print('Goal reached! Good job!')
#         print(f'{steps_over} steps over the goal!')
#         break
#
#     command = input()
#
# if command == 'Going home':
#     steps_to_home = int(input())
#     steps_taken += steps_to_home
#     if steps_taken >= goal:
#         steps_over = steps_taken - goal
#         print('Goal reached! Good job!')
#         print(f'{steps_over} steps over the goal!')
#     else:
#         print(f'{goal-steps_taken} more steps to reach goal.')
