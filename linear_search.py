def linear_search(list,n,x):
    for i in range(n):
        if(x==list[i]):
            print("element found at position:",i+1)
n=int(input("Enter the size of list:"))
list=[]
for i in range(n):
   list.append(int(input("please enter %dth element:"%i)))
print(list)
x=int(input("Enter the searchable element:"))
linear_search(list, n, x)