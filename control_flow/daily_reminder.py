task = input("Enter your task: ")
priority =input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
if time_bound == "yes":
    print("Important reminder:", task, "has a deadline and needs to be completed ASAP.")
elif priority == "high":
    print("Reminder:",task, "is urgent and should be done immediately.")    
elif priority == "medium":
    print("Reminder:",task, "is important but not urgent.")
elif priority == "low":
    print(task, "can be done later.")   
else:
    print(task,"is not urgent and can be scheduled for later.")
