num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
option = input("Enter arithmetic operator (like +,-,*,/,%,^): \n")

if option == '+':
    ans = int(num1) + int(num2)
    print(ans)
elif option == '-':
    ans = int(num1) - int(num2)
    print(ans)
elif option == '*':
    ans = int(num1) * int(num2)
    print(ans)
elif option == '/':
    ans = int(num1) / int(num2)
    print(ans)
elif option == '%':
    ans = int(num1) % int(num2)
    print(ans)
elif option == '^':
    ans = pow(int(num1), int(num2))
    print(ans)
else:
    print("Invalid Input")
