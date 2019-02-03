# Program to display grade
bigData = int(input("Enter marks of Big Data out of 100          : "))
dataMining = int(input("Enter marks of Data Mining out of 100       : "))
python = int(input("Enter marks of Python out of 100            : "))
java = int(input("Enter marks of Java out of 100              : "))
computerGraphics = int(input("Enter marks of Computer Graphics out of 100 : "))

percentage = ((bigData + dataMining + python + java + computerGraphics) * 100) / 500

if percentage > 90:
	print("Your Grade is A+")
elif 80 < percentage <= 90:
	print("Your Grade is A")
elif 70 < percentage <= 80:
	print("Your Grade is B+")
elif 60 < percentage <= 70:
	print("Your Grade is B")
elif 50 < percentage <= 60:
	print("Your Grade is C+")
elif 40 < percentage <= 50:
	print("Your Grade is C")
elif 33 < percentage <= 40:
	print("Your Grade is D")
else:
	print("Your Failed!!!")
