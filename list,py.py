a=[1,2,5,3,7,3,7,4,6,7,3,4,5,6,8,9,9]
b=[None]*100
i=-1
for ele in a :
  if ele > 5 :
      i=i+1
      b[i]=ele
for k in range(0,i+1) :
        print(b[k])
   
n=int(input())
