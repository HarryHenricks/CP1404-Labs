"""
Program to calculate and display a user's bonus on sales.
If sales are under $1000, the user gets a 10% bonus.
If sales are $1000 or over, the bonus is 15%.
"""
sales = 1

while sales >= 0:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        print("Invalid")
        break

    if sales < 1000:
        user_bonus = sales * 0.1
    elif sales >= 1000:
        user_bonus = sales * 0.15

    print(user_bonus)

