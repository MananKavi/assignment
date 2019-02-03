# Program to print odd numbers of input range.
start = int(input("Enter starting range : "))
last = int(input("Enter closing range  : "))

for number in range(start, last + 1):
	if number % 2 != 0:
		print(number, end=", ")
