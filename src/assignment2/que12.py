# Program to find smallest divisor of input number.
number = int(input("Enter an integer : "))
divisor = []

for i in range(2, number + 1):
	if number % i == 0:
		divisor.append(i)

divisor.sort()

print("Smallest divisor is:", divisor[0])
