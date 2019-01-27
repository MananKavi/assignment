principalAmount = input("Enter your principal amount : ")
n = input("Enter time duration in year : ")
rateOfInterest = 10

loanInterest = (float(principalAmount) * float(rateOfInterest) * float(n)) / (10 * 100 * 12)

print(str(loanInterest) + " is your loan interest")
