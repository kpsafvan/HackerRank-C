if __name__ == '__main__':
    n = int(input())
    arr = []

    for i in range(0,n):
        ele=input().split()
        arr.append(ele)
    for j in range(0,n) :
     for i in range(0,n) :
      if arr[i] < arr[i+1] :
       temp = arr[i]
       arr[i]= arr[i+1]
       arr[i+1]=temp
       print(arr[i])

print(arr)

