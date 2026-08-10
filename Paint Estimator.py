# Name: Brian Butler
# Assignment: Paint Estimator
# Reflection:
#   Share what I liked about this assignment?
#     I liked seeing how one big problem could be broken into small, single
#     purpose functions. Once each function was written, main() read almost
#     like a plain-English list of the steps, which made the program easy to
#     follow and easy to test one piece at a time.
#
#   Share what I struggled with?
#     The part I struggled with most was the input validation. Getting the
#     try/except and the while loop to work together so that a bad entry
#     (a word, a zero, or a negative number) re-prompts the user instead of
#     crashing took a few tries before it behaved the way I wanted.
#
#   Explain in your own words what a function is and how to code and use one?
#     A function is a named block of code that does one job. You code one with
#     the "def" keyword, a name, and a set of parameters in parentheses that
#     act like input values, and you use "return" to hand a result back. You
#     use (call) a function by writing its name with any needed arguments, and
#     you can store what it returns in a variable, like:
#         fPaintPriceBB = getFloatInput("Enter paint price per gallon: ")
#
#   In your own words share 2 reasons why you should code functions:
#     1. They stop repetition. Instead of copying the same validation code
#        five times, I wrote getFloatInput once and called it five times.
#     2. They make the program easier to read and fix. Each function is small
#        and does one thing, so if a calculation is wrong I know exactly which
#        function to open instead of searching through one giant block of code.

import math


def getFloatInput(strPromptBB):
    while True:
        try:
            fValueBB = float(input(strPromptBB))
        except ValueError:
            print("Invalid entry. Please enter a numeric value.")
            continue
        if fValueBB <= 0:
            print("Please enter a non-zero, positive number.")
            continue
        return fValueBB


def getGallonsOfPaint(fSquareFeetBB, fFeetPerGallonBB):
    return math.ceil(fSquareFeetBB / fFeetPerGallonBB)


def getLaborHours(fLaborHoursPerGallonBB, iGallonsBB):
    return fLaborHoursPerGallonBB * iGallonsBB


def getLaborCost(fLaborHoursBB, fLaborChargePerHourBB):
    return fLaborHoursBB * fLaborChargePerHourBB


def getPaintCost(iGallonsBB, fPaintPriceBB):
    return iGallonsBB * fPaintPriceBB


def getSalesTax(strStateBB):
    strStateBB = strStateBB.upper()
    if strStateBB == "CT":
        return 0.06
    elif strStateBB == "MA":
        return 0.0625
    elif strStateBB == "ME":
        return 0.085
    elif strStateBB == "NH":
        return 0.0
    elif strStateBB == "RI":
        return 0.07
    elif strStateBB == "VT":
        return 0.06
    else:
        return 0.0


def showCostEstimate(strLastNameBB, iGallonsBB, fLaborHoursBB,
                     fPaintCostBB, fLaborCostBB, fTaxBB, fTotalBB):
    strOutputBB = ("Gallons of paint: " + str(iGallonsBB) + "\n" +
                   "Hours of labor: " + str(fLaborHoursBB) + "\n" +
                   "Paint charges: $" + format(fPaintCostBB, ",.2f") + "\n" +
                   "Labor charges: $" + format(fLaborCostBB, ",.2f") + "\n" +
                   "Tax: $" + format(fTaxBB, ",.2f") + "\n" +
                   "Total cost: $" + format(fTotalBB, ",.2f"))

    print(strOutputBB)

    strFileNameBB = strLastNameBB + "_PaintJobOutput.txt"
    fileBB = open(strFileNameBB, "w")
    fileBB.write(strOutputBB + "\n")
    fileBB.close()

    print()
    print("File: " + strFileNameBB + " was created.")


def main():
    fSquareFeetBB = getFloatInput("Enter wall space in square feet: ")
    fPaintPriceBB = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallonBB = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallonBB = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHourBB = getFloatInput("Labor charge per hour: ")

    strStateBB = input("State job is in: ")
    strLastNameBB = input("Customer Last Name: ")

    iGallonsBB = getGallonsOfPaint(fSquareFeetBB, fFeetPerGallonBB)
    fLaborHoursBB = getLaborHours(fLaborHoursPerGallonBB, iGallonsBB)
    fPaintCostBB = getPaintCost(iGallonsBB, fPaintPriceBB)
    fLaborCostBB = getLaborCost(fLaborHoursBB, fLaborChargePerHourBB)
    fTaxRateBB = getSalesTax(strStateBB)
    fTaxBB = (fPaintCostBB + fLaborCostBB) * fTaxRateBB
    fTotalBB = fPaintCostBB + fLaborCostBB + fTaxBB

    print()
    showCostEstimate(strLastNameBB.strip(), iGallonsBB, fLaborHoursBB,
                     fPaintCostBB, fLaborCostBB, fTaxBB, fTotalBB)


main()
