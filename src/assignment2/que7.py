# Program to print numbers in given range divisible by given number.
start = int(input("Enter lower range limit : "))
last = int(input("Enter upper range limit : "))
number = int(input("Enter the number to be divided by : "))

for divisibleNumber in range(start, last + 1):
	if divisibleNumber % number == 0:
		print(divisibleNumber)
