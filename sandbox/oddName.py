"""
Harry
"""

def main():
    x = True
    name = input("What is you name: ")

    while x:

        if name.isalpha():
            print("Your name is {}".format(name))
            x = False

        else:
            name = input("What is your name: ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_count = 0

    for char in alphabet:
        for letter in name.lower():

            if letter is char:
                char_count += 1



            if char_count > 0:
                print("Letter {} appears {} times".format(letter, char_count))

                char_count = 0  # reset variable





main()