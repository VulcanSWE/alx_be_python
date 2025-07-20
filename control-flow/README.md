
Introducing Logic into programming (Control flow and loops)

    Novice
    Weight: 1
    Project will start Jul 14, 2025 12:00 AM, must end by Jul 21, 2025 12:00 AM
    Checker was released at Jul 14, 2025 12:00 AM
    An auto review will be launched at the deadline

This project dives into the world of control flow and loops, essential concepts for introducing logic into your Python programs. You’ll learn how to make decisions using conditional statements and automate repetitive tasks using loops.
Project Objectives:

By the end of this project, you should be able to:

    Explain the concept of control flow and its role in programming.
    Utilize conditional statements (if, else, elif) to control the flow of execution in your Python code based on specific conditions.
    Write practical examples demonstrating the use of conditional statements for decision-making.
    Understand the concept of Match Case statements introduced in Python 3.10 as an alternative to multiple if/elif statements (optional for Python versions below 3.10).
    Explain the advantages of Match Case statements for handling multiple conditions.
    Implement Match Case statements using proper syntax, including matching against specific values and types (optional for Python versions below 3.10).
    Apply best practices for using Match Case statements to enhance code readability and efficiency (optional for Python versions below 3.10).
    Grasp the purpose and different types of loops available in Python.
    Utilize for loops to iterate over sequences (lists, tuples, strings, etc.) efficiently.
    Write examples demonstrating how to use for loops to iterate over various data structures.
    Explain the concept of while loops and how they differ from for loops.
    Implement while loops in Python to execute code repeatedly as long as a specific condition remains true.
    Understand nested loops (loops within loops) and their applications in scenarios like working with multidimensional data or creating patterns.

This project equips you with fundamental programming skills to control the flow of your Python programs and automate repetitive tasks. Mastering these concepts will allow you to write more dynamic and efficient code.
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Weather Recommendation Program
mandatory

Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

Task Description:

Create a Python script named weather_advice.py. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

Instructions:

    Prompt User for Weather Input:
        Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
        Use the prompt: What's the weather like today? (sunny/rainy/cold):.

    Provide Clothing Recommendations:
        Based on the user’s input, your program will recommend different types of clothing:
            If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
            If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
            If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
        Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.

    Output the Recommendation:
        Print the clothing recommendation based on the weather condition provided by the user.

Example Interaction:

What's the weather like today? (sunny/rainy/cold): sunny
Wear a t-shirt and sunglasses.

Or, for an unexpected input scenario:

What's the weather like today? (sunny/rainy/cold): windy
Sorry, I don't have recommendations for this weather.

Repo:

    GitHub repository: alx_be_python
    Directory: control-flow
    File: weather_advice.py

1. Simple Calculator with Match Case
mandatory

Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

Task Description:

Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

Instructions:

    Prompt for User Input:
        Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
        Make sure you use num1 and num2 for first and second numbers
        Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.

    Perform the Calculation Using Match Case:
        Implement a Match Case statement that executes the chosen operation based on the user’s input.
            For addition (+), subtract (-), multiply (*), and divide (/).
        Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.

    Output the Result:
        Display the result of the operation in a user-friendly message, e.g., The result is [result].

Example Interaction:

Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.

Or, for a division by zero scenario:

Enter the first number: 10
Enter the second number: 0
Choose the operation (+, -, *, /): /
Cannot divide by zero.

Repo:

    GitHub repository: alx_be_python
    Directory: control-flow
    File: match_case_calculator.py

2. Multiplication Table Generator
mandatory

Objective: Use a for loop to generate and print the multiplication table for a given number.

Task Description:

Create a Python script named multiplication_table.py. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

Instructions:

    Prompt User for a Number:
        Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
        Save it in a variable name number

    Generate and Print the Multiplication Table:
        Use a for loop to iterate through the numbers 1 to 10.
        For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
        Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.

Example Interaction:

If the user inputs 5, the output should be:

Enter a number to see its multiplication table: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

This task is designed to reinforce the concept of for loops by applying them in a practical scenario that generates a multiplication table. Through this exercise, students will learn how loops can significantly simplify the process of performing repetitive tasks, enhancing their understanding of looping constructs in Python.

Repo:

    GitHub repository: alx_be_python
    Directory: control-flow
    File: multiplication_table.py

3. Drawing Patterns with Nested Loops
mandatory

Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

Task Description:

Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

Instructions:

    Prompt User for Pattern Size:
        Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.

    Draw the Pattern:
        First, use a while loop to iterate through each row of the pattern.
        Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
        After completing each row, print a newline character to move to the next row.
        Continue until the pattern forms a square of the inputted size.

Example Interaction:

If the user inputs 4, the output should be:

Enter the size of the pattern: 4
****
****
****
****

Repo:

    GitHub repository: alx_be_python
    Directory: control-flow
    File: pattern_drawing.py

