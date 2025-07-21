# Takes input to display for multiplication Table Program
number = int(input("Enter a number to see its multiplication table:"))

# Generate and display the multiplication table for the given number
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")