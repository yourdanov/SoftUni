username = input()
password = input()
typed_password = input()

while password != typed_password:
    typed_password = input()

print(f'Welcome {username}!')
