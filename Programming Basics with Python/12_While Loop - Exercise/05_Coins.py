change = float(input())
change = int(change*100) # the summ is now in stotinki
coins_counter = 0

coins_counter += change // 200 # 2 leva
change = change % 200 # if we remove 2 leve how many leva/stotinki left
coins_counter += change // 100 # 1 leva
change = change % 100 # if we remove 1 leve how many leva/stotinki left
coins_counter += change // 50 # 50 stotinki
change = change % 50 # if we remove 50 stotinki how many stotinki left
coins_counter += change // 20 # 20 stotinki
change = change % 20 # if we remove 20 stotinki how many stotinki left
coins_counter += change // 10 # 10 stotinki
change = change % 10 # if we remove 10 stotinki how many stotinki left
coins_counter += change // 5 # 5 stotinki
change = change % 5 # if we remove 5 stotinki how many stotinki left
coins_counter += change // 2 # 2 stotinki
change = change % 2 # if we remove 2 stotinki how many stotinki left
coins_counter += change // 1 # 1 stotinka
change = change % 1 # if we remove 1 stotinka how many left

print(coins_counter)

#
# import math
#
# change = float(input())
# change = int(change*100)
#
# coins_counter = 0
#
# while change > 0:
#     if change >= 200:
#         change -= 200
#         coins_counter += 1
#     elif 200 > change >= 100:
#         change -= 100
#         coins_counter += 1
#     elif 100 > change >= 50:
#         change -= 50
#         coins_counter += 1
#     elif 50 > change >= 20:
#         change -= 20
#         coins_counter += 1
#     elif 20 > change >= 10:
#         change -= 10
#         coins_counter += 1
#     elif 10 > change >= 5:
#         change -= 5
#         coins_counter += 1
#     elif 5 > change >= 2:
#         change -= 2
#         coins_counter += 1
#     else:
#         change -= 1
#         coins_counter += 1
#
#     change = math.floor(change)
#
# print(coins_counter)
