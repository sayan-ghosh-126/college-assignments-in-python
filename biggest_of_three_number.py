num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if(num1>num2):
    if(num1>num3):
        print("The Biggest number is:first number=",num1)
    else:
        print("The Biggest number is:third number=",num3)  
else:
    if(num2>num3):
        print("The Biggest number is:second number=",num2)
    else:
        print("The Biggest number is:third number=",num3)
