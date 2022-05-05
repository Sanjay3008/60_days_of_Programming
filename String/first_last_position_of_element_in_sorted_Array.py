x = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ]

target = 5
start = 0
end = 0
i = 0
while(i<len(x)):
    if(x[i]==target):
        start = i

        while(x[i]==target):
            i=i+1

        end = i-1
        break
    i=i+1

print(start,end)
