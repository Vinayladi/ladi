n = int(input())
arr = list(map(int,input().split()))
le = 0
de,i = 1,1
temp = [0]*n
for i in range(n):
    temp[:] = arr
    del temp[i]
    print(temp)
    j = 1
    te = 1
    while j<n-1:
        if temp[j]<temp[j-1]:
            te += 1
        else:
            if le <te:
                le = te
            te = 0
        j += 1
    if le < te:
        le = te
    
print(le)
            
