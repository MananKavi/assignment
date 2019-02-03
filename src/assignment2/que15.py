# Program to print all integers that aren't divisible by 2 or 3
for number in range(1, 51):
	if number % 2 != 0 and number % 3 != 0:
		print(number, end=" ")
