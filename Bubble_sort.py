def Bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
n=int(input("Please enter the size of list:"))
list=[]                
for i in range(n):
    list.append(int(input("enter%dth element:"%i)))
Bubble_sort(list)
print("The sorted list is below:")
print(list)        