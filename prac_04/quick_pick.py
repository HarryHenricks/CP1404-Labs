import random

def main():

    user_pick = int(input("How many quick picks: "))

    for i in range(0, user_pick):
        rand_line()

def rand_line():
    line = []
    while len(line) != 6:
        number = random.randint(1, 45)

        if number in line:
            number = random.randint(1, 45)
        else:
            line.append(number)

    print("{} {} {} {} {} {}".format(line[0], line[1], line[2], line[3], line[4], line[5]))




main()