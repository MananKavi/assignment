# Program for swapping without temp variable
number1: int = input("Enter first number  : ")
number2: int = input("Enter second number : ")

print(str(number1) + " and " + str(number2))

number1 = int(number1) + int(number2)
number2 = int(number1) - int(number2)
number1 = int(number1) - int(number2)

print("After swapping")
print(str(number1) + " and " + str(number2))
