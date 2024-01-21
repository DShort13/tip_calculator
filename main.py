print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people are splitting the bill? ")

total_as_float = float(total)
tip_as_int = int(tip)
people_as_int = int(people)

tip = 1 + tip_as_int / 100

split = round(total_as_float * tip / people_as_int, 2)

print(f"Each person should pay: ${split}")