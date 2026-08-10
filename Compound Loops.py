# =====================================================================
# Name:        Brian Butler
# Code Name:   Compound Loops
#
# Reflection:
#   What I liked about this assignment:
#     The part I liked most was the goal predictor. It's kind of cool
#     that the program can tell me how many months it'll take to hit a
#     number when I don't even know the answer going in. Watching the
#     balance go up every single month also made compound interest
#     finally click for me.
#
#   What I struggled with:
#     The input validation gave me the most trouble by far. Getting it
#     to catch someone typing letters and also block zeros and negatives
#     without the whole program crashing took me a bunch of tries. I
#     kept mixing up when to use try/except versus a plain if statement
#     before it finally made sense.
#
#   Common and difference of Python while and for loops:
#     They both repeat code, that's the main thing they have in common.
#     The difference is a for loop is for when you already know how many
#     times you're going to loop, and a while loop is for when you don't
#     and you just keep going until something changes. So I reached for a
#     for loop when the count was set and a while loop when it wasn't.
#
#   Which type of loops did I use and why:
#     I ended up using both. I used a for loop for the month-by-month
#     table since the user tells me exactly how many months to run. I
#     used while loops for the goal predictor and for all the input
#     checks, because in those cases I don't know ahead of time how many
#     times I'll need to loop.
#
#   How many loops in total did I code:
#     6 total -- four while loops for checking the inputs, one for loop
#     for the table, and one while loop for the goal.
#
#   Top 3 things I learned on this assignment:
#     1. How try/except keeps the program from blowing up when someone
#        types something that isn't a number.
#     2. How compound interest actually builds -- the interest gets
#        added back in, so every month grows off a bigger number than
#        the one before it.
#     3. How to format money and big numbers so they line up nicely with
#        commas and two decimals.
# =====================================================================


while True:
    try:
        DepositBB = float(input("Enter the initial deposit amount: $"))
        if DepositBB <= 0:
            print("The deposit must be a positive, non-zero number. Please try again.\n")
            continue
        break
    except ValueError:
        print("That is not a valid number. Please enter a numeric deposit.\n")


while True:
    try:
        InterestRateBB = float(input("Enter the annual interest rate percentage (for example 4 for 4%): "))
        if InterestRateBB <= 0:
            print("The interest rate must be a positive, non-zero number. Please try again.\n")
            continue
        break
    except ValueError:
        print("That is not a valid number. Please enter a numeric interest rate.\n")


while True:
    try:
        MonthsBB = int(input("Enter the number of months the deposit will stay in the account: "))
        if MonthsBB <= 0:
            print("The number of months must be a positive, non-zero whole number. Please try again.\n")
            continue
        break
    except ValueError:
        print("That is not a valid number. Please enter a whole number of months.\n")


    try:
        GoalBB = float(input("Enter your savings goal amount: $"))
        if GoalBB < 0:
            print("The goal cannot be negative. Please try again.\n")
            continue
        break
    except ValueError:
        print("That is not a valid number. Please enter a numeric goal.\n")


MonthlyRateBB = (InterestRateBB / 100) / 12


print("\n----- Monthly Account Balance -----")
BalanceBB = DepositBB
for MonthNumberBB in range(1, MonthsBB + 1):
    InterestBB = BalanceBB * MonthlyRateBB
    BalanceBB = BalanceBB + InterestBB
    print("Month {:>3}:   ${:>12,.2f}".format(MonthNumberBB, BalanceBB))



GoalBalanceBB = DepositBB
MonthsToGoalBB = 0
while GoalBalanceBB < GoalBB:
    GoalBalanceBB = GoalBalanceBB + (GoalBalanceBB * MonthlyRateBB)
    MonthsToGoalBB = MonthsToGoalBB + 1


print("\n----- Savings Goal Prediction -----")
print("It will take {:,} month(s) to reach your goal of ${:,.2f}.".format(MonthsToGoalBB, GoalBB))
