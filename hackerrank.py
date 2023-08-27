if __name__ == '__main__':
    n = int(input())
    list=["None"]*n
    for i in range(0,n) :
        ele=input().split() 
        list.append(ele)
    for i in range(0,n-1) :
        for j in range(0,n-2) :
            if list[i] > list[i+1] :
                temp = list[i]
                list[i] = list[i+1]
                list[i] = temp
    print(list[1])

