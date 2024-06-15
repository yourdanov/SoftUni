student_name = input()

grades_total = 0
years_counter = 0
failed_years = 0

# 1:
# while True:
#     annual_grade = float(input())
#
#     if annual_grade < 4:
#         failed_years += 1
#         if failed_years == 2:
#             print(f'{student_name} has been excluded at {years_counter + 1} grade')
#             break

#         continue
#
#     grades_total += annual_grade
#     years_counter += 1
#
#     if years_counter == 12:
#         average_grade = grades_total / 12
#         print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
#         break
#
# 2:
while years_counter < 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f'{student_name} has been excluded at {years_counter + 1} grade')
            break

        continue

    grades_total += annual_grade
    years_counter += 1

else:
    average_grade = grades_total / 12
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
