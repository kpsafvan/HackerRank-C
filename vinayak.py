c=0;
while(c==0):
    s=int(input())
    for i in range(0,s):
        for k in range (0,s-i) :
            print("*",end='')
        print('')
    c= int(input())    
