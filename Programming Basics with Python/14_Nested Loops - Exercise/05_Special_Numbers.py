number = int(input())

for i in range(1111, 9999):
    number_string = str(i)
    total_4 = 0
    for j in number_string:
        if int(j) != 0:
            if number % int(j) == 0:
                total_4 += 1

            if total_4 == 4:
                print(i, end=' ')
