# Program to print all possible combinations of inputted 3 digits
number1 = int(input("Enter first number  : "))
number2 = int(input("Enter second number : "))
number3 = int(input("Enter third number  : "))

digits = [number1, number2, number3]

for i in range(0, 3):
	for j in range(0, 3):
		for k in range(0, 3):
			if (i != j & j != k & k != i):
				print(digits[i], digits[j], digits[k])
