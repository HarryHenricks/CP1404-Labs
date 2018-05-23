

from silverservicetaxi import SilverServiceTaxi

Silver_Taxi = SilverServiceTaxi("Hummer", 200, 4)

print(Silver_Taxi)
Silver_Taxi.drive(10)
Silver_Taxi.get_fare()


Test = SilverServiceTaxi("Test", 100, 2)
Test.drive(18)
print(Test.get_fare())
