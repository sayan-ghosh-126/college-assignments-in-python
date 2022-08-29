r=int(input("enter the total term:"))
a=0
b=1
if(r==1):
    print(a)
elif(r==2):
    print(a)
    print(b)
else:
     print(a)
     print(b)
     for i in range(3,r+1):
        c=a+b
        print(c)
        a=b
        b=c        