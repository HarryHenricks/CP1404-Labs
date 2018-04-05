
def main():

    numbers = []
    try:
        for x in range(0,5):
            user_input = float(input("Number: "))
            numbers.append(user_input)

    except ValueError:
        print("Error, wrong type")

    print("The first number is {}\n"
          "The last number is {}\n"
          "The smallest number is {}\n"
          "The largest number is {}\n"
          "The average of the numbers is {}\n".format(numbers[0], numbers[-1], min(numbers), max(numbers), sum(numbers)/ len(numbers)))






main()


