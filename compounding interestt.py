# Name: Brian Butler
# Assignment: Compound Loops
# Reflection:
# What I liked about this assignment:
#   I liked seeing how the money grows each month with compounding interest.
#   It feels useful since I can use this for my own savings or car plans.
#
# What I struggled with:
#   I struggled a bit with where to put the .2f for formatting and making sure
#   the interest rate was converted right from percent to a monthly decimal.
#
# Common and difference of Python while and for loops:
#   Common: Both while and for loops repeat a block of code.
#   Difference: A for loop is used when you know how many times to repeat,
#               like a range of numbers. A while loop repeats as long as a
#               condition is True, so it's better when you don't know how
#               many times you'll need.
#
# Which type of loops did you use for this assignment and why?
#   I used a for loop to go through each month the user entered, because I
#   knew exactly how many months to show. I used a while loop to figure out
#   how many months it takes to reach the goal, because I didn't know that
#   number ahead of time.
#
# How many loops are present in your code?
#   There are 5 loops total:
#     - 4 while loops for input validation (deposit, rate, months, goal)
#     - 1 for loop to show month-by-month balance
#     - 1 while loop to calculate months to reach the goal
#
# 3 things you learned on this assignment:
#   1. How to validate numeric input with try/except and keep asking until it's valid.
#   2. How to convert an annual interest rate percent into a monthly decimal rate.
#   3. When to use a for loop vs a while loop in a real calculation.


while True:
    try:
        fDepositBB = float(input("Enter the initial deposit ($): "))
        if fDepositBB <= 0:
            print("Deposit must be a positive number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid entry. Please enter a numeric value.")

while True:
    try:
        fRatePercentBB = float(input("Enter the annual interest rate (%): "))
        if fRatePercentBB <= 0:
            print("Interest rate must be a positive number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid entry. Please enter a numeric value.")

while True:
    try:
        iMonthsBB = int(input("Enter the number of months: "))
        if iMonthsBB <= 0:
            print("Number of months must be a positive integer greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid entry. Please enter a whole number.")

while True:
    try:
        fGoalBB = float(input("Enter your savings goal ($): "))
        if fGoalBB < 0:
            print("Savings goal cannot be negative.")
            continue
        break
    except ValueError:
        print("Invalid entry. Please enter a numeric value.")


fMonthlyRateBB = (fRatePercentBB / 100) / 12


fBalanceBB = fDepositBB

print("\n" + "=" * 50)
print(f"{'Month':<6} {'Balance':>12}")
print("=" * 50)

for iMonthBB in range(1, iMonthsBB + 1):
    fInterestBB = fBalanceBB * fMonthlyRateBB
    fBalanceBB = fBalanceBB + fInterestBB
    print(f"{iMonthBB:<6} ${fBalanceBB:>10,.2f}")

print("=" * 50)
print(f"Final balance after {iMonthsBB} months: ${fBalanceBB:,.2f}")
print(f"Total interest earned: ${fBalanceBB - fDepositBB:,.2f}")


fGoalBalanceBB = fDepositBB
iMonthsToGoalBB = 0

if fGoalBB > fDepositBB:
    while fGoalBalanceBB < fGoalBB:
        fInterestGoalBB = fGoalBalanceBB * fMonthlyRateBB
        fGoalBalanceBB = fGoalBalanceBB + fInterestGoalBB
        iMonthsToGoalBB = iMonthsToGoalBB + 1

    print(f"\nIt will take {iMonthsToGoalBB:,} month(s) to reach your goal of ${fGoalBB:,.2f}.")
else:
    print(f"\nYour initial deposit already meets or exceeds your goal of ${fGoalBB:,.2f}.")
