# Prompt user for input
salesAmount = float(input("Enter sales amount: "))

# Calculate commission based on sales amount
if salesAmount <= 1000:
    commissionRate = 0.05
elif salesAmount <= 5000:
    commissionRate = 0.07
elif salesAmount <= 10000:
    commissionRate = 0.1
else:
    commissionRate = 0.15

commission = salesAmount * commissionRate

# Display commission
print("Commission earned:", commission)