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
    print("Your emissions this week are: ", co2emission)
    if ncar == 0:
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

while choice1 == 2:
    KWHU = int(input("How much electricity have you used this month (You can check your Electricity meter to find out!), or press (0) to exit: "))
    emissionfactor = int(input("Is your home powered by Coal-Fired Electricity (1), Natural Gas (2), Renewable Energy (3): "))
    if emissionfactor == 1:
        Coal = KWHU*1.2
        print("Your household Emissions are, ", Coal)
    elif emissionfactor == 2:
        NaturalGas = KWHU*0.6
        print("Your household Emissions are,", NaturalGas)
    elif emissionfactor == 3:
        print("Your household emissions are nearly zero!")
    if KWHU == 0:
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))
while choice1 == 3:
    Food = input("Have you eat meat in the last week (y/n), or press (0) to return: ")
    if Food == "y":
        Meat = int(input("Select the meats you have eaten (Chicken - 1) (Beef - 2) (Lamb - 3): "))
        if Meat == 1:
            Nkg = int(input("How much of Chicken (In Kilograms) have you eaten this week: "))
            Number = Nkg*6.9
            print("The produced carbon dioxide is,", Number, "kg Co2 this week")
        if Meat == 2:
            Nkg = int(input("How much of Chicken (In Kilograms) have you eaten this week: "))
            Number = Nkg*27
            print("The produced carbon dioxide is,", Number, "kg Co2 this week")
        if Meat == 3:
            Nkg = int(input("How much of Chicken (In Kilograms) have you eaten this week: "))
            Number = Nkg*39.2
            print("The produced carbon dioxide is,", Number, "kg Co2 this week")
    if Food == "n":
        print("You have a very small emission rate!")
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))
    if Food == "0":
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

while choice1 == 4:
    Sure = input("Are you sure you want to proceed (y/n): ")
    if Sure == "y":
        input_list = []
        List = input("Input all the values you collected from today (Don't worry about units): ")
        List.split()
        for i in List:
            sum = 0
            sum = sum + i
            print(List)