import random
q=0
a=random.randint(0,4)
c='y'
while c !='n' :
 print('Enter the number')
 b=int(input())
 q=q+1
 if a == b :
     print('You guessed correctly')
     print('Took you',q,'tries')
     c='n'
 else :
     print('Try again')
     print('Press y to continue and n to exit')
     c=input().lower()
y=input()
     
