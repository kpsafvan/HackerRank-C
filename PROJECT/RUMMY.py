def getscore() :
 for i in range(0,n) :
   print('Score of ',name[i],':') 
   score[i]=score[i] + int(input())
def printscore() :
  for i in range(0,n) :
   print(name[i],':',score[i])
def checkwin() :
  for i in range(0,n) :
      if score[i] > scorelimit :
          print(name[i],'purathayiiii')
n=int(input('Number of players :'))
game='y'
print('Player names :')
name = ['None']*n
score = [0]*n
for i in range(0,n) :
    name[i]=input()
scorelimit=int(input('Score limit :'))    
while game =='y' :
 getscore()
 printscore()
 checkwin()
 game=input('Enter y to continue')


   
  

 
