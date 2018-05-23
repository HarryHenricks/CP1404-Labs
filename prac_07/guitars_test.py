from guitars import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.4)

print(guitar)

print("My Guitars!")

guitars = []
guitar_name = input("Name: ")

while guitar_name != "":

    guitar_year = int(input("Year: "))
    guitar_price = float(input("Price: "))

    guitar = Guitar(guitar_name, guitar_year, guitar_price)
    print("{} added".format(guitar))
    guitars.append(guitar)
else:
    guitar_name = input("Name: ")





for i, guitar in enumerate(guitars):

    if guitar.is_vintage():
        is_vintage = "(vintage)"
    else:
        is_vintage = ""

    print("Guitar {}: {} ({}), worth $ {} {}".format(i+1, guitar_name, guitar_year, guitar_price, is_vintage))

