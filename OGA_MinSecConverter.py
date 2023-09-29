time = int(input("enter an integer in seconds: "))
minutes = time // 60
remaining_seconds = time % 60
print(f"{time}seconds is {minutes}minutes and {remaining_seconds }seconds.")