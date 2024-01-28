def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time - principal

# Take input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Print the results
print(simple_interest(principal, rate, time))
print(compound_interest(principal, rate, time))