# Method 1 memory and time allocation: Memory: 0.57 MB Time: 0.020 s
# word = input()
#
# while word != 'Stop':
#     print(word)
#
#     word = input()
#######################################################################################
# Method 2 memory and time allocation: Memory: 0.56 MB Time: 0.030 s
while True:
    word = input()

    if word == 'Stop':
        break

    print(word)
