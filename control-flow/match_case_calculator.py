#Prompt for user input for two numbers and an operation
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        result = float(num1) + float(num2)
        print(f"The result is [result].")
    case "-":
        result = float(num1) - float(num2)
        print(f"The result is [result].")
    case "*":
        result = float(num1) * float(num2)
        print(f"The result is [result].")
    case "/":
        if float(num2) != 0:    
            result = float(num1) / float(num2)
            print(f"The result is [result].") 
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")
