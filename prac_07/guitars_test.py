from guitars import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)

guitar.__str__()

print("My Guitars!")

guitar_name = "Something" # initialise variable to something other than blank
guitars = []

while guitar_name != "":

    guitar_name = input("Name: ")
    if guitar_name == "":
        break

    guitar_year = int(input("Year: "))
    guitar_price = float(input("Price: "))

    guitar = Guitar(guitar_name, guitar_year, guitar_price)
    print("{} added".format(guitar.__str__()))
    guitars.append(guitar)




for i, guitar in enumerate(guitars):

    if guitar.is_vintage() == True:
        is_vintage = "(vintage)"
    else:
        is_vintage = ""

    print("Guitar {}: {} ({}), worth $ {} {}".format(i+1, guitar_name, guitar_year, guitar_price, is_vintage))

