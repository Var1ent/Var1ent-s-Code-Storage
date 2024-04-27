# My First Calculator
# This is a simple calculator that can add, subtract, multiply, and divide

Underline = '\33[4m'
Bold = '\33[1m'

print(Underline + Bold + "-----CALCULATOR-----")
print("\n")

num1 = float(input("First number : "))

num2 = float(input("Second number : "))

print("\n")
print("\bCHOOSE THE FOLLOWING OPERATIONS")
print("\n")

print("Enter 1 for Addition \n\nEnter 2 for Subtraction \n\nEnter 3 for Multiplication \n\nEnter 4 for Division")\

print("\n")

Entered_number = int(input( "chooose a number from 1 to 4 :"))

print("\n")

if Entered_number == 1:
  print("Addition of the numbers is : ",  int(num1 + num2))

if Entered_number ==2:
  print("Subtraction of the numbers is : ", int(num1 - num2))

if Entered_number == 3:
  print("Multiplication of the numbers is : ", int(num1 * num2))

if Entered_number == 4:
  print("The Division of the number is :", int(num1 / num2))
