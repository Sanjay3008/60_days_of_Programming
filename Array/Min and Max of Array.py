arr = [1000, 11, 445, 1, 330, 3000];

min = arr[0]
max = arr[0]

for i in range(1,len(arr),1):
    if(arr[i]>max):
        max = arr[i]
    elif(arr[i]<min):
        min = arr[i]

print(min,max)
