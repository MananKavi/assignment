# Program to compute n+nn+nnn+...
def Series(number, limit):
	str_n = str(number)
	
	sums = number
	sum_str = str(number)
	
	for i in range(1, limit):
		sum_str = sum_str + str_n
		sums = sums + int(sum_str)
	return sums


number = int(input("Enter a number : "))
limit = int(input("Enter limit : "))
total = Series(number, limit)
print(total)
