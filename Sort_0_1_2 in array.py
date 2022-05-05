arr= [0,2,1,2,0,1,0]

start = 0
mid = 0
last = len(arr)-1

while(mid<=last):
    if(arr[mid]==0):
        temp = arr[start]
        arr[start] = arr[mid]
        arr[mid] = temp
        start = start+1
        mid = mid+1
    elif(arr[mid]==1):
        mid = mid+1
    else:
        temp = arr[mid]
        arr[mid] = arr[last]
        arr[last] = temp
        last = last-1
    print(arr)
print(arr)
