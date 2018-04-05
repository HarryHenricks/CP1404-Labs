def main():
    try:
        name = input("Please enter your name: ")
        vowels = "aeiou"
        vowel_count = 0

        for char in vowels:
            for letter in name.lower():
                if char == letter:
                    vowel_count += 1

    except NameError:
        print("Please enter a valid name")

    print("Your name has {} vowels in it".format(vowel_count))

main()
