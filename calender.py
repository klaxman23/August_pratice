import calendar

mm = int(input("Enter month (1-12): "))
yy = int(input("Enter year: "))
print(calendar.month(yy, mm))
print("The month has been displayed above.")
# This code displays the calendar for a specified month and year.
# It prompts the user to input the month and year, then uses the calendar module to print the calendar for that month.
# The user is informed that the month has been displayed.