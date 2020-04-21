num1= int(input("Enter first number:"))
num2= int(input("Enter Second number:"))
print("Select any of the one '+,-,*,/,%'")
num3= input()
if num1== 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1== 56 and num2 == 9 and num3== '+':
    print("77")
elif num1== 56 and num2 == 6 and num3== '/':
    print("4")
elif num3== '*':
    print(num1*num2)
elif num3== '+':
    print(num1+num2)
elif num3== '/':
    print(num1/num2)

elif num3== '-':
    print(num1-num2)

elif num3== '%':
    print(num1%num2)

else:
    print("Out of ramge")