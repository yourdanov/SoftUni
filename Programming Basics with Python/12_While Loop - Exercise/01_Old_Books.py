# Solution 1
# book_name = input()
# book_count = 0
#
# is_book_found = False
#
# current_book = input()
#
# while current_book != "No More Books":
#     if current_book == book_name:
#         is_book_found = True
#         print(f'You checked {book_count} books and found it.')
#         break
#
#     book_count += 1
#     current_book = input()
#
# if not is_book_found:
#     print(f'The book you search is not here!')
#     print(f'You checked {book_count} books.')

# Solution 2
my_book = input()

counter = 0

while True:
    command = input()
    if command == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
        break
    elif command == my_book:
        print(f'You checked {counter} books and found it.')
        break

    else:
        counter += 1
