# Program to count number of alphabets and digits in file.
fileReader = open("resource.txt", "r")
words = fileReader.read()

letterCount = 0
numberCount = 0
for c in words:
	if c.isalpha():
		letterCount += 1
	elif c.isnumeric():
		numberCount += 1

print("Number of alphabets is", letterCount)
print("Number of digits is", numberCount)
