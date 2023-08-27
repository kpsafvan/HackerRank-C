import random
a = range(1,random.randint(6,10)*random.randint(6,10))
b = range(1,random.randint(1,10)*random.randint(1,10))
c=[]
for i in a :
 for j in b :
     if i == j :
      if i not in c :
        c.append(i)
print(c)
print(a)
print(b)

         
