"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)


    my_limo = Car(100)
    my_limo.add_fuel(20)
    print("Limo has {} units of fuel left".format(my_limo.fuel))
    my_limo.drive(115)
    print("Limo's odometer is {}".format(my_limo.odometer))


main()
