password = input("Input a password that is 10 characters long: ")
count = len(password)
if count < 10:
    exit()
else:
    print("Welcome to the calculator")
    choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

while choice1 == 1:
    ncar = int(input("Enter how many gallons of fuel or press 0 to return: "))
    co2emission = ncar/8887
    print("Your emissions this week are: ",co2emission)
    if ncar == 0:
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

while choice1 == 2:
    KWHU = int(input("How much electricity have you used this month (You can check your Electricity meter to find out!): "))
    emissionfactor = int(input("Is your home powered by Coal-Fired Electricity (1), Natural Gas (2), Renewable Energy (3): "))
    if emissionfactor == 1:
        Coal = KWHU*(1.2)
        print("Your household Emissions are, ", Coal)
    elif emissionfactor == 2:
        NaturalGas = KWHU*(0.6)
        print("Your household Emissions are,", NaturalGas)
    elif emissionfactor == 3:
        print("Your household emissions are nearly zero!")
