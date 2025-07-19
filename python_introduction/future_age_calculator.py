current_age = int(input("How old are you? "))

current_year = 2023  # Assuming the current year is 2023
future_years = int(input("How many years into the future do you want to calculate your age? "))
future_age = int(future_years) - current_year + current_age

print(f" In {future_years}, you will be {future_age} years old.")
# This code calculates the future age of a person based on their current age and the number of years into the future they want to calculate. It prompts the user for their current age and the number of years, then adds these values together to determine the future age. Finally, it prints out the result in a formatted string.