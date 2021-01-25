print("Welcome to the TIP CALCULATOR")
bill = float(input("what's your Bill amount: $"))
tip = int(input("How much tip you wanna give: "))
people = int (input("In how much people bill will be divided: "))

share = (bill + ((tip/100)*bill))/people
print(f"Each bill share is {round(share,2)}")