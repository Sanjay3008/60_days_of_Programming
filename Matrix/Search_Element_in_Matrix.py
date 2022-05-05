matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 30
found = False
for i in range(0,len(matrix),1):
    for j in range(0,len(matrix),1):
        if(matrix[i][j]==target):
            found = True
            break
    if(found):
        break

if(found):
    print("Present")
else:
    print("Not Present")
