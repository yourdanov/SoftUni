w_room = int(input())
l_room = int(input())
h_room = int(input())

room_size = w_room * l_room * h_room
taken_size = 0

while True:
    command = input()
    if command == "Done":
        print(f"{room_size - taken_size} Cubic meters left.")
        break
    else:
        command = int(command)
        taken_size += command
        if taken_size >= room_size:
            print(f"No more free space! You need {taken_size - room_size} Cubic meters more.")
            break

# free_space_width = int(input())
# free_space_length = int(input())
# free_space_height = int(input())
#
# total_space = free_space_height * free_space_width * free_space_length
# boxes_placed = 0
#
# while True:
#     command = input() # също така броят на кашоните
#     if command == 'Done':
#         print(f'{total_space - boxes_placed} Cubic meters left.')
#         break
#     box = int(command)
#     boxes_placed += box
#     if boxes_placed > total_space:
#         print(f'No more free space! You need {boxes_placed - total_space} Cubic meters more.')
#         break
