def checkprime(num) :
 t=int(round(num/2))
 for i in range(2,t) :
     if num % i == 0 :
         return 0
 return 1
num=int(input('Enter the number'))
if checkprime(num) == 1 :
    print(num,'is a Prime number')
else :
    print(num,'is Not a Prime number')

input()    
