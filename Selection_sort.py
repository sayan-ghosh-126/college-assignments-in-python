def Selection_sort(InputList):
    for i in range(len(InputList)):
        min_i=i
        for j in range(i+1,len(InputList)):
            if(InputList[min_i]>InputList[j]):
                min_i=j
                InputList[i],InputList[min_i]=InputList[min_i],InputList[i]
n=int(input("Please enter the size of list:"))
InputList=[]                
for i in range(n):
    InputList.append(int(input("enter%dth element:"%i)))
Selection_sort(InputList)
print("The sorted list is below:")
print(InputList)
