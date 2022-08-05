def Binary_search(sorted_list,n,x):
    start=0
    end=n-1
    while(start<=end):
        mean=(start+end)//2
        if(x==sorted_list[mean]):
            return mean
        elif(x<sorted_list[mean]):
            end=mean-1
        else:
            start=mean+1
    return -1
n=int(input("Enter the size of list:"))
sorted_list=[]
for i in range(n):
   sorted_list.append(int(input("please enter %dth element:"%i)))
print(sorted_list)
x=int(input("Enter the searchable element:"))
position=Binary_search(sorted_list, n, x) 
if(position!=-1):
    print("enter number %d is present at %d",(x,position))
else:
    print("element not found!!!")                      