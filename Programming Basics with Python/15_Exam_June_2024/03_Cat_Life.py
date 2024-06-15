breed = input()
gender = input()

life_years = 0

if breed == "British Shorthair":
    if gender == 'm':
        life_years = 13
    elif gender == 'f':
        life_years = 14
elif breed == "Siamese":
    if gender == 'm':
        life_years = 15
    elif gender == 'f':
        life_years = 16
elif breed == "Persian":
    if gender == 'm':
        life_years = 14
    elif gender == 'f':
        life_years = 15
elif breed == "Ragdoll":
    if gender == 'm':
        life_years = 16
    elif gender == 'f':
        life_years = 17
elif breed == "American Shorthair":
    if gender == 'm':
        life_years = 12
    elif gender == 'f':
        life_years = 13
elif breed == "Siberian":
    if gender == 'm':
        life_years = 11
    elif gender == 'f':
        life_years = 12
else:
    print(f"{breed} is invalid cat!")
    exit()

cat_months = (life_years * 12) // 6

print(f"{cat_months} cat months")
