num=int(input("Enter a Number:"))
temp=num
arm=0
while(num!=0):
    rem=num%10
    arm=arm+(rem*rem*rem)
    num=num//10
if(temp==arm):
    print("The Number is a Armstrong Number")
else:
    print("The Number is not a Armstrong Number")        