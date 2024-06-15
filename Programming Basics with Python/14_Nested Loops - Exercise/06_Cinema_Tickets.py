total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break
    free_seats = int(input())

    sold_tickets = 0

    while sold_tickets < free_seats:
        ticket_type = input()
        if ticket_type == "End":
            break
        sold_tickets += 1
        total_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

    hall_fullness = (sold_tickets / free_seats) * 100
    print(f"{movie_name} - {hall_fullness:.2f}% full.")

if total_tickets > 0:
    student_percentage = (student_tickets / total_tickets) * 100
    standard_percentage = (standard_tickets / total_tickets) * 100
    kid_percentage = (kid_tickets / total_tickets) * 100
else:
    student_percentage = 0
    standard_percentage = 0
    kid_percentage = 0

print(f"Total tickets: {total_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kid_percentage:.2f}% kids tickets.")
