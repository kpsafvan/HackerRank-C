list=[]
list=input()
l=len(list)
x=int(l/2)
flag=0
for i in range(0,x) :
    if list[i] != list[-1-i] :
     flag=1
if flag == 1 :
    print("pallindrome allaaaaa")
else : 
    print("pallindrome aan monuseeee")
input()
