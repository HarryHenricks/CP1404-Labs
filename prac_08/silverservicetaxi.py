
from taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""

        super().__init__(name, fuel)

        self.price_per_km = fanciness * self.price_per_km
        self.flagfall = 4.50


    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = super().get_fare()
        return fare + self.flagfall


    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        super().__str__()
        return "{}, plus flagfall of ${}".format(super().__str__(), self.flagfall)
