n=int(input())
for i in range(0,n) : 
    for s in range(0,i):
        print(' ',end='')
    for k in range(1,(2*n)-(2*i)) :
        print(k,end='')
    print()    
        
