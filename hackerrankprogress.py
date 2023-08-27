if __name__ == '__main__':
    n = int(input())
    temp = 0 
    list=['None']*n
    list=input().split()
    sum = 0
    k = ['None']*n
    for j in range (0,n):
        list[j]=int(list[j])
    for j in range (0,n):
       for i in range(0,n) :
           sum = sum + list[i]
       c=sum
       for i in range (0,n) :
             if list[i] < sum :
              sum = list[i]
              b=i
       list[b]=c
       if sum not in k :
        k[j]=int(sum)
       else :
        j=j-1 
       l=[]
    l=[ ele for ele in k if ele != 'None']
    print(l)
