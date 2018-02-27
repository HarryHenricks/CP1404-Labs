"""
Program to allow users to estimate their electricity bill
"""

price_kWh = float(input("Please enter your price per kilowatt in cents"))
daily_usage = float(input("How many kilowatts do you use per day?"))
biling_days = int(input("How many days are in your biling period?"))
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

bill = (price_kWh * daily_usage * biling_days)/100 # divide by 100 to change cents to dollars

user_tariff = int(input("Which tariff do you have, 11 or 31?"))


if user_tariff == 11:
    bill = bill + (bill * TARIFF_11)

elif user_tariff == 31:
    bill = bill + (bill * TARIFF_31)

else:
    print("Invalid response")


print("$", bill)
