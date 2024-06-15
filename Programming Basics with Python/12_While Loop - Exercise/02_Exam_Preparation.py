max_negative_scores = int(input())
negative_scores = 0
number_of_problems = 0
total_score = 0
final_problem_name = ''

while True:
    command = input()
    if command == 'Enough':
        print(f'Average score: {total_score / number_of_problems:.2f}')
        print(f'Number of problems: {number_of_problems}')
        print(f'Last problem: {final_problem_name}')
        break
    else:
        points = int(input())
        final_problem_name = ''
        final_problem_name += command
        if points <= 4:
            negative_scores += 1
            if negative_scores == max_negative_scores:
                print(f'You need a break, {negative_scores} poor grades.')
                break

        number_of_problems += 1
        total_score += points
