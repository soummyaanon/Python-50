months = ["January", "April", "August", "June", "November"]

for i in months:
    if i == "February":
        print("The month February has 28/29 days")

    elif i in ("April", "June", "September", "November"):
        print("The month of", i, "has 30 days.")

    elif i in ("January", "March", "May", "July", "August", "October", "December"):
        print("The month of", i, "has 31 days.")

    else:
        print(i, "is not a valid month name.")
