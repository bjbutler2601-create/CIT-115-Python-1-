# Name: Brian Butler
# Assignment: Grade Analyzer
# Reflection: What I liked about this assignment was figuring out how to find the
#             lowest test score using only comparison logic instead of built-in
#             tools like min() or lists - it forced me to think through the actual
#             logic instead of relying on a shortcut function.

#             What I struggled with was making sure the average calculation only
#             happened ONE time no matter which path (drop lowest or not) was taken,
#             instead of writing the division formula twice.
#             I figured out how to drop the lowest grade by comparing each test
#             score against the other three using <= in an if/elif/else chain.
#             Whichever test score is less than or equal to all three others is
#             the lowest, so I add up the other three and set the divisor to 3.
#             I used 4 "if" checks total for that: one per test score, plus the
#             final "else" catches the last remaining case.

#            Top 3 things I learned on this assignment:
#             1. How to validate user input and stop a program safely with exit()
#                or raise SystemExit instead of letting bad data cause errors later.
#             2. How to structure if/elif/else chains so only ONE calculation
#                block runs, keeping the code efficient and avoiding duplicate work.
#             3. How to convert a raw numeric average into a letter grade using a
#                clean if/elif/else "ladder" that checks ranges from high to low.


sNameBB = input("Enter the person's name for the Grade Analyzer: ")


iTest1BB = int(input("Enter test score 1 (whole number): "))
iTest2BB = int(input("Enter test score 2 (whole number): "))
iTest3BB = int(input("Enter test score 3 (whole number): "))
iTest4BB = int(input("Enter test score 4 (whole number): "))


sDropLowestBB = input("Should the lowest grade be dropped? Enter Y or N: ")


if iTest1BB < 0 or iTest2BB < 0 or iTest3BB < 0 or iTest4BB < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit


if sDropLowestBB != "Y" and sDropLowestBB != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit


if sDropLowestBB == "Y":
   
    if iTest1BB <= iTest2BB and iTest1BB <= iTest3BB and iTest1BB <= iTest4BB:
    
        iSumBB = iTest2BB + iTest3BB + iTest4BB
        iDivisorBB = 3
    elif iTest2BB <= iTest1BB and iTest2BB <= iTest3BB and iTest2BB <= iTest4BB:
    
        iSumBB = iTest1BB + iTest3BB + iTest4BB
        iDivisorBB = 3
    elif iTest3BB <= iTest1BB and iTest3BB <= iTest2BB and iTest3BB <= iTest4BB:
       
        iSumBB = iTest1BB + iTest2BB + iTest4BB
        iDivisorBB = 3
    else:
       
        iSumBB = iTest1BB + iTest2BB + iTest3BB
        iDivisorBB = 3
else:
  
    iSumBB = iTest1BB + iTest2BB + iTest3BB + iTest4BB
    iDivisorBB = 4


fAverageBB = iSumBB / iDivisorBB


if fAverageBB >= 97.0:
    sGradeBB = "A+"
elif fAverageBB >= 94.0:
    sGradeBB = "A"
elif fAverageBB >= 90.0:
    sGradeBB = "A-"
elif fAverageBB >= 87.0:
    sGradeBB = "B+"
elif fAverageBB >= 84.0:
    sGradeBB = "B"
elif fAverageBB >= 80.0:
    sGradeBB = "B-"
elif fAverageBB >= 77.0:
    sGradeBB = "C+"
elif fAverageBB >= 74.0:
    sGradeBB = "C"
elif fAverageBB >= 70.0:
    sGradeBB = "C-"
elif fAverageBB >= 67.0:
    sGradeBB = "D+"
elif fAverageBB >= 64.0:
    sGradeBB = "D"
elif fAverageBB >= 60.0:
    sGradeBB = "D-"
else:
    sGradeBB = "F"


print("Name:", sNameBB)
print("Average:", format(fAverageBB, ".1f"))
print("Letter Grade:", sGradeBB)
