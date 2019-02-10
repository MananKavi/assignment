# Program to count vowels in text file.
def countvowels(string):
	num_vowels = 0
	for char in string:
		if char in "aeiouAEIOU":
			num_vowels = num_vowels + 1
	return num_vowels


with open("resource.txt", "r") as fileReader:
	print("The number of vowels in the file is", countvowels(fileReader.read()))
