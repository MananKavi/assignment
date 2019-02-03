# Program to find whether number is palindrome or not.
number = input('Enter any number : ')
value = int(number)

if number == str(number)[::-1]:
	print('The given number is PALINDROME')
else:
	print('The given number is NOT a palindrome')
