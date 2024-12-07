#Lines 3-10 are used as a short introduction to the program, this information can be considered sensitive and should be protected

print("Welcome to the Co2 calculator")


passwordcheck = False

while passwordcheck == False:

    password = input("Input a password that is 10 characters long: ")
    count = len(password)

    if count < 10:
        print("Error: Enter minimum 10 characters for password")
    else:
        passwordcheck = True
        print("Welcome to the calculator")
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

#The first choice the user makes is to decide what they would like to calculate, should they choose to determine their car emissions the following program runs
#The program asks the user to enter how much fuel they burned in gallons
#Then the program calculates their amount of co2 emitted
#The user has the option to go back and choose something elese to calculate

while choice1 == 1:
    ncar = int(input("Enter how many gallons of fuel or press 0 to return: "))
    co2emission = ncar/8887
    print("Your emissions this week are: ", co2emission, "kg of co2")
    if ncar == 0:
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

#Should the user choose to discover their household power use and co2 emissions, this program would run
#User has the option to choose what kind of power grid they use
#The program uses the same formula to calculate their emissions unless they use renewable energy

while choice1 == 2:
    KWHU = int(input("How much electricity have you used this month (You can check your Electricity meter to find out!), or press (0) to exit: "))
    emissionfactor = int(input("Is your home powered by Coal-Fired Electricity (1), Natural Gas (2), Renewable Energy (3): "))
    if emissionfactor == 1:
        Coal = KWHU*1.2
        print("Your household Emissions are, ", Coal, "kg of co2")
    elif emissionfactor == 2:
        NaturalGas = KWHU*0.6
        print("Your household Emissions are,", NaturalGas, "kg of co2")
    elif emissionfactor == 3:
        print("Your household emissions are nearly zero! approximately 0.9 kg of co2")
    if KWHU == 0:
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

#Should the user chooses to see how much their dietry choices produce, they press 3 and this program runs
#User must choose between if they ate meats this week or if they ate ther things, we only calculate meat, other things have an average emission rate of 2 kg co2
#Same process runs for each each meat with different values

while choice1 == 3:
    Food = input("Have you eat meat in the last week (y/n), or press (0) to return: ")
    if Food == "y":
        Meat = int(input("Select the meats you have eaten (Chicken - 1) (Beef - 2) (Lamb - 3): "))
        if Meat == 1:
            Nkg = int(input("How much of Chicken (In Kilograms) have you eaten this week: "))
            Number = Nkg*6.9
            print("The produced carbon dioxide is,", Number, "kg Co2 this week")
        if Meat == 2:
            Nkg = int(input("How much of Beef (In Kilograms) have you eaten this week: "))
            Number = Nkg*27
            print("The produced carbon dioxide is,", Number, "kg Co2 this week")
        if Meat == 3:
            Nkg = int(input("How much of Lamb (In Kilograms) have you eaten this week: "))
            Number = Nkg*39.2
            print("The produced carbon dioxide is,", Number, "kg Co2 this week")
    if Food == "n":
        print("You have a very small emission rate! Your emissions are likely to be around 2 kg co2")
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))
    if Food == "0":
        choice1 = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

#Now the user must confirm this is what they would like to do
#Once this is done, the user is asked how many values they have collected today
#The program asks the user to enter their values, (Non-specific to the tests) for as many times as the user says they collected values
#(e.g: the user says they got three values, the program runs the command three times to get all three data points)
#The values are compiled into a list and then the values are summed up, and converted from kg to metric tons
#The program decides if the user has a small, average, slightly big or a very large carbon footprint

while choice1 == 4:
    Sure = input("Are you sure you want to proceed (y/n): ")
    if Sure == "y":
        input_list = []
        element = int(input("How many values have you collected today: "))
        for i in range(element):
            valuescollected = int(input("Enter Co2 value: "))
            input_list.append(valuescollected)
        total = sum(input_list)
        totalMT = total*0.001
        if totalMT <= 4:
            print("Your carbon footprint is,", totalMT, "metric tons of co2")
            print("You have a smaller carbon footprint than the world average!")
        if totalMT >= 4:
            print("Your carbon footprint is,", totalMT, "metric tons of co2")
            print("You have around the same footprint as the world average!")
        if totalMT >= 8:
            print("Your carbon footprint is,", totalMT, "metric tons of co2")
            print("You have one of the lowest carbon footprints in the united states, but a much higher footprint than the world average!")
        if totalMT >= 15:
            print("Your carbon footprint is,", totalMT, "metric tons of co2")
            print("You have a very high carbon footprint and should reduce your emissions!")
    if Sure == "n":
        (choice1) = int(input("What would you like to calculate? (Car emissions(1), Energy use(2), Food consumption(3), Final value(4), Exit(5): "))

#The program ends once the user says they would like to end their process

while choice1 == 5:
    exit()
