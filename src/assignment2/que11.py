# Program to calculate sum of digits in number.
number = int(input("Enter a number : "))
sumOfDigits = 0

while number > 0:
	dig = number % 10
	sumOfDigits = sumOfDigits + dig
	number = number // 10

print("The sum of digits is : " + str(sumOfDigits))
