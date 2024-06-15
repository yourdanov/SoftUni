PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

trip_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

total_number = puzzles_number + dolls_number + bears_number + minions_number + trucks_number

puzzles_price = PUZZLE_PRICE * puzzles_number
dolls_price = TALKING_DOLL_PRICE * dolls_number
bears_price = TEDDY_BEAR_PRICE * bears_number
minions_price = MINION_PRICE * minions_number
trucks_price = TRUCK_PRICE * trucks_number

total_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

if total_number >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9 # Rent 10%

if total_price >= trip_price:
    print(f"Yes! {total_price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_price:.2f} lv needed.")
