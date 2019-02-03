# Program to reverse a give number
number = input("Enter a number : ")
reverse = 0

while int(number) > 0:
	reminder = int(number) % 10
	reverse = (reverse * 10) + reminder
	number = int(number) // 10

print("Reverse of given number is " + str(reverse))
