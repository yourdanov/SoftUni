base_number = int(input())
current_sum = 0

while True:
    current_number = int(input())
    current_sum += current_number

    if current_sum >= base_number:
        print(current_sum)
        break
