def simple_intrest(principal, rate, time):
    return (principal * rate *time ) / 100

def compound_interest(principal, rate, time):
    return principal * (1 + rate/100) ** time-principal
print(simple_intrest(1000, 10.25, 5))
print(compound_interest(10000, 10.25, 5))