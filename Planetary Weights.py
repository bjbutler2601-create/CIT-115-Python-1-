#Author: Brian Butler

#Planetary Weights

#Reflection:
#What I really liked? Well seeing as it is my first code for this class I thought it was pretty cool to see it run and actually work!!

#I most definitly struggled with a letter or two being lower case while the variable was capitolized. 

#I used formatting like :10.2f to make the numbers line up neatly. The 10 gives the value a fixed width, and the .2f keeps it to two decimal places.

#Three things I learned in this assignment, Calculations with variables and multiplication to find the planets weight.
#Learned how to format output so the results line up neatly using f-strings and number formatting.
#And I also learned how to get output from the user with the input function.

sNameBB = input("What is your name?")

sEarthWeightBB =float(input("What is your Weight?"))

nMercuryBB = sEarthWeightBB * 0.38
nVenusBB = sEarthWeightBB * 0.91
nMoonBB = sEarthWeightBB * 0.165
nMarsBB = sEarthWeightBB * 0.38
nJupiterBB = sEarthWeightBB * 2.34
nSaturnBB = sEarthWeightBB * 0.93
nUranusBB = sEarthWeightBB * 0.92
nNeptuneBB = sEarthWeightBB * 1.12
nPlutoBB = sEarthWeightBB * 0.066

print(f"{sNameBB} here are your weights on our Solar System's planets:")
print(f"Weight on Mercury:         {nMercuryBB:10.2f}")
print(f"Weight on Venus:           {nVenusBB:10.2f}")
print(f"Weight on our Mooon:       {nMoonBB:10.2f}")
print(f"Weight on Mars:            {nMarsBB:10.2f}")
print(f"Weight on Jupiter:         {nJupiterBB:10.2f}")
print(f"Weight on Saturn:          {nSaturnBB:10.2f}")
print(f"Weight on Uranus:          {nUranusBB:10.2f}")
print(f"Weight on Neptune:         {nNeptuneBB:10.2f}")
print(f"Weight on Pluto:           {nPlutoBB:10.2f}")
