# This code draws a pattern based on user input
# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))


#Initializing the counter(i) to 0
i = 0

# Generate and display the pattern
while i < size:
    for col in range(size):
        print("*", end=" ")
    print()
    i += 1

