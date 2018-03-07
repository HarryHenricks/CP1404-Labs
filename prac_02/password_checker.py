"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < 2:
        return False
    elif len(password) > 6:
        return False


    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)

        if char.islower():
            count_lower += 1

        elif char.isupper():
            count_upper += 1

        elif char.isdigit():
            count_digit += 1

        else:
            char_password = char
            for char in SPECIAL_CHARACTERS:
                if char == char_password:
                    count_special += 1


        pass


# TODO: if any of the 'normal' counts are zero, return False
    if count_lower == 0:
        print("You must have at least 1 lower charachter")
        return False

    elif count_upper == 0:
        print("You must have at least 1 upper charachter")
        return False

    elif count_digit == 0:
        print("You must have at least 1 digit")
        return False

    elif count_special == 0:
        print("You must have at least 1 special charachter")
        return False


    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()