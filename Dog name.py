#Author: Brian Butler
#Purpose: Learning to put data types, conversions, 
CONVERSION_FACTOR = 7.3

#1. Prompt and convert for a dog's name:
sNameOfDog = input("What is your dog's name:")

sAge = input(f"What is {sNameOfDog}'s age:")
fAge = float(sAge)

#iAge = int( input(f"What is {sNameOfDog}'s age:"))
#2. Calculate

fHumanAge = fAge *  CONVERSION_FACTOR

#3. Output
print(f"We are working with {sNameOfDog} and is {fAge} years old.")

print(sNameOfDog,format(fHumanAge,".2f"))
print(f"{sNameOfDog} human age is {fHumanAge:.2f}.")

