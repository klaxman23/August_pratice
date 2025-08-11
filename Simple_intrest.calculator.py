# Simple Interest Calculator

# Input: principal amount, rate of interest, time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"Simple Interest = {simple_interest}")
