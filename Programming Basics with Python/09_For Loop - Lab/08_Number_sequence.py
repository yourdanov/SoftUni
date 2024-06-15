from sys import maxsize

# Solution_1 ##############################################
# number = int(input())

# min_number = int(input())
# max_number = int(input())
#
# for _ in range(number - 2):
#     current_number = int(input())
#
#     if current_number < min_number:
#         min_number = current_number
#
#     if current_number > max_number:
#         max_number = current_number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")
#
# Solution_2 ##############################################
#
# number = int(input())
# numbers = [int(input()) for _ in range(number)]
# print(f'Max number: {max(numbers)}')
# print(f'Min number: {min(numbers)}')

# Solution_3 ##############################################

number = int(input())

min_number = maxsize
max_number = -maxsize

for _ in range(number):
    current_number = int(input())

    if current_number < min_number:
        min_number = current_number

    if current_number > max_number:
        max_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
