speed = float(input())
fuel_per_100km = float(input())

distance_to_moon = 384400
time_on_moon = 3

time_to_moon = distance_to_moon / speed
total_time = (2 * time_to_moon) + time_on_moon

if total_time % 1 != 0:
    total_time_rounded = int(total_time) + 1
else:
    total_time_rounded = int(total_time)

total_distance = 2 * distance_to_moon
total_fuel_needed = (total_distance / 100) * fuel_per_100km

if total_fuel_needed % 1 != 0:
    total_fuel_needed_rounded = int(total_fuel_needed) + 1
else:
    total_fuel_needed_rounded = int(total_fuel_needed)

print(total_time_rounded)
print(total_fuel_needed_rounded)
