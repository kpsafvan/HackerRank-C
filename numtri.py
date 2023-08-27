n=int(input())
s=n
for k in range(0,n+1) :
    for i in range(0,k) :
        print(s,end='')
        s=s-1
    print()
    s=n
for k in range(0,n-1) :
    for i in range(0,n-k-1) :
        print(s,end='')
        s=s-1
    print()
    s=n
    
