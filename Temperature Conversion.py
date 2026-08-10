#Name: Brian Butler (BB)
#Assignment: Temperature Converter

#Reflection: I liked how easy it is to convert Fahrenheit to Celsius learning the code was a bit challenging but it is a useful tool.

#1.I have learned the "if" on the outside picks the scale and the inner "if" checks the limit

#2.Have a better understanding of the Comparison Operators (==) for equality and the (=) to assign

#3.input() always gives you a string, you need float() before doing any comparisons or math.

#if/else  Theres one condition which is true takes one path and false takes path number 2 every run can only go one of 2 ways. 
#if/elif/else allows for 3 or more paths to take, if the first condition is true it skips the rest,
#else- catches everything else that did not match anything. I used all 3 if/elif/else

#Struggled with keeping the nested indentation straight.

print("Welcome to Brian's Temperature Converter!")
print()

fTempEnteredBB= float(input("Enter a temperature: "))
sScaleBB = input("Is the temperature entered F for Fahrenheit or C for Celsius? ")

if sScaleBB == "F" or sScaleBB == "f":
    if fTempEnteredBB > 212:
        print ("Temp can not be > 212")
    else:
        fCelsiusBB = (5.0 / 9) * (fTempEnteredBB - 32)
        print(f"The Celsius equivalent is: {fCelsiusBB:.1f}")
elif sScaleBB == "C" or sScaleBB == "c":
    if fTempEnteredBB > 100:
        print ("Temp can not be > 100")
    else:
        fFahrenheitBB = (9.0 / 5.0) * fTempEnteredBB + 32
        print(f"The Fahrenheit equivalent is: {fFahrenheitBB:.1f}")
else:
    print ("Enter a F or C")
