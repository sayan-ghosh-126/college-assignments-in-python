
def Insertion_Sort(InputList):
	for i in range(1, len(InputList)):
		Next_Element = InputList[i]
		j = i-1
		while j >=0 and Next_Element < InputList[j] :
				InputList[j+1] = InputList[j]
				j -= 1
		InputList[j+1] =Next_Element
n=int(input("Please enter the size of list:"))
InputList=[]                
for i in range(n):
    InputList.append(int(input("enter%dth element:"%i)))
Insertion_Sort(InputList)
print("The sorted list is below:")
print(InputList)




       