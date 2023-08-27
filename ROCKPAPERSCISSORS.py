q=0
while q==0 :
 p1=input('Player One  ').lower()
 p2=input('Player Two  ').lower()
 if p1 == p2 :
  print('Draw')
 else : 
  if p1 == 'r' and p2 == 'p' :
      print('Player two wins')
  elif p1 == 'r' and p2 == 's' :
      print('Player one wins')
  elif p1 == 'p' and p2 == 'r' :
     print('Player one wins')
  elif p1 == 'p' and p2 =='s'  :
      print('Player two wins')
  elif p1 == 's' and p2 == 'r' :
      print('Player two wins')
  elif p1 == 's' and p2 == 'p' :
      print('Player one wins')
 print('Press n to exit')   
 s=input().lower()
 if s == 'n' :
  q =1
