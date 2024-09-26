#calculator
print("1.ADDITION")
print("2.SUBTRACT")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("CHOOSE AN OPTION:")
option=int(input("Enter an operation:"))
if (option in [1,2,3,4]):
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    if (option==1):
        result=num1+num2
    elif (option==2):
        result=num1-num2
    elif (option==3):
        result=num1*num2
    elif (option==4):
        result=num1//num2

else:
    print("invalid option entered!")

print("the result of the operation is {}".format(result))