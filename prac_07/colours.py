

colour_names = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb"}

# only first 3 hexadecimals from http://www.color-hex.com/color-names.html added
colour = input("Enter colour: ")
while colour != "":
    if colour in colour_names:
        print(("Hexadecimal for {} is {}".format(colour, colour_names[colour])))
    else:
        print("Invalid colour")
    state = input("Enter colour: ")

