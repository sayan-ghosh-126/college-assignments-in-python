class stack:
    s=[]
    def push(self):
        a=int(input("enter the number:"))
        stack.s.append(a)
    def pop(self):
        if(a.s==[]):
            print("stack is empty")
        else:
            print("deleted element is:",stack.s[n-1])
            del stack.s[n-1]
    def display(self):
        l=len(stack.s)
        print("stack contains are")
        for i in range(l):
            print(stack.s[i])
a=stack()
n=int(input("enter the size of the array")) 
for j in range(n):
    a.push()
    a.display()
print("are you want to delete? press 1 for yes and press 2 for no")
k=int(input("please enter your choice:"))
if k==1:
    a.pop()
    a.display()
else:
    a.display()                   

