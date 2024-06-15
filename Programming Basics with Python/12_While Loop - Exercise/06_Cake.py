w_cake = int(input())
l_cake = int(input())

cake_size = w_cake * l_cake

taken_pieces = 0

while True:
    command = input()
    if command == "STOP":
        print(f"{cake_size - taken_pieces} pieces are left.")
        break
    else:
        command = int(command)
        taken_pieces += command
        if taken_pieces >= cake_size:
            print(f"No more cake left! You need {taken_pieces - cake_size} pieces more.")
            break

# width = int(input())
# length = int(input())
#
# number_of_pieces = width * length
# pieces_requested = 0
#
# while number_of_pieces >= 0:
#     command = input()
#     if command == 'STOP':
#         print(f'{abs(number_of_pieces)} pieces are left.')
#         break
#     pieces_taken = int(command)
#     number_of_pieces -= pieces_taken
#     pieces_requested += pieces_taken
#     if number_of_pieces < 0:
#         print(f'No more cake left! You need {abs(number_of_pieces)} pieces more.')
#         break
