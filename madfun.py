# madfun.py
# Ben Underwood

import math

number = float(input("Enter a number with a decimal: "))

print("The absolute value of your number is:", abs(number))

print("Your number rounded is:", float(round(number)))

# The example shows a float being returned

print("The square root of the absolute value of your rounded number is:", math.sqrt(abs(round(number))))

# Alternatively, we can use abs(round(number)) ** 0.5 to calculate the square root