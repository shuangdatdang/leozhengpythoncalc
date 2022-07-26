import math

print("Welcome to the Distance Calculator")
num1 = float(input("Enter x1:"))
num2 = float(input("Enter y1:"))
num3 = float(input("Enter x2:"))
num4 = float(input("Enter y2:"))
base = num3 - num1
height = num4 - num2
totalDist = math.hypot(base, height)
print("Distance between points is " + str(totalDist) + ".")
