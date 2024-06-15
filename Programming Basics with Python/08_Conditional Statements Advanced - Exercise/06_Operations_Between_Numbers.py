N1 = int(input())
N2 = int(input())
operand = input()

result = 0
parity = 0

if operand == "+":
    result = N1 + N2
    if result % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"{N1} {operand} {N2} = {result} - {parity}")

elif operand == "-":
    result = N1 - N2
    if result % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"{N1} {operand} {N2} = {result} - {parity}")

elif operand == "*":
    result = N1 * N2
    if result % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"{N1} {operand} {N2} = {result} - {parity}")

elif operand == '/':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")

elif operand == '%':
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
