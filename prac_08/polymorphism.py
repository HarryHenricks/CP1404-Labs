from silverservicetaxi import SilverServiceTaxi
from taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
print("Lets drive!")

def main():
    total_bill = 0 # initialise bill
    taxi_choice = 0  # default choice if none selected
    menu()
    user_input = input(">>> ").lower()
    while user_input != "q":
        if user_input == "c":
            taxi_choice = choose_taxi(total_bill)
        elif user_input == "d":
            total_bill = drive(taxi_choice, total_bill)

        menu()
        user_input = input(">>> ").lower()
    print("Total trip cost: ${}".format(total_bill))
    print("Taxis are now: ")
    list_taxis()


def drive(taxi_choice, total_bill):
    trip_distance = float(input("Drive how far? "))
    taxis[taxi_choice].drive(trip_distance)
    fare = taxis[taxi_choice].get_fare()
    print("Your {} trip cost you ${}".format(taxis[taxi_choice].name, fare))
    total_bill += fare
    print("Bill to date: ${}".format(total_bill))
    return  total_bill


def menu():
    print("q)uit, c)hoose taxi, d)rive")


def choose_taxi(total_bill):
    print("Taxis available:")
    list_taxis()
    taxi_choice = int(input("Choose taxi: "))
    print("Bill to date: ${}".format(total_bill))
    return taxi_choice


def list_taxis():
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi.__str__()))

main()