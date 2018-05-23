
from UnreliableCar import UnReliable
import random


car = UnReliable("Test", 10, 1)

car.drive(10)
print("{}".format(car.__str__()))


