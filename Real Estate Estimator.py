# Name: Brian Butler
# Assignment: Real Estate with Lists
#
#  Reflection:
#   What did you like about this assignment?
#     I liked that it takes a real-world scenario (analyzing property sales)
#     and turns it into a program. Building the analytics such as median and
#     commission myself made the math feel practical instead of abstract.
#
#   What did you struggle with?
#     Getting the median logic right for both odd and even sized lists took
#     some thought, especially remembering that Python list indexes start at 0
#     when I divide the count by 2 to find the middle element.
#
#   
#     A list is an ordered, changeable collection that can hold many values in
#     a single variable. Each value has a position (index) starting at 0. You
#     can add to it, remove from it, sort it, and loop through it, which makes
#     it perfect when you do not know how many items you will have ahead of time.
#
#  
#     In an earlier project I tracked quiz scores. A list let me keep adding
#     each score as it came in and then loop through them at the end to find
#     the highest, lowest, and average score without creating a separate
#     variable for every single quiz.


def getFloatInput(strPromptBB):
    """Prompt the user with the given text and return a valid, non-zero,
    positive float. Keeps asking until the user enters a good value."""
   
    while True:
       
        try:
            fValueBB = float(input(strPromptBB))
        except ValueError:
            
            print("Input a number that is greater than 0.")
            continue

       
        if fValueBB <= 0:
            print("Input a number that is greater than 0.")
            continue

        
        return fValueBB


def getMedian(lstValuesBB):
    """Receive a list of numbers and return the median as a float.
    (Written without using the statistics module.)"""
    iCountBB = len(lstValuesBB)   
    iMidBB = iCountBB // 2        

    
    if iCountBB % 2 != 0:
        fMedianBB = float(lstValuesBB[iMidBB])
    
    else:
        fMedianBB = (lstValuesBB[iMidBB] + lstValuesBB[iMidBB - 1]) / 2

    return fMedianBB


def main():
    
    lstSalesBB = []

    
    while True:
        
        fSalesPriceBB = getFloatInput("Enter property sales value: ")
        
        lstSalesBB.append(fSalesPriceBB)

        
        while True:
            strAnotherBB = input("Enter another value Y or N:")
            if strAnotherBB in ("Y", "y", "N", "n"):
                break

        
        if strAnotherBB in ("N", "n"):
            break

    
    lstSalesBB.sort()

   
    iPropertyNumberBB = 1
    for fSaleBB in lstSalesBB:
        print("Property " + str(iPropertyNumberBB) + " $ " + format(fSaleBB, ",.2f"))
        iPropertyNumberBB += 1


    fMinBB = lstSalesBB[0]
    fMaxBB = lstSalesBB[len(lstSalesBB) - 1]  

    fTotalBB = sum(lstSalesBB)

    fAverageBB = fTotalBB / len(lstSalesBB)

    fMedianBB = getMedian(lstSalesBB)

    fCommissionBB = fTotalBB * .03

    print("Minimum: " + format(fMinBB, ",.2f"))
    print("Maximum: " + format(fMaxBB, ",.2f"))
    print("Total: " + format(fTotalBB, ",.2f"))
    print("Average: " + format(fAverageBB, ",.2f"))
    print("Median: " + format(fMedianBB, ",.2f"))
    print("Commission: " + format(fCommissionBB, ",.2f"))



main()
