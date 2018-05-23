
from car import Car
import random

class UnReliable(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):

        reliability_requirement = random.uniform(0, 100)


        if self.reliability > reliability_requirement:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("Car is too unreliable to make the journey")

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)


