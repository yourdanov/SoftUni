# from sys import maxsize
#
# number = int(input())
#
# max_number = -maxsize
# sum_numbers = 0

max_num = float('-inf')

sum_numbers = 0

n = int(input())

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_numbers += num

if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    sum_numbers = sum_numbers - max_num
    print("No")
    print(f"Diff = {abs(max_num - sum_numbers)}")
