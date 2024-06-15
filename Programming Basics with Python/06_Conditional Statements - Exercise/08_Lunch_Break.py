import math

series_name = str(input())
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 0.125
rest_time = break_duration * 0.25

time_left = break_duration - (lunch_time + rest_time)

difference1 = math.ceil(episode_duration - time_left)
difference2 = math.ceil(time_left - episode_duration)

if time_left < episode_duration:
    print(f"You don't have enough time to watch {series_name}, you need {difference1:.0f} more minutes.")
else:
    print(f"You have enough time to watch {series_name} and left with {difference2:.0f} minutes free "
          f"time.")
