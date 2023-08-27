import random
a=[[0]*90000]*90000 
def printsudo() :
 for i in range(0,90000) :
    for j in range(0,90000) :
        a[i][j]=random.randint(-900000,900000)
        print(a[i][j]*a[i][j],'  ',end='')
    print('\n')    
printsudo()
print(a[6][6])
        
