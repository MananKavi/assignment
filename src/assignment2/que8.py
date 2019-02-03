# Program to print quotient and remainder of input numbers.
number1 = input("Enter first number  : ")
number2 = input("Enter second number : ")

quotient = round(int(number1) / int(number2))
remainder: int = int(number1) % int(number2)

print("Quotient is " + str(quotient) + " and Remainder is " + str(remainder))
