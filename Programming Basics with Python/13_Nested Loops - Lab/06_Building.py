number_of_floors = int(input())
number_of_rooms = int(input())

for i in range(number_of_floors, 0, - 1):
    for j in range(0, number_of_rooms):
        if i == number_of_floors:
            print('L{0}{1} '.format(i, j), end='')
        elif i % 2 == 0:
            print('O{0}{1} '.format(i, j), end='')
        elif i % 2 == 1:
            print('A{0}{1} '.format(i, j), end='')
    print()

# number_of_floors = int(input())
# number_of_rooms = int(input())
#
# flat_name
#
# for i in range(number_of_floors, 0, - 1):
#     for j in range(0, number_of_rooms):
#         if i == number_of_floors:
#             flat_name = f'L{number_of_floors}{number_of_rooms}'
#         elif i % 2 == 0:
#             flat_name = f'O{number_of_floors}{number_of_rooms}'
#         elif i % 2 == 1:
#             flat_name = f'A{number_of_floors}{number_of_rooms}'
#
#         print(flat_name, end=' ')
#
#     print()
