# Daily Reminder Program

# This program prompts the user to enter a task and reminds them of it daily.
task = input("Enter your task: ").strip()

priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        print(f"Reminder: {task} - This is a high priority task.")
    case "medium":
        print(f"Reminder: {task} - This is a medium priority task.")
    case "low":
        print(f"Reminder: {task} - This is a low priority task.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
if time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!.")  
else:
    print(f"Reminder: {task} - This task is not time-bound, but please try to complete it as soon as possible.")
# End of Daily Reminder Program
